#Tos2Info.py
#contains any manually-added tos2 role information not accessible by the steamAPI
#also includes some getters to reduce the amount of redundant data

roleInfo = {
    "admirer": {
        "alignment": ["Town", "Support"],
        "id": 1
    },
    "amnesiac": {
        "alignment": ["Town", "Support"],
        "id": 2
    },
    "bodyguard": {
        "alignment": ["Town", "Protective"],
        "id": 3
    },
    "cleric": {
        "alignment": ["Town", "Protective"],
        "id": 4
    },
    "catalyst": {
        "alignment": ["Town", "Outlier"],
        "id": 59
    },
    "coroner": {
        "alignment": ["Town", "Investigative"],
        "id": 5
    },
    "crusader": {
        "alignment": ["Town", "Protective"],
        "id": 6
    },
    "deputy": {
        "alignment": ["Town", "Killing"],
        "id": 7
    },
    "investigator": {
        "alignment": ["Town", "Investigative"],
        "id": 8
    },
    "jailor": {
        "alignment": ["Town", "Power"],
        "id": 9
    },
    "lookout": {
        "alignment": ["Town", "Investigative"],
        "id": 10
    },
    "marshal": {
        "alignment": ["Town", "Power"],
        "id": 55
    },
    "mayor": {
        "alignment": ["Town", "Power"],
        "id": 11
    },
    "monarch": {
        "alignment": ["Town", "Power"],
        "id": 12
    },
    "oracle": {
        "alignment": ["Town", "Protective"],
        "id": 56
    },
    "prosecutor": {
        "alignment": ["Town", "Power"],
        "id": 13
    },
    "psychic": {
        "alignment": ["Town", "Investigative"],
        "id": 14
    },
    "retributionist": {
        "alignment": ["Town", "Support"],
        "id": 15
    },
    "seer": {
        "alignment": ["Town", "Investigative"],
        "id": 16
    },
    "sheriff": {
        "alignment": ["Town", "Investigative"],
        "id": 17
    },
    "socialite": {
        "alignment": ["Town", "Support"],
        "id": 54
    },
    "spy": {
        "alignment": ["Town", "Investigative"],
        "id": 18
    },
    "tavernkeeper": {
        "alignment": ["Town", "Support"],
        "id": 19
    },
    "tracker": {
        "alignment": ["Town", "Investigative"],
        "id": 20
    },
    "trapper": {
        "alignment": ["Town", "Protective"],
        "id": 21
    },
    "trickster": {
        "alignment": ["Town", "Killing"],
        "id": 22
    },
    "veteran": {
        "alignment": ["Town", "Killing"],
        "id": 23
    },
    "vigilante": {
        "alignment": ["Town", "Killing"],
        "id": 24
    },
    "conjurer": {
        "alignment": ["Coven", "Killing"],
        "id": 25
    },
    "covenleader": {
        "alignment": ["Coven", "Power"],
        "id": 26
    },
    "cultist": {
        "alignment": ["Coven", "Outlier"],
        "id": 60
    },
    "dreamweaver": {
        "alignment": ["Coven", "Deception"],
        "id": 27
    },
    "enchanter": {
        "alignment": ["Coven", "Utility"],
        "id": 28
    },
    "hexmaster": {
        "alignment": ["Coven", "Power"],
        "id": 29
    },
    "illusionist": {
        "alignment": ["Coven", "Deception"],
        "id": 30
    },
    "jinx": {
        "alignment": ["Coven", "Killing"],
        "id": 31
    },
    "medusa": {
        "alignment": ["Coven", "Deception"],
        "id": 32
    },
    "necromancer": {
        "alignment": ["Coven", "Utility"],
        "id": 33
    },
    "poisoner": {
        "alignment": ["Coven", "Utility"],
        "id": 34
    },
    "potionmaster": {
        "alignment": ["Coven", "Utility"],
        "id": 35
    },
    "ritualist": {
        "alignment": ["Coven", "Killing"],
        "id": 36
    },
    "voodoomaster": {
        "alignment": ["Coven", "Utility"],
        "id": 37
    },
    "wildling": {
        "alignment": ["Coven", "Utility"],
        "id": 38
    },
    "witch": {
        "alignment": ["Coven", "Power"],
        "id": 39
    },
    "arsonist": {
        "alignment": ["Neutral", "Killing"],
        "colour": "0xDB7601",
        "id": 40
    },
    "baker": {
        "alignment": ["Neutral", "Apocalypse"],
        "colour": "0xFE014E",
        "id": 41
    },
    "berserker": {
        "alignment": ["Neutral", "Apocalypse"],
        "colour": "0xFE014E",
        "id": 42
    },
    "cursedsoul": {
        "alignment": ["Neutral", "Outlier"],
        "colour": "0xF5A563",
        "id": 53
    },
    "doomsayer": {
        "alignment": ["Neutral", "Evil"],
        "colour": "0x00CC99",
        "id": 43
    },
    "executioner": {
        "alignment": ["Neutral", "Evil"],
        "colour": "0x949797",
        "id": 44
    },
    "jester": {
        "alignment": ["Neutral", "Evil"],
        "colour": "0xF5A6D4",
        "id": 45
    },
    "pirate": {
        "alignment": ["Neutral", "Evil"],
        "colour": "0xECC23E",
        "id": 46
    },
    "plaguebearer": {
        "alignment": ["Neutral", "Apocalypse"],
        "colour": "0xFE014E",
        "id": 47
    },
    "serialkiller": {
        "alignment": ["Neutral", "Killing"],
        "colour": "0x1D4DFC",
        "id": 48
    },
    "shroud": {
        "alignment": ["Neutral", "Killing"],
        "colour": "0x6699FF",
        "id": 49
    },
    "soulcollector": {
        "alignment": ["Neutral", "Apocalypse"],
        "colour": "0xFE014E",
        "id": 50
    },
    "werewolf": {
        "alignment": ["Neutral", "Killing"],
        "colour": "0x9D7038",
        "id": 51
    },
    "vampire": {
        "alignment": ["Neutral", "Outlier"],
        "colour": "0xd90707",   
        "id": 52
    }
}

