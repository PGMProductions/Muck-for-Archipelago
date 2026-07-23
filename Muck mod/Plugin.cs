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
using System.Threading.Tasks;

namespace ARCHIPELAGO;



[BepInPlugin(MyPluginInfo.PLUGIN_GUID, MyPluginInfo.PLUGIN_NAME, MyPluginInfo.PLUGIN_VERSION)]
public class Plugin : BaseUnityPlugin
{
    public static new ManualLogSource Logger;

    public static Plugin Instance;

    public Dictionary<string, int> givenPowerups;
    public Dictionary<string, int> givenTools;

    public Harmony harmony = new Harmony("MUCK-Archipelago");

    public bool hasReceivedArrows;

    public bool deathlinked;

    private async void Awake()
    {
        // Plugin startup logic
        Logger = base.Logger;
        Logger.LogInfo($"Plugin {MyPluginInfo.PLUGIN_GUID} is loaded!");
        Logger.LogInfo("It's muckin' time");
        harmony.PatchAll();






        Instance = this;

        deathlinked = false;

        resetGivenPowerups();
        resetGivenTools();

    }


    public void Update()
    {



        if (File.Exists("receive.deathlink"))
        {
            if (GameManager.state == GameManager.GameState.Playing)
            {
                deathlinked = true;
                PlayerStatus.Instance.Damage(0,ignoreProtection: true);
                
            }

            File.Delete("receive.deathlink");
        }


        if (GameManager.state == GameManager.GameState.Playing)
        {




            try
            {
                updateGivenPowerups(getPowerupsDict());
                updateGivenTools(getToolsDict());
            }
            catch { }
            ;

        }

    }

    public async void atGameStart()
    {
        if (File.Exists("ARCHIPELAGO_Powerups.itmlst"))
        {
            File.Delete("ARCHIPELAGO_Powerups.itmlst");
        }

        if (File.Exists("ARCHIPELAGO_Locations.lctlst"))
        {
            File.Delete("ARCHIPELAGO_Locations.lctlst");
        }

        if (File.Exists("ARCHIPELAGO_Options.optlst"))
        {
            File.Delete("ARCHIPELAGO_Options.optlst");
        }

        if (File.Exists("ARCHIPELAGO_Tools.itmlst"))
        {
            File.Delete("ARCHIPELAGO_Tools.itmlst");
        }


        if (File.Exists("victory"))
        {
            File.Delete("victory");
            Logger.LogInfo("Destroying victory");
        }

        Logger.LogInfo("ARCHIPELAGO_Powerups.itmlst");
        File.WriteAllText("ARCHIPELAGO_Powerups.itmlst", "Broccoli,0\r\nDumbbell,0\r\nJetpack,0\r\nOrange Juice,0\r\nPeanut Butter,0\r\nBlue Pill,0\r\nRed Pill,0\r\nSneaker,0\r\nRobin Hood Hat,0\r\nSpooo Bean,0\r\nBulldozer,0\r\nHorseshoe,0\r\nDanis Milk,0\r\nPiggybank,0\r\nCrimson Dagger,0\r\nDracula,0\r\nJanniks Frog,0\r\nJuice,0\r\nAdrenaline,0\r\nBerserk,0\r\nCheckered Shirt,0\r\nSniper Scope,0\r\nKnuts Hammer,0\r\nWings of Glory,0\r\nEnforcer,0");

        Logger.LogInfo("Creatinng ARCHIPELAGO_Locations.lctlst");
        File.WriteAllText("ARCHIPELAGO_Locations.lctlst", "PowerupWhite,0\r\nPowerupBlue,0\r\nPowerupOrange,0\r\nAdamantite Pickaxe,0\r\nGold Pickaxe,0\r\nMithril Pickaxe,0\r\nSteel Pickaxe,0\r\nWood Pickaxe,0\r\nOak Bow,0\r\nWood Bow,0\r\nBirch bow,0\r\nFir bow,0\r\nAncient Bow,0\r\nAdamantite Axe,0\r\nGold Axe,0\r\nMithril Axe,0\r\nSteel Axe,0\r\nWood Axe,0\r\nAdamantite Boots,0\r\n_ Boots,0\r\nGold Boots,0\r\nMithril Boots,0\r\nObamium Boots,0\r\nSteel Boots,0\r\nWolfskin Boots,0\r\nAdamantite Helmet,0\r\nChunkium Helmet,0\r\nGold Helmet,0\r\nMithril Helmet,0\r\nObamium Helmet,0\r\nSteel Helmet,0\r\nWolfskin Helmet,0\r\nAdamantite Pants,0\r\nChunkium Pants,0\r\nGold Pants,0\r\nMithril Pants,0\r\nObamium Pants,0\r\nSteel Pants,0\r\nWolfskin Pants,0\r\nAdamantite Chestplate,0\r\nChunkium Chestplate,0\r\nGold Chestplate,0\r\nMithril Chestplate,0\r\nObamium Chestplate,0\r\nSteel Chestplate,0\r\nWolfskin Chestplate,0\r\nAdamantite Sword,0\r\nGold Sword,0\r\nMithril Sword,0\r\nObamium Sword,0\r\nSteel Sword,0\r\nChiefs Spear,0\r\nChunky Hammer,0\r\nGronks Sword,0\r\nNight Blade,0\r\nWyvern Dagger,0");

        Logger.LogInfo("ARCHIPELAGO_Options.optlst");
        File.WriteAllText("ARCHIPELAGO_Options.optlst", "allowLootAsLocations,0");

        Logger.LogInfo("ARCHIPELAGO_Tools.itmlst");
        File.WriteAllText("ARCHIPELAGO_Tools.itmlst", "weapons,0\r\nbows,0\r\naxes,0\r\npickaxes,0\r\nhelmets,0\r\nchestplates,0\r\nleggings,0\r\nboots,0");


        await Task.Delay(3000);



        resetGivenPowerups();
        updateGivenPowerups(getPowerupsDict());

        resetGivenTools();
        updateGivenTools(getToolsDict());


        //godMode();


        fullyHeal();
        
    }




