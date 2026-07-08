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




[HarmonyPatch(typeof(InventoryUI))]
[HarmonyPatch(nameof(InventoryUI.CraftItem))]
class PatcherCaftItem
{

    
    static bool Prefix(InventoryItem item)
    {
        if (Constants.itemsToPrevent.Contains(item.name))
        {

            if (!InventoryUI.Instance.IsCraftable(item) || (InventoryUI.Instance.currentMouseItem != null && (!item.Compare(InventoryUI.Instance.currentMouseItem) || InventoryUI.Instance.currentMouseItem.amount + item.craftAmount > InventoryUI.Instance.currentMouseItem.max)) || Plugin.Instance.hasLocation(item.name))
            {
                return false;
            }


            InventoryItem.CraftRequirement[] requirements = item.requirements;
            foreach (InventoryItem.CraftRequirement craftRequirement in requirements)
            {
                int num = 0;
                foreach (InventoryCell cell in InventoryUI.Instance.cells)
                {
                    if (!(cell.currentItem == null) && cell.currentItem.Compare(craftRequirement.item))
                    {
                        if (cell.currentItem.amount > craftRequirement.amount)
                        {
                            int num2 = craftRequirement.amount - num;
                            cell.currentItem.amount -= num2;
                            cell.UpdateCell();
                            break;
                        }
                        num += cell.currentItem.amount;
                        cell.RemoveItem();
                    }
                }
            Plugin.Instance.sendUniqueLocation(item.name);
            }

            

            return false;
        };

        return true;
    }
}

[HarmonyPatch(typeof(InventoryUI))]
[HarmonyPatch(nameof(InventoryUI.PickupItem))]
class PatcherPickupItem
{


    static bool Prefix(InventoryItem item)
    {
        if (Constants.itemsToPrevent.Contains(item.name) && item.description != Constants.GivenItemDescription)
        {
            Plugin.Instance.sendALternateUniqueLocation(item.name);
            return false;
        }
        ;

        return true;
    }
}

[HarmonyPatch(typeof(InventoryUI))]
[HarmonyPatch(nameof(InventoryUI.AddItemToInventory))]
class PatcherAddItemToInventory
{


    static bool Prefix(InventoryItem item)
    {
        if (Constants.itemsToPrevent.Contains(item.name) && item.description != Constants.GivenItemDescription)
        {
            Plugin.Instance.sendALternateUniqueLocation(item.name);
            return false;
        }
        ;

        return true;
    }
}


[HarmonyPatch(typeof(GameManager))]
[HarmonyPatch(nameof(GameManager.StartGame))]
class PatcherStartGame
{


    static void Postfix()
    {
        Plugin.Instance.atGameStart();
    }
}
