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

    

def create_all_locations(world: APQuestWorld) -> None:
    create_powerups_locations(world)
    


def create_powerups_locations(world: MuckWorld) -> None:
    
    whitePerRegion = world.options.whitePerRegion
    bluePerRegion = world.options.bluePerRegion
    orangePerRegion = world.options.orangePerRegion
    
    for i in range(world.options.nbPowerupRegions):
        region = world.get_region(f"Powerups Region {i+1}")
        
        region.add_locations(get_location_names_with_ids([f"White Powerup {j+1}" for j in range(i*whitePerRegion,(i+1)*whitePerRegion)]),MuckLocation)
        region.add_locations(get_location_names_with_ids([f"Blue Powerup {j+1}" for j in range(i*bluePerRegion,(i+1)*bluePerRegion)]),MuckLocation)
        region.add_locations(get_location_names_with_ids([f"Orange Powerup {j+1}" for j in range(i*orangePerRegion,(i+1)*orangePerRegion)]),MuckLocation)
    
    
    
    
    
    
    
    
    
    
    
    