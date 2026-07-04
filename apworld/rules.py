from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule, HasAny, HasFromList, True_

from .constants import POWERUPSLIST


if TYPE_CHECKING:
    from .world import MuckWorld
    



def HasNPowerups(n):
    return HasFromList(*POWERUPSLIST,count=n)


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
        rule: Rule = HasNPowerups(powerupsRequiredPerRegion*i)
        
        world.set_rule(entrance,rule)
            

def set_completion_condition(world: APQuestWorld) -> None:
    totalPowerups = (world.options.whitePerRegion + world.options.bluePerRegion + world.options.orangePerRegion) * world.options.nbPowerupRegions
    world.set_completion_rule(HasNPowerups(10*world.options.logicDifficulty))