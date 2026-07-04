from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item , ItemClassification

from .constants import DEFAULT_ITEM_CLASSIFICATIONS,ITEM_NAME_TO_ID,WHITEPOWERUPSLIST,BLUEPOWERUPSLIST,ORANGEPOWERUPSLIST

if TYPE_CHECKING:
    from .world import MuckWorld





class MuckItem(Item):
    game = "Muck"



def get_random_filler_item_name(world: APQuestWorld) -> str:
    
    whiteWeight = world.options.whitePowerupItemWeight
    blueWeight = world.options.bluePowerupItemWeight
    orangeWeight = world.options.orangePowerupItemWeight
    
    totalWeight = whiteWeight+blueWeight+orangeWeight
    
    random = world.random.randint(1, totalWeight)
    
    if random <= whiteWeight:
        return WHITEPOWERUPSLIST[world.random.randint(0, len(WHITEPOWERUPSLIST)-1)]
    
    elif random <= whiteWeight+blueWeight:
        return BLUEPOWERUPSLIST[world.random.randint(0, len(BLUEPOWERUPSLIST)-1)]
    
    else:
        return ORANGEPOWERUPSLIST[world.random.randint(0, len(ORANGEPOWERUPSLIST)-1)]
    




def create_item_with_correct_classification(world: APQuestWorld, name: str) -> APQuestItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return MuckItem(name, classification, ITEM_NAME_TO_ID[name], world.player)



def create_all_items(world: MuckWorld) -> None:
    itempool: list[Item] = []
    
    #add here when there'll be non-filler items
    
    number_of_items = len(itempool)
    
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    
    world.multiworld.itempool += itempool



