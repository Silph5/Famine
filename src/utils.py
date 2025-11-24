import os
import json
import requests
import re
import Tos2Info
import discord

achInfoPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "achInfo.json")
steamLinkPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),  "data", "steamLinks.json")
guildSDirPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),  "data", "guildSettings")

def errorEmbed(errorStr):
    return discord.Embed(title="Command failed", description=errorStr, colour=0xd4af37)

def getGuildSettings(guildID):
    try: 
        with open(os.path.join(guildSDirPath, f"{guildID}.json"), "r") as settings:
            settingsDict = json.load(settings)
            
        return settingsDict
    
    except FileNotFoundError:
        with open(os.path.join(guildSDirPath, f"{guildID}.json"), "w") as settings:
            default = {
                "cmdChannel":"none"
            }
            json.dump(default, settings, indent=4)

        with open(os.path.join(guildSDirPath, f"{guildID}.json"), "r") as settings:
            settingsDict = json.load(settings)

        return settingsDict

def isValidChannel(guildID, ctxChannelID):
    gSettings = getGuildSettings(guildID)
    if str(gSettings["cmdChannel"]) == "none":
        return True
    if str(gSettings["cmdChannel"]) != str(ctxChannelID):
        return False
    
    return True

def getSteamProfileNameAndValidate(steamKey, steamId):

    if not steamId.isdigit():
        return None, "SteamIDs must be numeric"
    
    if not len(steamId) == 17:
        return None, "SteamIDs must be 17 digits long"
    
    if not steamId[:7] == "7656119":
        return None, "user SteamID invalid"
    
    #requests information of account with given steamId
    response = requests.get("https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/", params={"key":steamKey, "steamids":steamId})
    
    profile = response.json()

    if response.status_code != 200:
        return None, "unable to reach steam"
    
    if not profile["response"]["players"]:
        return None, "SteamID is not associated with an account"

    return profile["response"]["players"][0]["personaname"], None

def getAchCompletionStr(playerAchJson, achApiIndex):
    if playerAchJson["playerstats"]["achievements"][achApiIndex]["achieved"] == 1:
        return " - :white_check_mark:"
    else:
        return " - :x:"
    
#------------------------------------------------------------------------------------------------------
#this is all for the big messy function that populates achInfo.json with info from various steamAPI endpoints. 

def getAchievementRoleAndCategory(achName):

    wordsArray = re.split(r"(?=[A-Z0-9])(?<=[a-z])|(?<=[0-9])(?=[A-Z])", achName) 
    #this regex splits the string into words and FULL numbers (e.g. "Win", "25", "Games")

    if wordsArray[0] == "Win":
        achCategory = "winAchievements"
        try:
            roleName = wordsArray[4].lower()
        except:
            roleName = ""
    else:
        achCategory = "generalAchievements"
        roleName = wordsArray[0].lower()
    
    match roleName:
        case "mayore": 
            roleName = "mayor"
            #typo in steam api
        case "tavern":
            roleName = "tavernkeeper"
        case "coven":
            roleName = "covenleader"
        case "hex":
            roleName = "hexmaster"
        case "potion":
            roleName = "potionmaster"
        case "voodoo":
            roleName = "voodoomaster"
        case "soul":
            roleName = "soulcollector"
        case "cursed":
            roleName = "cursedsoul"
        case "serial":
            roleName = "serialkiller"
    
    if not roleName in Tos2Info.roleInfo:
        roleName = "misc"
        achCategory = "generalAchievements"

    return roleName, achCategory


def updateAchInfoJson(steamKey):

    newDictForJson = {}
    newDictForJson["misc"] = {
        "icon":"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/2140510/b2570c971297dba7fd62abd5f66d877ff99e31b5.jpg",
        "generalAchievements":[]
    }

    response = requests.get("https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/", params={"key":steamKey, "appid":"2140510"})
        
    gameSchema = response.json()

    for apiIndex, ach in enumerate(gameSchema["game"]["availableGameStats"]["achievements"]):
        
        roleName, achCategory = getAchievementRoleAndCategory(ach["name"])

        if not roleName in newDictForJson:
            newDictForJson[roleName] = {
                "icon":ach["icon"],
                "winAchievements":[],
                "generalAchievements":[]
            }
        
        
        newDictForJson[roleName][achCategory].append({
            "apiIndex":apiIndex,            
            "apiName":ach["name"],
            "displayName":ach["displayName"],
            "description":ach.get("description", ""),
            "isSecret":ach["hidden"],
            "percent":""
        })

    #get global percents from next endpoint

    response = requests.get("https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/", params={"gameid":"2140510", "format":"json"})

    globalPercents = response.json()

    for ach in globalPercents["achievementpercentages"]["achievements"]:
        
        roleName, achCategory = getAchievementRoleAndCategory(ach["name"])

        if not roleName in newDictForJson:
            continue

        for achListI, knownAch in enumerate(newDictForJson[roleName][achCategory]):
            if knownAch["apiName"] == ach["name"]:
                newDictForJson[roleName][achCategory][achListI]["percent"] = ach["percent"]
                break


    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "achInfo.json")

    with open(achInfoPath, "w") as achInfo:
        json.dump(newDictForJson, achInfo, indent=4)