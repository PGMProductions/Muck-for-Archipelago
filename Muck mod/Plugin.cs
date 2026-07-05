using BepInEx;
using BepInEx.Logging;
using MonoMod.RuntimeDetour;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Threading;
using UnityEngine;
using UnityEngine.SocialPlatforms;
using UnityEngine.UIElements;
using static UnityEngine.GUI;
using HarmonyLib;

namespace ARCHIPELAGO;



[BepInPlugin(MyPluginInfo.PLUGIN_GUID, MyPluginInfo.PLUGIN_NAME, MyPluginInfo.PLUGIN_VERSION)]
public class Plugin : BaseUnityPlugin
{
    internal static new ManualLogSource Logger;

    public static Plugin Instance;

    public GameManager.GameState previousState;

    public Dictionary<string, int> givenPowerups;

    public Harmony harmony = new Harmony("MUCK-Archipelago");



    private async void Awake()
    {
        // Plugin startup logic
        Logger = base.Logger;
        Logger.LogInfo($"Plugin {MyPluginInfo.PLUGIN_GUID} is loaded!");
        Logger.LogInfo("It's muckin' time");
        harmony.PatchAll();

        if (!File.Exists("ARCHIPELAGO_Powerups.itmlst"))
        {
            Logger.LogInfo("Creatinng ARCHIPELAGO_Powerups.itmlst");
            File.WriteAllText("ARCHIPELAGO_Powerups.itmlst", "Broccoli,0\r\nDumbbell,0\r\nJetpack,0\r\nOrange Juice,0\r\nPeanut Butter,0\r\nBlue Pill,0\r\nRed Pill,0\r\nSneaker,0\r\nRobin Hood Hat,0\r\nSpooo Bean,0\r\nBulldozer,0\r\nHorseshoe,0\r\nDanis Milk,0\r\nPiggybank,0\r\nCrimson Dagger,0\r\nDracula,0\r\nJanniks Frog,0\r\nJuice,0\r\nAdrenaline,0\r\nBerserk,0\r\nCheckered Shirt,0\r\nSniper Scope,0\r\nKnuts Hammer,0\r\nWings of Glory,0\r\nEnforcer,0\r\n");
        }

        if (!File.Exists("ARCHIPELAGO_Locations.lctlst"))
        {
            Logger.LogInfo("Creatinng ARCHIPELAGO_Locations.lctlst");
            File.WriteAllText("ARCHIPELAGO_Locations.lctlst", "PowerupWhite,0\r\nPowerupBlue,0\r\nPowerupOrange,0\r\n");
        }


        Instance = this;


        resetGivenPowerups();

    }


    public void Update()
    {



        if (previousState == GameManager.GameState.Loading && GameManager.state == GameManager.GameState.Playing)
        {
            atGameStart();
        }



        if (GameManager.state == GameManager.GameState.Playing)
        {
            try
            {
                updateGivenPowerups(getPowerupsDict());
            }
            catch { }
            ;

        }


        //Logger.LogInfo($"Game state : {GameManager.state}");
        previousState = GameManager.state;
    }

    public void atGameStart()
    {
        resetGivenPowerups();
        updateGivenPowerups(getPowerupsDict());
    }




    public void forceGivePowerup(int powerupId, int count)
    {
        FieldInfo field = PowerupInventory.Instance.GetType().GetField("powerups", BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Public);
        int[] powerups = (int[])field.GetValue(PowerupInventory.Instance);
        powerups[powerupId]+= count;
        field.SetValue(PowerupInventory.Instance, powerups);

        UiEvents.Instance.AddPowerup(ItemManager.Instance.allPowerups[powerupId]);
        for (int i = 0; i < count; i++)
        {
            PowerupUI.Instance.AddPowerup(powerupId);
        }

    }

    public bool isGamePlaying() //untested
    {
        return GameManager.state == GameManager.GameState.Playing;
    }


    public bool isPlayerDead()  //untested
    {
        return GameManager.state == GameManager.GameState.GameOver;
    }

    public void printPowerupList()
    {
        foreach (KeyValuePair<string, int> powerup in ItemManager.Instance.stringToPowerupId)
        {
            Logger.LogInfo($"name : {powerup.Key}, id : {powerup.Value}");
        }
    }




    public Dictionary<string,int> getPowerupsDict()        //note to self, breaks when you reach 2147483647 of a single powerup
    {
        string readText = File.ReadAllText("ARCHIPELAGO_Powerups.itmlst");

        return strToDict(readText);
    }


