from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from .constants import MAXBLUEPOWERUPLOCATIONS,MAXORANGEPOWERUPLOCATIONS,MAXWHITEPOWERUPLOCATIONS,LOCATION_NAME_TO_ID



if TYPE_CHECKING:
    from .world import MuckWorld


class MuckLocation(Location):
    game = "Muck"
    




def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

    

def create_all_locations(world: MuckWorld) -> None:
    create_powerups_locations(world)
    create_items_locations(world)
    

def create_items_locations(world: MuckWorld) -> None:
    woodTier = world.get_region("Wood Tier")
    steelTier = world.get_region("Steel Tier")
    mithrilTier = world.get_region("Mithril Tier")
    adamantiteTier = world.get_region("Adamantite Tier")
    obamiumTier = world.get_region("Obamium Tier")
    
    postBosses = world.get_region("Post Bosses")
    
    if world.options.includeExoticArmors:
        woodTier.add_locations(get_location_names_with_ids(["Wolfskin Helmet","Wolfskin Pants","Wolfskin Boots","Wolfskin Chestplate"]))
        postBosses.add_locations(get_location_names_with_ids(["Chunkium Helmet","Chunkium Pants","Chunkium Boots","Chunkium Chestplate"]))
    
    if world.options.includeLegendaryWeapons:
        adamantiteTier.add_locations(get_location_names_with_ids(["Wyvern Dagger"]))
        obamiumTier.add_locations(get_location_names_with_ids(["Chiefs Spear","Gronks Sword","Night Blade"]))
        postBosses.add_locations(get_location_names_with_ids(["Chunky Hammer","Ancient Bow"]))
    
    
    
    woodTier.add_locations(get_location_names_with_ids(["Wood Pickaxe","Wood Axe","Wood Bow"]))
    steelTier.add_locations(get_location_names_with_ids(["Steel Pickaxe","Steel Axe","Steel Helmet","Steel Pants","Steel Boots","Steel Chestplate","Steel Sword","Gold Pickaxe","Gold Axe","Gold Helmet","Gold Pants","Gold Boots","Gold Chestplate","Gold Sword","Birch bow"]))
    mithrilTier.add_locations(get_location_names_with_ids(["Mithril Pickaxe","Mithril Axe","Mithril Helmet","Mithril Pants","Mithril Boots","Mithril Chestplate","Mithril Sword","Fir bow"]))
    adamantiteTier.add_locations(get_location_names_with_ids(["Adamantite Pickaxe","Adamantite Axe","Adamantite Helmet","Adamantite Pants","Adamantite Boots","Adamantite Chestplate","Adamantite Sword","Oak Bow"]))
    obamiumTier.add_locations(get_location_names_with_ids(["Obamium Helmet","Obamium Pants","Obamium Boots","Obamium Chestplate","Obamium Sword"]))


def create_powerups_locations(world: MuckWorld) -> None:
    
    whitePerRegion = world.options.whitePerRegion
    bluePerRegion = world.options.bluePerRegion
    orangePerRegion = world.options.orangePerRegion
    
    for i in range(world.options.nbPowerupRegions):
        region = world.get_region(f"Powerups Region {i+1}")
        
        region.add_locations(get_location_names_with_ids([f"White Powerup {j+1}" for j in range(i*whitePerRegion,(i+1)*whitePerRegion)]),MuckLocation)
        region.add_locations(get_location_names_with_ids([f"Blue Powerup {j+1}" for j in range(i*bluePerRegion,(i+1)*bluePerRegion)]),MuckLocation)
        region.add_locations(get_location_names_with_ids([f"Orange Powerup {j+1}" for j in range(i*orangePerRegion,(i+1)*orangePerRegion)]),MuckLocation)
    
    
    
    
    
    
    
    
    
    
    
    
    