    public void forceGivePowerup(int powerupId, int count)
    {
        FieldInfo field = PowerupInventory.Instance.GetType().GetField("powerups", BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Public);
        int[] powerups = (int[])field.GetValue(PowerupInventory.Instance);
        powerups[powerupId] += count;
        field.SetValue(PowerupInventory.Instance, powerups);

        UiEvents.Instance.AddPowerup(ItemManager.Instance.allPowerups[powerupId]);
        for (int i = 0; i < count; i++)
        {
            PowerupUI.Instance.AddPowerup(powerupId);
        }

    }


    public bool giveRightTool(string name, int count)
    {
        string[] list;
        if (name == "weapons") {
            list = Constants.weapons;
        }
        else if (name == "bows") {
            list = Constants.bows;
        }
        else if (name == "axes") {
            list = Constants.axes;
        }
        else if (name == "pickaxes") {
            list = Constants.pickaxes;
        }

        else if (name == "helmets") {
            list = Constants.helmets;
        }
        else if (name == "chestplates") {
            list = Constants.chestplates;
        }
        else if (name == "leggings") {
            list = Constants.leggings;
        }
        else if (name == "boots") {
            list = Constants.boots;
        }
        else { return false; }


        deleteAllItemsFromList(list);
        return giveUniqueItem(list[count-1],1);
    }

