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

LOCATION_NAME_TO_ID = {
"Adamantite Pickaxe" : MuckOffset + 0,
"Gold Pickaxe" : MuckOffset + 1,
"Mithril Pickaxe" : MuckOffset + 2,
"Steel Pickaxe" : MuckOffset + 3,
"Wood Pickaxe" : MuckOffset + 4,
"Oak Bow" : MuckOffset + 5,
"Wood Bow" : MuckOffset + 6,
"Birch bow" : MuckOffset + 7,
"Fir bow" : MuckOffset + 8,
"Ancient Bow" : MuckOffset + 9,
"Adamantite Axe" : MuckOffset + 10,
"Gold Axe" : MuckOffset + 11,
"Mithril Axe" : MuckOffset + 12,
"Steel Axe" : MuckOffset + 13,
"Wood Axe" : MuckOffset + 14,
"Adamantite Boots" : MuckOffset + 15,
"Chunkium Boots" : MuckOffset + 16,
"Gold Boots" : MuckOffset + 17,
"Mithril Boots" : MuckOffset + 18,
"Obamium Boots" : MuckOffset + 19,
"Steel Boots" : MuckOffset + 20,
"Wolfskin Boots" : MuckOffset + 21,
"Adamantite Helmet" : MuckOffset + 22,
"Chunkium Helmet" : MuckOffset + 23,
"Gold Helmet" : MuckOffset + 24,
"Mithril Helmet" : MuckOffset + 25,
"Obamium Helmet" : MuckOffset + 26,
"Steel Helmet" : MuckOffset + 27,
"Wolfskin Helmet" : MuckOffset + 28,
"Adamantite Pants" : MuckOffset + 29,
"Chunkium Pants" : MuckOffset + 30,
"Gold Pants" : MuckOffset + 31,
"Mithril Pants" : MuckOffset + 32,
"Obamium Pants" : MuckOffset + 33,
"Steel Pants" : MuckOffset + 34,
"Wolfskin Pants" : MuckOffset + 35,
"Adamantite Chestplate" : MuckOffset + 36,
"Chunkium Chestplate" : MuckOffset + 37,
"Gold Chestplate" : MuckOffset + 38,
"Mithril Chestplate" : MuckOffset + 39,
"Obamium Chestplate" : MuckOffset + 40,
"Steel Chestplate" : MuckOffset + 41,
"Wolfskin Chestplate" : MuckOffset + 42,
"Adamantite Sword" : MuckOffset + 43,
"Gold Sword" : MuckOffset + 44,
"Mithril Sword" : MuckOffset + 45,
"Obamium Sword" : MuckOffset + 46,
"Steel Sword" : MuckOffset + 47,
"Chiefs Spear" : MuckOffset + 48,
"Chunky Hammer" : MuckOffset + 49,
"Gronks Sword" : MuckOffset + 50,
"Night Blade" : MuckOffset + 51,
"Wyvern Dagger" : MuckOffset + 52
}

for i in range(MAXWHITEPOWERUPLOCATIONS):
    LOCATION_NAME_TO_ID[f"White Powerup {i}"] = powerupsOffset + i
for i in range(MAXBLUEPOWERUPLOCATIONS):
    LOCATION_NAME_TO_ID[f"Blue Powerup {i}"] = bluePowerupsOffset + i
for i in range(MAXORANGEPOWERUPLOCATIONS):
    LOCATION_NAME_TO_ID[f"Orange Powerup {i}"] = orangePowerupsOffset + i
    
    
    
ITEM_NAME_TO_ID = {
"Progressive Weapon" : 0,
"Progressive Bow" : 1,
"Progressive Axe" : 2,
"Progressive Pickaxe" : 3,

"Progressive Helmet" : 4,
"Progressive Chestplate" : 5,
"Progressive Leggings" : 6,
"Progressive Boots" : 7,

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
    
"Progressive Weapon" : ItemClassification.progression,
"Progressive Bow" : ItemClassification.progression,
"Progressive Axe" : ItemClassification.progression,
"Progressive Pickaxe" : ItemClassification.progression,

"Progressive Helmet" : ItemClassification.progression,
"Progressive Chestplate" : ItemClassification.progression,
"Progressive Leggings" : ItemClassification.progression,
"Progressive Boots" : ItemClassification.progression,
    
    
    
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