    public void resetGivenPowerups()
    {
        Logger.LogInfo("Powerup Dict Reset");
        givenPowerups = new Dictionary<string, int>
        {
            { "Broccoli",0 },
            { "Dumbbell",0},
            { "Jetpack",0},
            { "Orange Juice",0},
            { "Peanut Butter",0},
            { "Blue Pill",0},
            { "Red Pill",0},
            { "Sneaker",0},
            { "Robin Hood Hat",0},
            { "Spooo Bean",0},
            { "Bulldozer",0},
            { "Horseshoe",0},
            { "Danis Milk",0},
            { "Piggybank",0},
            { "Crimson Dagger",0},
            { "Dracula",0},
            { "Janniks Frog",0},
            { "Juice",0},
            { "Adrenaline",0},
            { "Berserk",0},
            { "Checkered Shirt",0},
            { "Sniper Scope",0},
            { "Knuts Hammer",0},
            { "Wings of Glory",0},
            { "Enforcer",0}
        }; 

    }


    public void sendLocation(string locationName)
    {
        Dictionary<string, int> locationDict = strToDict(File.ReadAllText("ARCHIPELAGO_Locations.lctlst"));
        
        locationDict[locationName]++;
        Logger.LogInfo(dictToStr(locationDict));
        File.WriteAllText("ARCHIPELAGO_Locations.lctlst",dictToStr(locationDict));
    }

    public static Dictionary<string, int> strToDict(string str)
    {
        string[] readList = str.Split(new string[] { Environment.NewLine , "\n"}, StringSplitOptions.None);

        Dictionary<string, int> finalDict = new Dictionary<string, int>();

        foreach (string line in readList)
        {
            string[] splitString = line.Split(",".ToCharArray());

            finalDict.Add(splitString[0], Int32.Parse(splitString[1]));

        }
        return finalDict;
    }

    public static string dictToStr(Dictionary<string, int> dict)
    {
        string finalString = "";
        bool firstLine = true;
        foreach (KeyValuePair<string, int> line in dict)
        {
            if (firstLine)
            {
                finalString = finalString + $"{line.Key},{line.Value}";
                firstLine = false ;
            }
            else
            {
                finalString = finalString + $"\n{line.Key},{line.Value}";
            }
            
        }
        return finalString;
    }

    public void updateGivenPowerups(Dictionary<string, int> powerupsToHave)
    {
        foreach (KeyValuePair<string, int> powerup in powerupsToHave)
        {
            if (powerup.Value > givenPowerups[powerup.Key])
            {
                int nbPowerupsToGive = powerup.Value - givenPowerups[powerup.Key];
                Logger.LogInfo($"{powerup.Key} : {nbPowerupsToGive.ToString()}");
                forceGivePowerup(ItemManager.Instance.stringToPowerupId[powerup.Key], nbPowerupsToGive);
                givenPowerups[powerup.Key] += nbPowerupsToGive;
            }
        }
    }



    public void win()
    {
    File.WriteAllText("victory", "Bob defeated");
    }


}




[HarmonyPatch(typeof(PowerupInventory))]
[HarmonyPatch(nameof(PowerupInventory.AddPowerup))]
class PatcherAddPowerup
{


    static bool Prefix(string name, int powerupId, int objectId)
    {

        Vector3 position = ItemManager.Instance.list[objectId].transform.position;
        ParticleSystem component = UnityEngine.Object.Instantiate(PowerupInventory.Instance.powerupFx, position, Quaternion.identity).GetComponent<ParticleSystem>();
        ParticleSystem.MainModule main = component.main;
        main.startColor = ItemManager.Instance.allPowerups[powerupId].GetOutlineColor();


        if (ItemManager.Instance.allPowerups[powerupId].tier == Powerup.PowerTier.Orange)
        {
            component.gameObject.GetComponent<RandomSfx>().sounds = new AudioClip[1] { PowerupInventory.Instance.goodPowerupSfx };
            component.GetComponent<RandomSfx>().Randomize(0f);
        }


        if (ItemManager.Instance.allPowerups[powerupId].tier == Powerup.PowerTier.White)
        {
            Plugin.Instance.sendLocation("PowerupWhite");
        }
        else if (ItemManager.Instance.allPowerups[powerupId].tier == Powerup.PowerTier.Blue)
        {
            Plugin.Instance.sendLocation("PowerupBlue");
        }
        else if (ItemManager.Instance.allPowerups[powerupId].tier == Powerup.PowerTier.Orange)
        {
          
            Plugin.Instance.sendLocation("PowerupOrange");
        }
         return false;
    }
}




[HarmonyPatch(typeof(ServerSend))]
[HarmonyPatch(nameof(ServerSend.GameOver))]
class PatcherGameOver
{


    static bool Prefix(int winnerId = -2)
    {
         if (winnerId == -3)
        {
            Plugin.Instance.win();
        }



        return true;
    }
}