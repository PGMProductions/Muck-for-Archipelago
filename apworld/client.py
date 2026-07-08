from CommonClient import CommonContext as SuperContext, gui_enabled, ClientCommandProcessor, logger, get_base_parser, CommonContext, server_loop
import asyncio
import typing
import os

from tkinter import filedialog

from NetUtils import NetworkItem

from .constants import powerupsOffset,bluePowerupsOffset,orangePowerupsOffset,POWERUPSLIST,ID_TO_ITEM_NAME,ID_TO_LOCATION_NAME,LOCATION_NAME_TO_ID

MUCK_FOLDER_PATH = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Muck"

class MuckContext(CommonContext):
    tags = {"AP", "Online"}
    game = "Muck"
    command_processor = ClientCommandProcessor
    items_handling = 0b111
    
    allowLootAsLocations = None
    
    
    
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
    
    
    
    
    def on_package(self, cmd: str, args: dict[str, any]) -> None:
        if cmd == "Connected":
            self.allowLootAsLocations = args["slot_data"]["allowLootAsLocations"]


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
                    
                    
                    elif splitLine[0] == "_ Boots":
                        locations.append(LOCATION_NAME_TO_ID["Chunkium Boots"])
                    
                    else:
                        locations.append(LOCATION_NAME_TO_ID[splitLine[0]])
                        
                        
                        
            await ctx.check_locations(locations)
            
        except:
            pass
            
        
        locationDict = {"PowerupWhite" : 0,
                        "PowerupBlue" : 0,
                        "PowerupOrange" : 0,
                        
                        "Adamantite Pickaxe" : 0,
                        "Gold Pickaxe" : 0,
                        "Mithril Pickaxe" : 0,
                        "Steel Pickaxe" : 0,
                        "Wood Pickaxe" : 0,
                        "Oak Bow" : 0,
                        "Wood Bow" : 0,
                        "Birch bow" : 0,
                        "Fir bow" : 0,
                        "Ancient Bow" : 0,
                        "Adamantite Axe" : 0,
                        "Gold Axe" : 0,
                        "Mithril Axe" : 0,
                        "Steel Axe" : 0,
                        "Wood Axe" : 0,
                        "Adamantite Boots" : 0,
                        "Chunkium Boots" : 0,
                        "Gold Boots" : 0,
                        "Mithril Boots" : 0,
                        "Obamium Boots" : 0,
                        "Steel Boots" : 0,
                        "Wolfskin Boots" : 0,
                        "Adamantite Helmet" : 0,
                        "Chunkium Helmet" : 0,
                        "Gold Helmet" : 0,
                        "Mithril Helmet" : 0,
                        "Obamium Helmet" : 0,
                        "Steel Helmet" : 0,
                        "Wolfskin Helmet" : 0,
                        "Adamantite Pants" : 0,
                        "Chunkium Pants" : 0,
                        "Gold Pants" : 0,
                        "Mithril Pants" : 0,
                        "Obamium Pants" : 0,
                        "Steel Pants" : 0,
                        "Wolfskin Pants" : 0,
                        "Adamantite Chestplate" : 0,
                        "Chunkium Chestplate" : 0,
                        "Gold Chestplate" : 0,
                        "Mithril Chestplate" : 0,
                        "Obamium Chestplate" : 0,
                        "Steel Chestplate" : 0,
                        "Wolfskin Chestplate" : 0,
                        "Adamantite Sword" : 0,
                        "Gold Sword" : 0,
                        "Mithril Sword" : 0,
                        "Obamium Sword" : 0,
                        "Steel Sword" : 0,
                        "Chiefs Spear" : 0,
                        "Chunky Hammer" : 0,
                        "Gronks Sword" : 0,
                        "Night Blade" : 0,
                        "Wyvern Dagger" : 0,}
        
        
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
        

        for location in ctx.checked_locations:
            name = ID_TO_LOCATION_NAME[location]
            if name == "Chunkium Boots":
                name = "_ Boots"
            if not name.split(" ")[1] == "Powerup":
                locationDict[name] += 1
        
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
        except:
            pass
        
        
        receivedWeapons = min(receivedItems.count("Progressive Weapon"),10)
        receivedBows = min(receivedItems.count("Progressive Bow"),5)
        receivedAxes = min(receivedItems.count("Progressive Axe"),4)
        receivedPickaxes = min(receivedItems.count("Progressive Pickaxe"),4)
        
        receivedHelmets = min(receivedItems.count("Progressive Helmet"),5)
        receivedChestplates = min(receivedItems.count("Progressive Chestplate"),5)
        receivedLeggings = min(receivedItems.count("Progressive Leggings"),5)
        receivedboots = min(receivedItems.count("Progressive Boots"),5)
        
        
        try:
            with(open(MUCK_FOLDER_PATH + "\\ARCHIPELAGO_Tools.itmlst","w")) as f:
                f.write(f"""weapons,{receivedWeapons}
bows,{receivedBows}
axes,{receivedAxes}
pickaxes,{receivedPickaxes}
helmets,{receivedHelmets}
chestplates,{receivedChestplates}
leggings,{receivedLeggings}
boots,{receivedboots}""")
        except:
            pass
        
        
        await  asyncio.sleep(1)




async def other_loop(ctx: MuckContext):
    while not ctx.exit_event.is_set():

        try:
            with(open(MUCK_FOLDER_PATH + "\\victory","r")) as f:
                ctx.finished_game = True
            
            os.remove(MUCK_FOLDER_PATH + "\\victory")
            
            
        except:
            pass
        
        
        try:
            
            with(open(MUCK_FOLDER_PATH + "\\ARCHIPELAGO_Options.optlst","w")) as f:
                
                if ctx.allowLootAsLocations == 1:
                    f.write("allowLootAsLocations,1")
                else:
                    f.write("allowLootAsLocations,0")

        except:
            pass
    
        await  asyncio.sleep(3)
        






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
    
    global MUCK_FOLDER_PATH
    folderFound = False
    while not folderFound:
        try:
            with(open(MUCK_FOLDER_PATH + "\\ARCHIPELAGO_Powerups.itmlst","r") as f):
                folderFound = True 
        except:
            MUCK_FOLDER_PATH = filedialog.askdirectory(title="Choose Muck Folder")


    ctx = MuckContext(None, None)
    
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
    asyncio.create_task(locations_checker(ctx), name="MuckLocationsChecker")
    asyncio.create_task(items_checker(ctx),name="MuckItemsChecker")
    asyncio.create_task(other_loop(ctx),name="MuckAdditionalChecker")
    
    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()
    
    await ctx.exit_event.wait()
    await ctx.shutdown()



