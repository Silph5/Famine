#Tos2Info.py
#contains any manually-added tos2 role information not accessible by the steamAPI
#also includes some getters to reduce the amount of redundant data

from enum import Enum

class Role(Enum):
    ADMIRER = 1
    AMNESIAC = 2
    BODYGUARD = 3
    CLERIC = 4
    CATALYST = 59
    CORONER = 5
    CRUSADER = 6
    DEPUTY = 7
    INVESTIGATOR = 8
    JAILOR = 9
    LOOKOUT = 10
    MARSHAL = 55
    MAYOR = 11
    MONARCH = 12
    ORACLE = 56
    PROSECUTOR = 13
    PSYCHIC = 14
    RETRIBUTIONIST = 15
    SEER = 16
    SHERIFF = 17
    SOCIALITE = 54
    SPY = 18
    TAVERNKEEPER = 19
    TRACKER = 20
    TRAPPER = 21
    TRICKSTER = 22
    VETERAN = 23
    VIGILANTE = 24
    CONJURER = 25
    ARCHMAGE = 26
    CULTIST = 60
    DREAMWEAVER = 27
    ENCHANTER = 28
    HEXMASTER = 39
    ILLUSIONIST = 40
    JINX = 31
    MEDUSA = 32
    NECROMANCER = 33
    POISONER = 34
    POTIONMASTER = 35
    RITUALIST = 36
    VOODOOMASTER = 37
    WILDLING = 38
    WITCH = 39
    ARSONIST = 40
    BAKER = 41
    BERSERKER = 42
    CURSEDSOUL = 53
    DOOMSAYER = 43
    EXECUTIONER = 44
    JESTER = 45
    PIRATE = 46
    PLAGUEBEARER = 47
    SERIALKILLER = 48
    SHROUD = 49
    SOULCOLLECTOR = 50
    WEREWOLF = 51
    VAMPIRE = 52


