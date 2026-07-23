from BaseClasses import ItemClassification

MAXPOWERUPREGIONS = 20

MAXWHITEPERREGION = 50
MAXBLUEPERREGION = 50
MAXORANGEPERREGION = 50

MAXWHITEPOWERUPLOCATIONS = MAXPOWERUPREGIONS * MAXWHITEPERREGION
MAXBLUEPOWERUPLOCATIONS = MAXPOWERUPREGIONS * MAXBLUEPERREGION
MAXORANGEPOWERUPLOCATIONS = MAXPOWERUPREGIONS * MAXORANGEPERREGION


powerupsOffset = 9000
bluePowerupsOffset = MAXWHITEPOWERUPLOCATIONS + powerupsOffset
orangePowerupsOffset = MAXBLUEPOWERUPLOCATIONS + bluePowerupsOffset

LOCATION_NAME_TO_ID = {
"Gold Pickaxe" : 1,
"Mithril Pickaxe" : 2,
"Steel Pickaxe" : 3,
"Wood Pickaxe" : 4,
"Oak Bow" : 5,
"Wood Bow" : 6,
"Birch bow" : 7,
"Fir bow" : 8,
"Ancient Bow" : 9,
"Adamantite Axe" : 10,
"Gold Axe" : 11,
"Mithril Axe" : 12,
"Steel Axe" : 13,
"Wood Axe" : 14,
"Adamantite Boots" : 15,
"Chunkium Boots" : 16,
"Gold Boots" : 17,
"Mithril Boots" : 18,
"Obamium Boots" : 19,
"Steel Boots" : 20,
"Wolfskin Boots" : 21,
"Adamantite Helmet" : 22,
"Chunkium Helmet" : 23,
"Gold Helmet" : 24,
"Mithril Helmet" : 25,
"Obamium Helmet" : 26,
"Steel Helmet" : 27,
"Wolfskin Helmet" : 28,
"Adamantite Pants" : 29,
"Chunkium Pants" : 30,
"Gold Pants" : 31,
"Mithril Pants" : 32,
"Obamium Pants" : 33,
"Steel Pants" : 34,
"Wolfskin Pants" : 35,
"Adamantite Chestplate" : 36,
"Chunkium Chestplate" : 37,
"Gold Chestplate" : 38,
"Mithril Chestplate" : 39,
"Obamium Chestplate" : 40,
"Steel Chestplate" : 41,
"Wolfskin Chestplate" : 42,
"Adamantite Sword" : 43,
"Gold Sword" : 44,
"Mithril Sword" : 45,
"Obamium Sword" : 46,
"Steel Sword" : 47,
"Chiefs Spear" : 48,
"Chunky Hammer" : 49,
"Gronks Sword" : 50,
"Night Blade" : 51,
"Wyvern Dagger" : 52,
"Adamantite Pickaxe" : 53
}

for i in range(MAXWHITEPOWERUPLOCATIONS):
    LOCATION_NAME_TO_ID[f"White Powerup {i+1}"] = powerupsOffset + i
for i in range(MAXBLUEPOWERUPLOCATIONS):
    LOCATION_NAME_TO_ID[f"Blue Powerup {i+1}"] = bluePowerupsOffset + i
for i in range(MAXORANGEPOWERUPLOCATIONS):
    LOCATION_NAME_TO_ID[f"Orange Powerup {i+1}"] = orangePowerupsOffset + i



ITEM_NAME_TO_ID = {
"Progressive Weapon" : 1,
"Progressive Bow" : 2,
"Progressive Axe" : 3,
"Progressive Pickaxe" : 4,

"Progressive Helmet" : 5,
"Progressive Chestplate" : 6,
"Progressive Leggings" : 7,
"Progressive Boots" : 8,

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

