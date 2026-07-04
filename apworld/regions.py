from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region


if TYPE_CHECKING:
    from .world import MuckWorld

def create_and_connect_regions(world: MuckWorld) -> None:
    create_all_regions(world)
    connect_regions(world)
    

def create_all_regions(world: MuckWorld) -> None:
    island = Region("Island", world.player, world.multiworld)
    
    
    regions = [island]
    
    
    for i in range(world.options.nbPowerupRegions):
        regions.append(Region(f"Powerups Region {i+1}", world.player, world.multiworld))
    
    
    world.multiworld.regions += regions
    
    
    
def connect_regions(world: MuckWorld) -> None:
    island = world.get_region("Island")
    
    lastRegion = island
    for i in range(world.options.nbPowerupRegions):
        newRegion = world.get_region(f"Powerups Region {i+1}")
        lastRegion.connect(newRegion,f"to Powerup Region {i+1}")
        lastRegion = newRegion

    
    
    
    
    
    
    
    