roleInfo = {
    "admirer": {
        "alignment": ("Town", "Support"),
        "id": 1,
        "hiddenDesc": "Have a Witch try to control a Bestowed player"
    },
    "amnesiac": {
        "alignment": ("Town", "Support"),
        "id": 2,
        "hiddenDesc": "Remember you were a Jailor"
    },
    "bodyguard": {
        "alignment": ("Town", "Protective"),
        "id": 3,
        "hiddenDesc": "Protect someone from War"
    },
    "cleric": {
        "alignment": ("Town", "Protective"),
        "id": 4,
        "hiddenDesc": "Protect a Bodyguard that successfully protected somebody"
    },
    "catalyst": {
        "alignment": ("Town", "Outlier"),
        "id": 59,
        #cata is missing its secret ach from the api due to improper naming, will fix later
    },
    "coroner": {
        "alignment": ("Town", "Investigative"),
        "id": 5,
        "hiddenDesc": "Find Pestilence"
    },
    "crusader": {
        "alignment": ("Town", "Protective"),
        "id": 6,
        "hiddenDesc": "Visit the same target as War and attack them"
    },
    "deputy": {
        "alignment": ("Town", "Killing"),
        "id": 7,
        "hiddenDesc": "Shoot a Conjurer"
    },
    "investigator": {
        "alignment": ("Town", "Investigative"),
        "id": 8,
        "hiddenDesc": "Find Trespassing 3 times in a game"
    },
    "jailor": {
        "alignment": ("Town", "Power"),
        "id": 9,
        "hiddenDesc": "Execute an Apocalypse god"
    },
    "lookout": {
        "alignment": ("Town", "Investigative"),
        "id": 10,
        "hiddenDesc": "Watch someone with no visitors die"
    },
    "marshal": {
        "alignment": ("Town", "Power"),
        "id": 55,
        "hiddenDesc": "Execute a Knighted evil player during a tribunal"
    },
    "mayor": {
        "alignment": ("Town", "Power"),
        "id": 11,
        "hiddenDesc": "Reveal after being Knighted"
    },
    "monarch": {
        "alignment": ("Town", "Power"),
        "id": 12,
        "hiddenDesc": "Knight yourself"
    },
    "oracle": {
        "alignment": ("Town", "Protective"),
        "id": 56,
        "hiddenDesc": "Successfully protect another Oracle"
    },
    "prosecutor": {
        "alignment": ("Town", "Power"),
        "id": 13,
        "hiddenDesc": "Prosecute a Horseman of the Apocalypse"
    },
    "psychic": {
        "alignment": ("Town", "Investigative"),
        "id": 14,
        "hiddenDesc": "Have no Vision due to insomnia"
    },
    "retributionist": {
        "alignment": ("Town", "Support"),
        "id": 15,
        "hiddenDesc": "Resurrect a Monarch and Knight yourself"
    },
    "seer": {
        "alignment": ("Town", "Investigative"),
        "id": 16,
        "hiddenDesc": "Find two Neutral Killing roles as enemies"
    },
    "sheriff": {
        "alignment": ("Town", "Investigative"),
        "id": 17,
        "hiddenDesc": "Find a Pirate to be suspicious"
    },
    "socialite": {
        "alignment": ("Town", "Support"),
        "id": 54,
        "hiddenDesc": "Throw a party with another Socialite"
    },
    "spy": {
        "alignment": ("Town", "Investigative"),
        "id": 18,
        "hiddenDesc": "See someone get their dreams invaded"
    },
    "tavernkeeper": {
        "alignment": ("Town", "Support"),
        "id": 19,
        "split": 6,
        "hiddenDesc": "Be jailed by the Jailor you previously roleblocked"
    },
    "tracker": {
        "alignment": ("Town", "Investigative"),
        "id": 20,
        "hiddenDesc": "Track yourself."
    },
    "trapper": {
        "alignment": ("Town", "Protective"),
        "id": 21,
        "hiddenDesc": "See War trigger your Trap"
    },
    "trickster": {
        "alignment": ("Town", "Killing"),
        "id": 22,
        "hiddenDesc": "Unleash a Werewolf rampage"
    },
    "veteran": {
        "alignment": ("Town", "Killing"),
        "id": 23,
        "hiddenDesc": "Attack War"
    },
    "vigilante": {
        "alignment": ("Town", "Killing"),
        "id": 24,
        "hiddenDesc": "Shoot yourself at night"
    },
    "conjurer": {
        "alignment": ("Coven", "Killing"),
        "id": 25,
        "hiddenDesc": "Kill an Admirer's found Obsession"
    },
    "archmage": {
        "alignment": ("Coven", "Power"),
        "id": 26,
        "hiddenDesc": "Retrain a Hex Master, Potion Master or Voodoo Master into eachother"
    },
    "cultist": {
        "alignment": ("Coven", "Outlier"),
        "id": 60,
        "hiddenDesc": "Convert a Vigilante who previously shot a member of your faction"
    },
    "dreamweaver": {
        "alignment": ("Coven", "Deception"),
        "id": 27,
        "hiddenDesc": "Give an unrevealed Mayor insomnia"
    },
    "enchanter": {
        "alignment": ("Coven", "Utility"),
        "id": 28,
        "hiddenDesc": "Forge a Coven member's last will"
    },
    "hexmaster": {
        "alignment": ("Coven", "Power"),
        "id": 29,
        "split": 3,
        "hiddenDesc": "Hex a player with a Crusader guarding them"
    },
    "illusionist": {
        "alignment": ("Coven", "Deception"),
        "id": 30,
        "hiddenDesc": "Illusion a Poisoner who is Smogging"
    },
    "jinx": {
        "alignment": ("Coven", "Killing"),
        "id": 31,
        "hiddenDesc": "Jinx a Werewolf"
    },
    "medusa": {
        "alignment": ("Coven", "Deception"),
        "id": 32,
        "hiddenDesc": "Stone a Serial Killer"
    },
    "necromancer": {
        "alignment": ("Coven", "Utility"),
        "id": 33,
        "hiddenDesc": "Reanimate War"
    },
    "poisoner": {
        "alignment": ("Coven", "Utility"),
        "id": 34,
        "hiddenDesc": "Have a player you Smogged at night die"
    },
    "potionmaster": {
        "alignment": ("Coven", "Utility"),
        "id": 35,
        "split": 6,
        "hiddenDesc": "Reveal a Vigilante the night they shoot you"
    },
    "ritualist": {
        "alignment": ("Coven", "Killing"),
        "id": 36,
        "hiddenDesc": "Perform a Blood Ritual on a Doomsayer"
    },
    "voodoomaster": {
        "alignment": ("Coven", "Utility"),
        "id": 37,
        "split": 6,
        "hiddenDesc": "Hang a Deafened player"
    },
    "wildling": {
        "alignment": ("Coven", "Utility"),
        "id": 38,
        "hiddenDesc": "See a Trickster absorb an attack"
    },
    "witch": {
        "alignment": ("Coven", "Power"),
        "id": 39,
        "hiddenDesc": "Control War, Horseman of the Apocalypse"
    },
    "arsonist": {
        "alignment": ("Neutral", "Killing"),
        "colour": "0xDB7601",
        "id": 40,
        "hiddenDesc": "Douse yourself"
    },
    "baker": {
        "alignment": ("Neutral", "Apocalypse"),
        "colour": "0xFE014E",
        "id": 41,
        "hiddenDesc": "Kill 5 players in one night from Famine"
    },
    "berserker": {
        "alignment": ("Neutral", "Apocalypse"),
        "colour": "0xFE014E",
        "id": 42,
        "hiddenDesc": "Kill a player protected by a Cleric"
    },
    "cursedsoul": {
        "alignment": ("Neutral", "Outlier"),
        "colour": "0xF5A563",
        "id": 53,
        "split": 6,
        "hiddenDesc": "Execute a Jailor whose role you stole"
    },
    "doomsayer": {
        "alignment": ("Neutral", "Evil"),
        "colour": "0x00CC99",
        "id": 43,
        "hiddenDesc": "Doom 3 players by night 3"
    },
    "executioner": {
        "alignment": ("Neutral", "Evil"),
        "colour": "0x949797",
        "id": 44,
        "hiddenDesc": "Hang a Deputy who successfully shot as your target"
    },
    "jester": {
        "alignment": ("Neutral", "Evil"),
        "colour": "0xF5A6D4",
        "id": 45,
        "hiddenDesc": "Free from Guilt"
    },
    "pirate": {
        "alignment": ("Neutral", "Evil"),
        "colour": "0xECC23E",
        "id": 46,
        "hiddenDesc": "Win the game without Plundering anyone"
    },
    "plaguebearer": {
        "alignment": ("Neutral", "Apocalypse"),
        "colour": "0xFE014E",
        "id": 47,
        "hiddenDesc": "Survive a Pirate trying to Plunder you"
    },
    "serialkiller": {
        "alignment": ("Neutral", "Killing"),
        "colour": "0x1D4DFC",
        "id": 48,
        "split": 6,
        "hiddenDesc": "Kill the Pirate who has you as a Landlubber"
    },
    "shroud": {
        "alignment": ("Neutral", "Killing"),
        "colour": "0x6699FF",
        "id": 49,
        "hiddenDesc": "Attack 2 players in one night"
    },
    "soulcollector": {
        "alignment": ("Neutral", "Apocalypse"),
        "colour": "0xFE014E",
        "id": 50,
        "split": 4,
        "hiddenDesc": "Survive a Conjurer nuke"
    },
    "werewolf": {
        "alignment": ("Neutral", "Killing"),
        "colour": "0x9D7038",
        "id": 51,
        "hiddenDesc": "Kill atleast one Town, Coven and Neutral in one night"
    },
    "vampire": {
        "alignment": ("Neutral", "Outlier"),
        "colour": "0xd90707",   
        "id": 52,
        "hiddenDesc": "Convert 3 Town Killing roles in one game"
    }
}

