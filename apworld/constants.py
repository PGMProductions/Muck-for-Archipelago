from BaseClasses import ItemClassification

MAXPOWERUPREGIONS = 20

MAXWHITEPERREGION = 50
MAXBLUEPERREGION = 50
MAXORANGEPERREGION = 50

MAXWHITEPOWERUPLOCATIONS = MAXPOWERUPREGIONS*MAXWHITEPERREGION
MAXBLUEPOWERUPLOCATIONS = MAXPOWERUPREGIONS*MAXBLUEPERREGION
MAXORANGEPOWERUPLOCATIONS = MAXPOWERUPREGIONS*MAXORANGEPERREGION


MuckOffset = 68000

powerupsOffset = MuckOffset + 9000
bluePowerupsOffset = powerupsOffset + MAXWHITEPOWERUPLOCATIONS
orangePowerupsOffset = bluePowerupsOffset + MAXBLUEPOWERUPLOCATIONS

LOCATION_NAME_TO_ID = {}

for i in range(MAXWHITEPOWERUPLOCATIONS):
    LOCATION_NAME_TO_ID[f"White Powerup {i}"] = powerupsOffset + i
for i in range(MAXBLUEPOWERUPLOCATIONS):
    LOCATION_NAME_TO_ID[f"Blue Powerup {i}"] = bluePowerupsOffset + i
for i in range(MAXORANGEPOWERUPLOCATIONS):
    LOCATION_NAME_TO_ID[f"Orange Powerup {i}"] = orangePowerupsOffset + i
    
    
    
ITEM_NAME_TO_ID = {

"Broccoli" : 100,
"Dumbbell" : 101,
"Jetpack" : 102,
"Orange Juice" : 103,
"Peanut Butter" : 104,
"Blue Pill" : 105,
"Red Pill" : 106,
"Sneaker" : 107,
"Robin Hood Hat" : 108,
"Spooo Bean" : 109,
"Bulldozer" : 110,
"Horseshoe" : 111,
"Danis Milk" : 112,
"Piggybank" : 113,
"Crimson Dagger" : 114,
"Dracula" : 115,
"Janniks Frog" : 116,
"Juice" : 117,
"Adrenaline" : 118,
"Berserk" : 119,
"Checkered Shirt" : 120,
"Sniper Scope" : 121,
"Knuts Hammer" : 122,
"Wings of Glory" : 123,
"Enforcer" : 124
}

ID_TO_ITEM_NAME = {v:k for k,v in ITEM_NAME_TO_ID.items()}
ID_TO_LOCATION_NAME = {v:k for k,v in LOCATION_NAME_TO_ID.items()}

DEFAULT_ITEM_CLASSIFICATIONS = {
    
"Broccoli" : ItemClassification.filler | ItemClassification.progression_deprioritized,
"Dumbbell" : ItemClassification.filler | ItemClassification.progression_deprioritized,
"Jetpack" : ItemClassification.filler | ItemClassification.progression_deprioritized,
"Orange Juice" : ItemClassification.filler | ItemClassification.progression_deprioritized,
"Peanut Butter" : ItemClassification.filler | ItemClassification.progression_deprioritized,
"Blue Pill" : ItemClassification.filler | ItemClassification.progression_deprioritized,
"Red Pill" : ItemClassification.filler | ItemClassification.progression_deprioritized,
"Sneaker" : ItemClassification.filler | ItemClassification.progression_deprioritized,
"Robin Hood Hat" : ItemClassification.filler | ItemClassification.progression_deprioritized,
"Spooo Bean" : ItemClassification.filler | ItemClassification.progression_deprioritized,

"Bulldozer" : ItemClassification.filler | ItemClassification.progression_deprioritized,
"Horseshoe" : ItemClassification.filler | ItemClassification.progression_deprioritized,
"Danis Milk" : ItemClassification.filler | ItemClassification.progression_deprioritized,
"Piggybank" : ItemClassification.filler | ItemClassification.progression_deprioritized,
"Crimson Dagger" : ItemClassification.filler | ItemClassification.progression_deprioritized,
"Dracula" : ItemClassification.filler | ItemClassification.progression_deprioritized,
"Janniks Frog" : ItemClassification.filler | ItemClassification.progression_deprioritized,
"Juice" : ItemClassification.filler | ItemClassification.progression_deprioritized,

"Adrenaline" : ItemClassification.useful | ItemClassification.progression_deprioritized,
"Berserk" : ItemClassification.useful | ItemClassification.progression_deprioritized,
"Checkered Shirt" : ItemClassification.useful | ItemClassification.progression_deprioritized,
"Sniper Scope" : ItemClassification.useful | ItemClassification.progression_deprioritized,
"Knuts Hammer" : ItemClassification.useful | ItemClassification.progression_deprioritized,
"Wings of Glory" : ItemClassification.useful | ItemClassification.progression_deprioritized,
"Enforcer" : ItemClassification.useful | ItemClassification.progression_deprioritized

    }



WHITEPOWERUPSLIST = ("Broccoli","Dumbbell","Jetpack","Orange Juice","Peanut Butter","Blue Pill","Red Pill","Sneaker","Robin Hood Hat","Spooo Bean")
BLUEPOWERUPSLIST = ("Bulldozer","Horseshoe","Danis Milk","Piggybank","Crimson Dagger","Dracula","Janniks Frog","Juice")
ORANGEPOWERUPSLIST = ("Adrenaline","Berserk","Checkered Shirt","Sniper Scope","Knuts Hammer","Wings of Glory","Enforcer")

POWERUPSLIST = WHITEPOWERUPSLIST + BLUEPOWERUPSLIST + ORANGEPOWERUPSLIST





#("Broccoli","Dumbbell","Jetpack","Orange Juice","Peanut Butter","Blue Pill","Red Pill","Sneaker","Robin Hood Hat","Spooo Bean","Bulldozer","Horseshoe","Danis Milk","Piggybank","Crimson Dagger","Dracula","Janniks Frog","Juice","Adrenaline","Berserk","Checkered Shirt","Sniper Scope","Knuts Hammer","Wings of Glory","Enforcer")