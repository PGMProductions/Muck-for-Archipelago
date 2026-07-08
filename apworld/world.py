from collections.abc import Mapping
from typing import Any

from . import items, locations, regions, rules

from . import options as muck_options

from worlds.AutoWorld import World

class MuckWorld(World):
    """
    Muck is a survival-roguelike about collecting resources and powerups during the day to survive the nights.
    Your goal is to repair a ship to leave the Muck island before the exponential difficulty destroys you, however, powerfull bosses will have to be fought for that
    To leave, you will have to face your arch nemesis : Bob
    """
    
    game = "Muck"

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID
    
    origin_region_name = "Island"

    options_dataclass = muck_options.MuckOptions
    options: muck_options.MuckOptions
    
    base_id = 68000

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.MuckItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
    
    def fill_slot_data(self):
        return self.options.as_dict("allowLootAsLocations")