buckets = {
    "townpower": (
        "jailor",
        "marshal",
        "mayor",
        "monarch",
        "prosecutor",
    ),
    "townkilling": (
        "deputy",
        "trickster",
        "veteran",
        "vigilante"
    ),
    "townsupport": (
        "admirer",
        "amnesiac",
        "retributionist",
        "socialite",
        "tavernkeeper"
    ),
    "towninvestigative": (
        "coroner",
        "investigator",
        "lookout",
        "psychic",
        "seer",
        "sheriff",
        "spy",
        "tracker"
    ),
    "townprotective": (
        "bodyguard",
        "cleric",
        "crusader",
        "oracle",
        "trapper"
    ),
    "covenpower": (
        "archmage",
        "hexmaster",
        "witch",
    ),
    "covenkilling": (
        "conjurer",
        "jinx",
        "ritualist"
    ),
    "covendeception": (
        "dreamweaver",
        "enchanter",
        "illusionist",
        "medusa"
    ),
    "covenutility": (
        "necromancer",
        "poisoner",
        "potionmaster",
        "voodoomaster",
        "wildling"
    ),
    "neutralkilling": (
        "arsonist",
        "serialkiller",
        "shroud",
        "werewolf",
    ),
    "neutralevil": (
        "doomsayer",
        "executioner",
        "jester",
        "pirate",
    ),
    "neutralapocalypse": (
        "baker",
        "berserker",
        "plaguebearer",
        "soulcollector"
    ),
    "outliers": (
        "catalyst",
        "cultist",
        "vampire",
        "cursedsoul"
    )
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
        
def getRoleDisplayName(roleInternalName):
    displayName = roleInternalName[0].upper() + roleInternalName[1:]

    if not roleInternalName in roleInfo:
        return displayName;

    if not "split" in roleInfo[roleInternalName]:
        return displayName;

    splitPoint = roleInfo[roleInternalName]["split"]

    displayName = displayName[:splitPoint] + " " + displayName[splitPoint].upper() + displayName[splitPoint+1:]
    return displayName;

_roleAliases = {
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
    ("cl", "cov", "leader", "coven_leader", "coven", "arch", "mage", "am"): "archmage",
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
    alias: fullName for keys, fullName in _roleAliases.items() for alias in keys
}

_bucketAliases = {
    ("tpow", "pow", "town_power",): "townpower",
    ("tk", "town_killing", "townkiller"): "townkilling",
    ("ts", "town_support",): "townsupport",
    ("ti", "town_investigative", "towninv", "towninvest",): "towninvestigative",
    ("tp", "tplo", "town_protective",): "townprotective",
    ("cpow", "coven_power", "covpower",): "covenpower",
    ("ck", "coven_killing", "covkilling",): "covenkilling",
    ("cd", "covdeception", "coven_deception",): "covendeception",
    ("cu", "covutility", "coven_utility",): "covenutility",
    ("nk", "skarso", "neutral_killing", "neutralkiller",): "neutralkilling",
    ("ne", "neutral_evil",): "neutralevil",
    ("na", "neutral_apocalypse", "neutralapoc",): "neutralapocalypse",
    ("no", "to", "co", "townoutlier", "neutraloutlier", "covenoutlier", "town_outlier", "coven_outlier", "neutral_outlier", "outlier",): "outliers"
}

bucketAliasLookup = {
    alias: fullName for keys, fullName in _bucketAliases.items() for alias in keys
}