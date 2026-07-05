from CommonClient import CommonContext as SuperContext, gui_enabled, ClientCommandProcessor, logger, get_base_parser, CommonContext, server_loop
import asyncio
import typing

from NetUtils import NetworkItem

from .constants import powerupsOffset,bluePowerupsOffset,orangePowerupsOffset,POWERUPSLIST,ID_TO_ITEM_NAME,ID_TO_LOCATION_NAME,LOCATION_NAME_TO_ID

MUCK_FOLDER_PATH = "C:\\Program Files (x86)\\Steam\\steamapps\\common\Muck"

class MuckContext(CommonContext):
    tags = {"AP", "Online"}
    game = "Muck"
    command_processor = ClientCommandProcessor
    items_handling = 0b111
    
    
    
    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.game = "Muck"
        
    
    
    def run_gui(self):
        from kvui import GameManager

        class MuckManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Muck Client"

        self.ui = MuckManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")
    
    
    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()



    async def connect(self, address: typing.Optional[str] = None):
        resetFilesStates()
        await super().connect(address)

    async def disconnect(self, allow_autoreconnect: bool = False):
        resetFilesStates()
        await super().disconnect(allow_autoreconnect)

    async def connection_closed(self):
        resetFilesStates()
        await super().connection_closed()

    async def shutdown(self):
        resetFilesStates()
        await super().shutdown()




async def locations_checker(ctx: MuckContext):
    while not ctx.exit_event.is_set():
        locations = []
        
        try:
            with open(MUCK_FOLDER_PATH + "\\ARCHIPELAGO_Locations.lctlst") as f:
                lines = f.readlines()
                
            locations = []
            
            for l in lines:
                splitLine = l.rstrip('\n').split(",")
                if int(splitLine[1]) > 0:
                    if splitLine[0] == "PowerupWhite":
                        for i in range(1,int(splitLine[1])+1):
                            locations.append(powerupsOffset + i)
                    elif splitLine[0] == "PowerupBlue":
                        for i in range(1,int(splitLine[1])+1):
                            locations.append(bluePowerupsOffset + i)
                    elif splitLine[0] == "PowerupOrange":
                        for i in range(1,int(splitLine[1])+1):
                            locations.append(orangePowerupsOffset + i)
                            
        else:
            await ctx.check_locations(locations)
            
        
        locationDict = {"PowerupWhite" : 0, "PowerupBlue" : 0, "PowerupOrange" : 0}
        
        
        #system for powerups
        i = 1
        while LOCATION_NAME_TO_ID[f"White Powerup {i}"] in ctx.checked_locations:
            i += 1
        locationDict["PowerupWhite"] = i-1
        
        i = 1
        while LOCATION_NAME_TO_ID[f"Blue Powerup {i}"] in ctx.checked_locations:
            i += 1
        locationDict["PowerupBlue"] = i-1
        
        i = 1
        while LOCATION_NAME_TO_ID[f"Orange Powerup {i}"] in ctx.checked_locations:
            i += 1
        locationDict["PowerupOrange"] = i-1
        
        
        
        #system for non-powerups (not used yet)
        """
        for location in ctx.checked_locations:
            name = ID_TO_LOCATION_NAME[location]
            if not name.split(" ")[1] == "Powerup":
                locationDict[name] += 1
                
        """
        
        setLocationsFile(locationDict)
                
        
        
        await asyncio.sleep(1)
        
        
async def items_checker(ctx: MuckContext):
    while not ctx.exit_event.is_set():
        receivedItems = list_received_items(ctx)
        
        powerupDict = {}
        for powerup in POWERUPSLIST:
            powerupDict[powerup] = receivedItems.count(powerup)
        try:
            with(open(MUCK_FOLDER_PATH + "\\ARCHIPELAGO_Powerups.itmlst","w")) as f:
                for name,quantity in powerupDict.items():
                    if name != POWERUPSLIST[0]:
                        f.write("\n")
                    f.write(f"{name},{quantity}")
        finally:
            pass
        
        
        await  asyncio.sleep(1)
        

def resetPowerupDict():
    with(open(MUCK_FOLDER_PATH + "\\ARCHIPELAGO_Powerups.itmlst","w")) as f:
        for powerup in POWERUPSLIST:
            if powerup != POWERUPSLIST[0]:
                f.write("\n")
            f.write(f"{powerup},0")
        

def setLocationsFile(locationDict = {"PowerupWhite" : 0, "PowerupBlue" : 0, "PowerupOrange" : 0}):
    with(open(MUCK_FOLDER_PATH + "\\ARCHIPELAGO_Locations.lctlst","w")) as f:
        for name,quantity in locationDict.items():
            if name != "PowerupWhite":
                f.write("\n")
            f.write(f"{name},{quantity}")


def resetFilesStates():
    resetPowerupDict()
    setLocationsFile()

def list_received_items(ctx: MuckContext):
    """returns a list of the names off all the items received (non unique)"""
    finalList = []
    for nItem in ctx.items_received:
        itemId = nItem.item
        name = ID_TO_ITEM_NAME[itemId]
        finalList.append(name)
    return finalList
        
        






    
async def startMuckClient(launch_args):
    ctx = MuckContext(None, None)
    
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
    asyncio.create_task(locations_checker(ctx), name="MuckLocationsChecker")
    asyncio.create_task(items_checker(ctx),name="MuckItemsChecker")
    
    
    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()
    
    await ctx.exit_event.wait()
    await ctx.shutdown()



