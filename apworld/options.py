from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

from .constants import MAXPOWERUPREGIONS,MAXWHITEPERREGION,MAXBLUEPERREGION,MAXORANGEPERREGION

class NumberOfPowerupsRegions(Range):
    """
    How many regions to create in logic and put powerups pickup locations into
    The logic uses multiple regions in order to force late powerups locations (example, White Powerup 87) to be in later spheres (so that one of your friends doesn't need it to enter their sphere 2 for example)
    Higher values means that it's less likely for powerups locations you will get pretty late to contain items needed earlier
    """
    display_name = "Number Of Powerup Logic Region"
    range_start = 1
    range_end = MAXPOWERUPREGIONS

    default = 4

class NumberWhitePowerupsPerRegion(Range):
    """
    How many white powerup pickup location to put in each region
    Note that the total ammount of white powerups you will need to pickup to get the whole location pool is Number Of Regions * Number Of Location Per Region
    White powerup locations picked up after that won't give you anything
    """
    display_name = "Number Of White Powerup Location Per Region"
    range_start = 1
    range_end = MAXWHITEPERREGION
    
    default = 10
    
class NumberBluePowerupsPerRegion(Range):
    """
    Same as above but for the blue powerup locations
    """
    display_name = "Number Of Blue Powerup Location Per Region"
    range_start = 1
    range_end = MAXBLUEPERREGION
    
    default = 5

class NumberOrangePowerupsPerRegion(Range):
    """
    Same as above but for the orange powerup locations
    """
    display_name = "Number Of Orange Powerup Location Per Region"
    range_start = 1
    range_end = MAXORANGEPERREGION
    
    default = 2
    

class WhiteItemWeight(Range):
    """
    When you receive a powerup item, the weight of this powerup being white
    """
    display_name = "White Powerup Item Weight"
    range_start = 0
    range_end = 50
    
    default = 5

class BlueItemWeight(Range):
    """
    When you receive a powerup item, the weight of this powerup being blue
    """
    display_name = "Blue Powerup Item Weight"
    range_start = 0
    range_end = 50
    
    default = 3

class OrangeItemWeight(Range):
    """
    When you receive a powerup item, the weight of this powerup being orange
    """
    display_name = "Orange Powerup Item Weight"
    range_start = 0
    range_end = 50
    
    default = 1



class Difficulty(Choice):
    """
    Only used in logic to determine how many powerups/weapons/armors you need to defeat bosses
    Will cause generation errors when using a low difficulty and a small item pool
    
    Easy will wait until you have a LOT of powerups and weapons before saying you can fight bosses
    None will assume you can beat everything with nothing but a rock
    Normal and Hard are in-betweens
    
    It is NOT recommended to play with None
    """
    display_name = "Logic Difficulty"

    option_easy = 3
    option_normal = 2
    option_hard = 1
    option_none = 0
    
    default = option_normal


class IncludeExoticArmors(Toggle):
    """
    Wether to add crafting Wolfskin armor and Chunkium armor as locations
    """
    display_name = "Include Exotic Armors"


class IncludeLegendaryWeapons(Toggle):
    """
    Wether to add crafting legendary weapons as locations
    These are the Wyvern Dagger, Gronk's Sword, Chunky Hammer, Night Blade, Chiefs Spear and Ancient Bow
    """
    display_name = "Include Legendary Weapons"



class AllowLootAsLocations(Toggle):
    """
    Allows you to get the locations for crafting tools/weapons/armors by obtaining them through other means
    (Looting chests, buying from woodmen...)
    """
    display_name = "Allow Looting Locations" 
    
    
@dataclass
class MuckOptions(PerGameCommonOptions):
    whitePowerupItemWeight: WhiteItemWeight
    bluePowerupItemWeight: BlueItemWeight
    orangePowerupItemWeight: OrangeItemWeight
    
    nbPowerupRegions: NumberOfPowerupsRegions
    whitePerRegion: NumberWhitePowerupsPerRegion
    bluePerRegion: NumberBluePowerupsPerRegion
    orangePerRegion: NumberOrangePowerupsPerRegion
    
    includeExoticArmors:IncludeExoticArmors
    includeLegendaryWeapons:IncludeLegendaryWeapons
    allowLootAsLocations: AllowLootAsLocations
    
    logicDifficulty: Difficulty
    


option_groups = [
    OptionGroup(
        "Game Options",
        [Difficulty],
    ),
    OptionGroup(
        "Powerup Items Options",
        [WhiteItemWeight,BlueItemWeight,OrangeItemWeight],
    ),
    OptionGroup(
        "Locations Options",
        [IncludeExoticArmors,IncludeLegendaryWeapons],
    ),
    OptionGroup(
        "Powerup Locations Options",
        [NumberOfPowerupsRegions,NumberWhitePowerupsPerRegion,NumberBluePowerupsPerRegion,NumberOrangePowerupsPerRegion],
    ),
    OptionGroup(
        "Gameplay Options",
        [AllowLootAsLocations],
    ),
]

    
    
    
    
    
    
    