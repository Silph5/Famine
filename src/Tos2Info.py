#Tos2Info.py
#contains any manually-added tos2 role information not accessible by the steamAPI
#also includes some getters to reduce the amount of redundant data

roleInfo = {
    "admirer":{
        "alignment":["Town", "Support"],
    },
    "amnesiac": {
        "alignment": ["Town", "Support"]
    },
    "bodyguard": {
        "alignment": ["Town", "Protective"]
    },
    "cleric": {
        "alignment": ["Town", "Protective"]
    },
    "catalyst": {
        "alignment": ["Town", "Outlier"]
    },
    "coroner": {
        "alignment": ["Town", "Investigative"]
    },
    "crusader": {
        "alignment": ["Town", "Protective"]
    },
    "deputy": {
        "alignment": ["Town", "Killing"]
    },
    "investigator": {
        "alignment": ["Town", "Investigative"]
    },
    "jailor": {
        "alignment": ["Town", "Power"]
    },
    "lookout": {
        "alignment": ["Town", "Investigative"]
    },
    "marshal": {
        "alignment": ["Town", "Power"]
    },
    "mayor": {
        "alignment": ["Town", "Power"]
    },
    "monarch": {
        "alignment": ["Town", "Power"]
    },
    "oracle": {
        "alignment": ["Town", "Protective"]
    },
    "prosecutor": {
        "alignment": ["Town", "Power"]
    },
    "psychic": {
        "alignment": ["Town", "Investigative"]
    },
    "retributionist": {
        "alignment": ["Town", "Support"]
    },
    "seer": {
        "alignment": ["Town", "Investigative"]
    },
    "sheriff": {
        "alignment": ["Town", "Investigative"]
    },
    "socialite": {
        "alignment": ["Town", "Support"]
    },
    "spy": {
        "alignment": ["Town", "Investigative"]
    },
    "tavernkeeper": {
        "alignment": ["Town", "Support"]
    },
    "tracker": {
        "alignment": ["Town", "Investigative"]
    },
    "trapper": {
        "alignment": ["Town", "Protective"]
    },
    "trickster": {
        "alignment": ["Town", "Killing"]
    },
    "veteran": {
        "alignment": ["Town", "Killing"]
    },
    "vigilante": {
        "alignment": ["Town", "Killing"]
    },
    "conjurer": {
        "alignment": ["Coven", "Killing"]
    },
    "covenleader": {
        "alignment": ["Coven", "Power"]
    },
    "cultist": {
        "alignment": ["Coven", "Outlier"]
    },
    "dreamweaver": {
        "alignment": ["Coven", "Deception"]
    },
    "enchanter": {
        "alignment": ["Coven", "Utility"]
    },
    "hexmaster": {
        "alignment": ["Coven", "Power"]
    },
    "illusionist": {
        "alignment": ["Coven", "Deception"]
    },
    "jinx": {
        "alignment": ["Coven", "Killing"]
    },
    "medusa": {
        "alignment": ["Coven", "Deception"]
    },
    "necromancer": {
        "alignment": ["Coven", "Utility"]
    },
    "poisoner": {
        "alignment": ["Coven", "Utility"]
    },
    "potionmaster": {
        "alignment": ["Coven", "Utility"]
    },
    "ritualist": {
        "alignment": ["Coven", "Killing"]
    },
    "voodoomaster": {
        "alignment": ["Coven", "Utility"]
    },
    "wildling": {
        "alignment": ["Coven", "Utility"]
    },
    "witch": {
        "alignment": ["Coven", "Power"]
    },
    "arsonist": {
        "alignment": ["Neutral", "Killing"],
        "colour": "0xDB7601"
    },
    "baker": {
        "alignment": ["Neutral", "Apocalypse"],
        "colour": "0xFE014E"
    },
    "berserker": {
        "alignment": ["Neutral", "Apocalypse"],
        "colour": "0xFE014E"
    },
    "cursedsoul": {
        "alignment": ["Neutral", "Outlier"],
        "colour": "0xf5a563"
    },
    "doomsayer": {
        "alignment": ["Neutral", "Evil"],
        "colour": "0x00CC99"
    },
    "executioner": {
        "alignment": ["Neutral", "Evil"],
        "colour": "0x949797"
    },
    "jester": {
        "alignment": ["Neutral", "Evil"],
        "colour": "0xF5A6D4"
    },
    "pirate": {
        "alignment": ["Neutral", "Evil"],
        "colour": "0xECC23E"
    },
    "plaguebearer": {
        "alignment": ["Neutral", "Apocalypse"],
        "colour": "0xFE014E"
    },
    "serialkiller": {
        "alignment": ["Neutral", "Killing"],
        "colour": "0x1D4DFC"
    },
    "shroud": {
        "alignment": ["Neutral", "Killing"],
        "colour": "0x6699FF"
    },
    "soulcollector": {
        "alignment": ["Neutral", "Apocalypse"],
        "colour": "0xFE014E"
    },
    "werewolf": {
        "alignment": ["Neutral", "Killing"],
        "colour": "0x9D7038"
    },
    "vampire": {
        "alignment": ["Neutral", "Outlier"],
        "colour": "0xd90707"
    }
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
    
roleAliases = {
    ("adm", "admi"): "admirer",
    "amne": "amnesiac",
    ("bg", "body"): "bodyguard",
    "cler": "cleric",
    "cata": "catalyst",
    "coro": "coroner",
    "crus": "crusader",
    "dep": "deputy",
    ("inv", "invest"): "investigator",
    "jail": "jailor",
    "lo": "lookout",
    "marsh": "marshal",
    ("mayo", "pilgrim"): "mayor",
    "mon": "monarch",
    ("ora", "orac"): "oracle",
    "pros": "prosecutor",
    "psy": "psychic",
    ("ret", "retri"): "retributionist",
    "sher": "sheriff",
    ("soc", "soci"): "socialite",
    "tav": "tavernkeeper",
    "track": "tracker",
    "trap": "trapper",
    "trick": "trickster",
    "vet": "veteran",
    ("vig", "vigi"): "vigilante",
    "conj": "conjurer",
    ("cl", "cov", "leader"): "covenleader",
    "cult": "cultist",
    ("dw", "dream"): "dreamweaver",
    "ench": "enchanter",
    ("hex", "hm"): "hexmaster",
    "illu": "illusionist",
    ("med", "medu"): "medusa",
    ("nec", "necro"): "necromancer",
    "pois": "poisoner",
    ("pm", "potion"): "potionmaster",
    "rit": "ritualist",
    ("vm", "voodoo"): "voodoomaster",
    "wild": "wildling",
    ("ars", "arso"): "arsonist",
    ("famine", "fam"): "baker",
    ("war", "bers"): "berserker",
    ("cs", "soul", "wanderingsoul", "cursed"): "cursedsoul",
    "doom": "doomsayer",
    ("exe", "exec"): "executioner",
    ("jest", "clown"): "jester",
    "pir": "pirate",
    ("plague", "pb", "pest", "pestilence"): "plaguebearer",
    "sk": "serialkiller",
    "shrond": "shroud",
    ("sc", "death"): "soulcollector",
    ("ww", "were"): "werewolf",
    "vamp": "vampire"
}

aliasLookup = {
    alias: fullName for keys, fullName in roleAliases.items() for alias in keys
}