    public void deleteAllItemsFromList(string[] list)
    {
        int itemId = 0;
        foreach (string itemName in list)
        {
            foreach (InventoryItem baseItem in ItemManager.Instance.allScriptableItems)
            {
                if (baseItem.name == itemName)
                {
                    itemId = baseItem.id;
                    break;
                }
            }
            InventoryUI.Instance.RemoveItem(ItemManager.Instance.allScriptableItems[itemId]);
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




    public Dictionary<string, int> getPowerupsDict()        //note to self, breaks when you reach 2147483647 of a single powerup
    {
        string readText = File.ReadAllText("ARCHIPELAGO_Powerups.itmlst");

        return strToDict(readText);
    }


    public Dictionary<string, int> getToolsDict()        //note to self, breaks when you reach 2147483647 of a single powerup
    {
        string readText = File.ReadAllText("ARCHIPELAGO_Tools.itmlst");

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

    public void resetGivenTools()
    {
        Logger.LogInfo("Tools Dict Reset");
        givenTools = new Dictionary<string, int>
        {
            { "weapons",0},
            { "bows",0},
            { "axes",0},
            { "pickaxes",0},
            { "helmets",0},
            { "chestplates",0},
            { "leggings",0},
            { "boots",0}
        };
        hasReceivedArrows = false;

    }


    public void sendLocation(string locationName)
    {
        Dictionary<string, int> locationDict = strToDict(File.ReadAllText("ARCHIPELAGO_Locations.lctlst"));

        locationDict[locationName]++;
        Logger.LogInfo(dictToStr(locationDict));
        File.WriteAllText("ARCHIPELAGO_Locations.lctlst", dictToStr(locationDict));
    }

    public void sendUniqueLocation(string locationName)
    {
        Dictionary<string, int> locationDict = strToDict(File.ReadAllText("ARCHIPELAGO_Locations.lctlst"));

        Logger.LogInfo(locationName);

        if (locationDict[locationName] == 0)
        {
            sendLocation(locationName);
        }

    }

    public void sendALternateUniqueLocation(string locationName)
    {
        if (allowAlternateLocations()) 
        {
            sendUniqueLocation(locationName);
        }
    }

    public bool hasLocation(string locationName)
    {
        Dictionary<string, int> locationDict = strToDict(File.ReadAllText("ARCHIPELAGO_Locations.lctlst"));

        if (locationDict[locationName] > 0)
        {
            return true;
        }
        return false;
    }


    public static Dictionary<string, int> strToDict(string str)
    {
        string[] readList = str.Split(new string[] { Environment.NewLine, "\n" }, StringSplitOptions.None);

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
                firstLine = false;
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
                PlayerStatus.Instance.UpdateStats();
            }
        }
    }

    public void updateGivenTools(Dictionary<string, int> toolsToHave)
    {
        foreach (KeyValuePair<string, int> tool in toolsToHave)
        {
            if (tool.Value > givenTools[tool.Key])
            {
                if(giveRightTool(tool.Key, tool.Value))
                { givenTools[tool.Key] += tool.Value - givenTools[tool.Key]; }
            }
        }
        if (givenTools["bows"] > 0 && !hasReceivedArrows)
        {
            giveUniqueItem("Flint Arrow", 500 * givenTools["bows"]);
            hasReceivedArrows = true;
        }
    }



    public bool allowAlternateLocations()
    {
        return strToDict(File.ReadAllText("ARCHIPELAGO_Options.optlst"))["allowLootAsLocations"] == 1;
    }

    public void win()
    {
        File.WriteAllText("victory", "Bob defeated");
    }




    public void fullyHeal()
    {
        PlayerStatus.Instance.hp = PlayerStatus.Instance.maxHp;
    }



    public bool giveUniqueItem(string itemName, int count)
    {
        InventoryItem item = ScriptableObject.CreateInstance<InventoryItem>();
        foreach (InventoryItem baseItem in ItemManager.Instance.allScriptableItems)
        {
            if (baseItem.name == itemName)
            {
                item.Copy(baseItem, count);
                item.description = Constants.GivenItemDescription;
                break;
            }
        }


        if (InventoryUI.Instance.AddItemToInventory(item) == 1)
        {
            return false;
        }

        return true;

    }

    public void godMode()
    {
        giveUniqueItem("AncientCore", 1);
        giveUniqueItem("Obamium Boots", 1);
        giveUniqueItem("Obamium Helmet", 1);
        giveUniqueItem("Obamium Pants", 1);
        giveUniqueItem("Obamium Chestplate", 1);
        giveUniqueItem("Chiefs Spear", 1);
        giveUniqueItem("Meat Soup", 69);
        giveUniqueItem("Adamantite bar", 69);
        giveUniqueItem("Gold bar", 69);
        giveUniqueItem("Iron bar", 150);
        giveUniqueItem("Mithril bar", 69);
        giveUniqueItem("Obamium bar", 69);
        giveUniqueItem("Ruby", 69);
        giveUniqueItem("Birch Wood", 69);
        giveUniqueItem("Rock", 150);
        giveUniqueItem("Dark Oak Wood", 69);
        giveUniqueItem("Oak Wood", 69);
        giveUniqueItem("Fir Wood", 69);
        giveUniqueItem("Wood", 300);
        giveUniqueItem("Blue Gem", 69);
        giveUniqueItem("Green Gem", 69);
        giveUniqueItem("Pink Gem", 69);
        giveUniqueItem("Red Gem", 69);
        giveUniqueItem("Yellow Gem", 69);
        giveUniqueItem("Flax Fibers", 69);
        giveUniqueItem("Rope", 69);
        giveUniqueItem("Wheat", 69);
        giveUniqueItem("Raw Meat", 69);


        givenPowerups = new Dictionary<string, int>
        {
            { "Broccoli",-100 },
            { "Dumbbell",-10000 },
            { "Jetpack",-5 },
            { "Orange Juice",-100 },
            { "Peanut Butter",-100 },
            { "Blue Pill",-100 },
            { "Red Pill",-100 },
            { "Sneaker",-100 },
            { "Robin Hood Hat",-100 },
            { "Spooo Bean",-100 },
            { "Bulldozer",-100 },
            { "Horseshoe",-100 },
            { "Danis Milk",-100 },
            { "Piggybank",-100 },
            { "Crimson Dagger",-100 },
            { "Dracula",-100 },
            { "Janniks Frog",-100 },
            { "Juice",-100 },
            { "Adrenaline",-100 },
            { "Berserk",-100 },
            { "Checkered Shirt",-100 },
            { "Sniper Scope",-100 },
            { "Knuts Hammer",-100 },
            { "Wings of Glory",-100 },
            { "Enforcer",-100 }
        };
    }


}