buckets = {
    "townpower": [
        "jailor",
        "marshal",
        "mayor",
        "monarch",
        "prosecutor",
        "catalyst"
    ],
    "townkilling": [
        "deputy",
        "trickster",
        "veteran",
        "vigilante"
    ],
    "townsupport": [
        "admirer",
        "amnesiac",
        "retributionist",
        "socialite",
        "tavernkeeper"
    ],
    "towninvestigative": [
        "coroner",
        "investigator",
        "lookout",
        "psychic",
        "seer",
        "sheriff",
        "spy",
        "tracker"
    ],
    "townprotective": [
        "bodyguard",
        "cleric",
        "crusader",
        "oracle",
        "trapper"
    ],
    "covenpower": [
        "covenleader",
        "hexmaster",
        "witch",
        "cultist"
    ],
    "covenkilling": [
        "conjurer",
        "jinx",
        "ritualist"
    ],
    "covendeception": [
        "dreamweaver",
        "enchanter",
        "illusionist",
        "medusa"
    ],
    "covenutility": [
        "necromancer",
        "poisoner",
        "potionmaster",
        "voodoomaster",
        "wildling"
    ],
    "neutralkilling": [
        "arsonist",
        "serialkiller",
        "shroud",
        "werewolf",
        "vampire"
    ],
    "neutralevil": [
        "doomsayer",
        "executioner",
        "jester",
        "pirate",
        "cursedsoul"
    ],
    "neutralapocalypse": [
        "baker",
        "berserker",
        "plaguebearer",
        "soulcollector"
    ]
}

factionIDs = {
    "town": 1, 
    "coven": 2, 
    "serialkiller": 3, 
    "arsonist": 4, 
    "werewolf": 5, 
    "shroud": 6, 
    "apocalypse": 7, 
    "executioner": 8, 
    "jester": 9, 
    "pirate": 10, 
    "doomsayer": 11, 
    "vampire": 12, 
    "cursedsoul": 13,
}


def getRoleColour(roleName):
    try:
        match roleInfo[roleName]["alignment"][0]:
            case "Town":
                return int("0x66BF58", 16)
            case "Coven":
                return int("0xA331EF", 16)
            case "Neutral":
                return int(roleInfo[roleName]["colour"], 16)
    except: 
        return int("0xFFD700", 16)
    
def getFactionColour(factionName):
    
    match factionName:
        case "town":
            return int("0x66BF58", 16)
        case "coven":
            return int("0xA331EF", 16)
        case "apocalypse":
            return int ("0xFE014E", 16)
        case _:
            return int(roleInfo[factionName]["colour"], 16)

roleAliases = {
    ("adm", "admi"): "admirer",
    ("amne",): "amnesiac",
    ("bg", "body"): "bodyguard",
    ("cler",): "cleric",
    ("cata",): "catalyst",
    ("coro",): "coroner",
    ("crus",): "crusader",
    ("dep",): "deputy",
    ("inv", "invest"): "investigator",
    ("jail",): "jailor",
    ("lo",): "lookout",
    ("marsh",): "marshal",
    ("mayo", "pilgrim", "mayore"): "mayor",
    ("mon",): "monarch",
    ("ora", "orac"): "oracle",
    ("pros",): "prosecutor",
    ("psy",): "psychic",
    ("ret", "retri"): "retributionist",
    ("sher",): "sheriff",
    ("soc", "soci"): "socialite",
    ("tav", "tavern_keeper", "tavern"): "tavernkeeper",
    ("track",): "tracker",
    ("trap",): "trapper",
    ("trick",): "trickster",
    ("vet",): "veteran",
    ("vig", "vigi"): "vigilante",
    ("conj",): "conjurer",
    ("cl", "cov", "leader", "coven_leader", "coven"): "covenleader",
    ("cult",): "cultist",
    ("dw", "dream"): "dreamweaver",
    ("ench",): "enchanter",
    ("hex", "hm", "hex_master"): "hexmaster",
    ("illu",): "illusionist",
    ("med", "medu"): "medusa",
    ("nec", "necro"): "necromancer",
    ("pois",): "poisoner",
    ("pm", "potion", "potion_master"): "potionmaster",
    ("rit",): "ritualist",
    ("vm", "voodoo", "voodoo_master"): "voodoomaster",
    ("wild",): "wildling",
    ("ars", "arso"): "arsonist",
    ("famine", "fam"): "baker",
    ("war", "bers"): "berserker",
    ("cs", "wanderingsoul", "cursed", "cursed_soul", "wandering_soul"): "cursedsoul",
    ("doom",): "doomsayer",
    ("exe", "exec"): "executioner",
    ("jest", "clown"): "jester",
    ("pir",): "pirate",
    ("plague", "pb", "pest", "pestilence"): "plaguebearer",
    ("sk", "serial_killer", "serial"): "serialkiller",
    ("shrond",): "shroud",
    ("sc", "soul", "death", "soul_collector"): "soulcollector",
    ("ww", "were"): "werewolf",
    ("vamp",): "vampire"
}

aliasLookup = {
    alias: fullName for keys, fullName in roleAliases.items() for alias in keys
}