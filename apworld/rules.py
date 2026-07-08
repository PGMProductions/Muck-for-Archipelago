from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule, HasAny, HasFromList, True_, HasAllCounts

from .constants import POWERUPSLIST


if TYPE_CHECKING:
    from .world import MuckWorld
    



def HasNPowerups(n):
    return HasFromList(*POWERUPSLIST,count=n)

def HasNTools(n):
    return HasAllCounts({"Progressive Pickaxe" : n , "Progressive Axe" : n})

def HasNWeapons(n):
    return Has("Progressive Weapon", count = n) | Has("Progressive Bow", count = n)

def HasNArmor(n):
    return HasFromList("Progressive Helmet", "Progressive Chestplate","Progressive Leggings","Progressive Boots", count=n)


def canKillBosses(world):
    return HasNPowerups(5*world.options.logicDifficulty) & HasNWeapons(3*world.options.logicDifficulty) & HasNArmor(4*min(2*world.options.logicDifficulty,5))

def canKillFinalBoss(world):
    weaponsNeeded = 0
    if world.options.logicDifficulty == 3:
        weaponsNeeded = 10
    elif world.options.logicDifficulty == 2:
        weaponsNeeded = 8
    elif world.options.logicDifficulty == 1:
        weaponsNeeded = 6
    
    armorNeeded = 0
    if world.options.logicDifficulty == 3:
        armorNeeded = 20
    elif world.options.logicDifficulty == 2:
        armorNeeded = 18
    elif world.options.logicDifficulty == 1:
        armorNeeded = 15
    

    return HasNPowerups(10*world.options.logicDifficulty) & HasNWeapons(weaponsNeeded) & HasNArmor(armorNeeded)


def set_all_rules(world: MuckWorld) -> None:

    set_all_entrance_rules(world)
    set_completion_condition(world)


def set_all_location_rules(world: MuckWorld) -> None:
    pass


def set_all_entrance_rules(world: MuckWorld) -> None:
    
    totalPowerupsPerRegion = world.options.whitePerRegion + world.options.bluePerRegion + world.options.orangePerRegion
    powerupsRequiredPerRegion = totalPowerupsPerRegion//2
    
    
    for i in range(world.options.nbPowerupRegions):
        entrance = world.get_entrance(f"to Powerup Region {i+1}")
        rule: Rule = HasNPowerups(powerupsRequiredPerRegion*i) & HasNWeapons(i+1)
        
        world.set_rule(entrance,rule)
    
    
    woodTool = world.get_entrance("Wooden Tools")
    steelTool = world.get_entrance("Steel Tools")
    mithrilTool = world.get_entrance("Mithril Tools")
    adamantiteTool = world.get_entrance("Adamantite Tools")
    postBosses = world.get_entrance("Can Kill Bosses")
    
    world.set_rule(woodTool,HasNTools(1))
    world.set_rule(steelTool,HasNTools(2))
    world.set_rule(mithrilTool,HasNTools(3))
    world.set_rule(adamantiteTool,HasNTools(4))
    
    world.set_rule(postBosses,canKillBosses(world))
    
    

def set_completion_condition(world: APQuestWorld) -> None:
    HardRequirements = HasNTools(4)
    
    SoftRequirement = canKillFinalBoss(world)
    
    
    world.set_completion_rule(HardRequirements & SoftRequirement)
    
    
    
    
    
    
    