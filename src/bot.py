#bot.py

import discord
import os
import json
import requests
import asyncio

import Tos2Info
import utils

from discord.ext import commands
from discord.ext import tasks
from discord import app_commands

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
steamKey = os.getenv("STEAM_API_KEY")
testingGuildId = os.getenv("TESTGUILDID")

if testingGuildId != "0":
    GUILD_ID = discord.Object(id=testingGuildId)
else:
    GUILD_ID = None

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="f!", intents=intents)

@bot.event
async def on_ready():
    bot.remove_command("help") #the default help command exposes this bots' admin commands.
    if not refreshAchInfo.is_running():
        refreshAchInfo.start()

    if GUILD_ID is None:
        synced = await bot.tree.sync()
        print(f"Globally synced {len(synced)} commands")
    
    else:
        synced = await bot.tree.sync(guild=GUILD_ID)
        print(f"Guild synced {len(synced)} commands")

@tasks.loop(hours=48)
async def refreshAchInfo():
    await bot.wait_until_ready()

    utils.updateAchInfoJson(steamKey=steamKey)
    print("refreshed ach info")

#----------------------------------------------------------------------------------------

@bot.tree.command(name="linksteam", description="Links steam account to the discord bot for achievement tracking")
@app_commands.describe(steam_id="User steamID")
async def linkSteamAccount(interaction: discord.Interaction, steam_id: str):

    await interaction.response.defer(ephemeral=True)

    if not interaction.guild is None:

        if not (utils.isValidChannel(interaction.guild.id, interaction.channel.id) or interaction.user.guild_permissions.administrator):
            await interaction.followup.send(embed=utils.errorEmbed("Command cannot be used in this channel."))
            return

    profileName, error = await asyncio.to_thread(utils.getSteamProfileNameAndValidate, steamKey, steam_id)

    if error:
        await interaction.followup.send(embed=utils.errorEmbed(errorStr=f"{error}\n\n _If you are unsure how to get your steamID, use /help for more info._"))
        return
    
    with open(utils.steamLinkPath, "r") as steamLinks:
        links = json.load(steamLinks)
    
    links[str(interaction.user.id)] = steam_id

    with open(utils.steamLinkPath, "w") as steamLinks:
        json.dump(links, steamLinks, indent=4)

    await interaction.followup.send(f"Linked to steam account \"{profileName}\". \n\nIf this is not your steam account, use /unlink or /link again with the correct steamID", ephemeral=True)

#----------------------------------------------------------------------------------------

@bot.tree.command(name="unlink", description="Unlinks your steam account from the bot")
async def unlinkSteamAccount(interaction: discord.Interaction):

    if not interaction.guild is None:

        if not (utils.isValidChannel(interaction.guild.id, interaction.channel.id) or interaction.user.guild_permissions.administrator):
            await interaction.response.send_message(embed=utils.errorEmbed("Command cannot be used in this channel."))
            return
    
    with open(utils.steamLinkPath, "r") as steamLinks:
        links = json.load(steamLinks)

    if str(interaction.user.id) not in links:
        await interaction.response.send_message(embed=utils.errorEmbed("Failed to unlink: no linked steam account"))
        return
    
    del links[str(interaction.user.id)]

    with open(utils.steamLinkPath, "w") as steamLinks:
        links = json.dump(links, steamLinks, indent=4)

    await interaction.response.send_message("Successfully unlinked account.")

#----------------------------------------------------------------------------------------

@bot.tree.command(name="achievements", description="Displays the achievements for a given role")
@app_commands.describe(role_name="Name/alias of the TOS2 role (e.g. retri/retributionist)")
async def sendRoleAchInfo(interaction: discord.Interaction, role_name: str):

    await interaction.response.defer()

    if not interaction.guild is None:

        if not (utils.isValidChannel(interaction.guild.id, interaction.channel.id) or interaction.user.guild_permissions.administrator):
            await interaction.followup.send(embed=utils.errorEmbed("Command cannot be used in this channel."))
            return

    initialRoleName = role_name
    roleName = role_name.lower().replace(" ", "")
    
    with open(utils.achInfoPath, "r") as achInfo:
        achInfoDict = json.load(achInfo)

    roleName = Tos2Info.aliasLookup.get(roleName, roleName)
        
    if not roleName in achInfoDict:
        await interaction.followup.send(embed=utils.errorEmbed("Failed to fetch achievements: couldnt find role."))
        return
    
    with open(utils.steamLinkPath, "r") as accLinks:
        steamLinksDict = json.load(accLinks)
    
    accountLinked = False
    if str(interaction.user.id) in steamLinksDict:
        accountLinked = True
        authorAchStats = requests.get("https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/", params={"key":steamKey, "appid":"2140510", "steamid":steamLinksDict[str(interaction.user.id)]}).json()
    
    authorStatsReachable = True
    if accountLinked and ("error" in authorAchStats["playerstats"]):
        authorStatsReachable = False
        
    aEmbed = discord.Embed(title=f"Achievements for {initialRoleName}:",color=Tos2Info.getRoleColour(roleName))
    aEmbed.set_thumbnail(url=achInfoDict[roleName]["generalAchievements"][0]["icon"])

    for ach in achInfoDict[roleName]["generalAchievements"]:
        endStr = ""
        if accountLinked and authorStatsReachable:
            endStr = await asyncio.to_thread(utils.getAchCompletionStr, authorAchStats, ach["apiIndex"])

        if ach["isSecret"]:
            aEmbed.add_field(name=(f"||{ach["displayName"]}|| {endStr}"), value=f"||Hidden achievement...||\n-# `{ach["percent"]}% of players unlocked`", inline=False)
        else:
            aEmbed.add_field(name=(f"{ach["displayName"]} {endStr}"), value=f"{ach["description"]}\n-# `{ach["percent"]}% of players unlocked`",inline=False)

    if not accountLinked:
        aEmbed.add_field(name="",value="_Use /linksteam [steamID] to see your achievement completions_",inline=False)

    if not authorStatsReachable:
        aEmbed.add_field(name="",value=f"_Failed to access achievement completions: {authorAchStats["playerstats"]["error"]}_",inline=False)

    await interaction.followup.send(embed=aEmbed)

#----------------------------------------------------------------------------------------

@bot.tree.command(name="winstats", description="shows highest win achievement for every role, and an estimate for total wins.")
async def sendWinTotals(interaction:discord.Interaction):

    await interaction.response.defer()

    if not interaction.guild is None:

        if not (utils.isValidChannel(interaction.guild.id, interaction.channel.id) or interaction.user.guild_permissions.administrator):
            await interaction.followup.send(embed=utils.errorEmbed("Command cannot be used in this channel."))
            return

    with open(utils.steamLinkPath, "r") as accLinks:
        steamLinksDict = json.load(accLinks)

    if not str(interaction.user.id) in steamLinksDict:
        await interaction.followup.send(embed=utils.errorEmbed("This command requires a linked steam account. Use /linksteam [steamID] to link your steam account."))
        return

    userAchStats = requests.get("https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/", params={"key":steamKey, "appid":"2140510", "steamid":steamLinksDict[str(interaction.user.id)]}).json()

    if "error" in userAchStats["playerstats"]:
        await interaction.followup.send(embed=utils.errorEmbed(f"Failed to access achievement completions: {userAchStats["playerstats"]["error"]}"))
        return

    with open(utils.achInfoPath, "r") as achInfo:
        achInfoDict = json.load(achInfo)

    townStr = ""
    covStr = ""
    neutStr = ""
    totalWins = 0
    winAmtArr = [1, 5, 10, 25]
    for role in Tos2Info.roleInfo:
        if not role in achInfoDict:
            continue
        
        roleWins = 0

        for i in range(len(achInfoDict[role]["winAchievements"])-1, -1, -1): #iterate backwards
            pStatsIndex = (achInfoDict[role]["winAchievements"][i]["apiIndex"])

            if userAchStats["playerstats"]["achievements"][pStatsIndex]["achieved"]:
                roleWins = winAmtArr[i]
                totalWins += roleWins
                break

        match Tos2Info.roleInfo[role]["alignment"][0]:
            case "Town":
                townStr += f"\n{role}: {roleWins}"
            case "Coven":
                covStr += f"\n{role}: {roleWins}"
            case "Neutral":
                neutStr += f"\n{role}: {roleWins}"

    statsEmbed = discord.Embed(title="Win statistics (highest win achievements unlocked):", colour=0xd4af37)
    
    statsEmbed.add_field(name="Town Roles", value=townStr, inline=True)
    statsEmbed.add_field(name="Coven Roles", value=covStr, inline=True)
    statsEmbed.add_field(name="Neutral Roles", value=neutStr, inline=True)
    statsEmbed.add_field(name="Total Wins:", value=f"***{totalWins}+***", inline=False)
        
    await interaction.followup.send(embed=statsEmbed)

#----------------------------------------------------------------------------------------
#I'd like to keep API calls to a max of 1 per function, i'll have to make an exception for it here unless i find a better a method.

@bot.tree.command(name="nextunobtained", description="Shows the most common achievement that you haven't unlocked")
async def nextUnobtainedAch(interaction:discord.Interaction):
    await interaction.response.defer()

    if not interaction.guild is None:

        if not (utils.isValidChannel(interaction.guild.id, interaction.channel.id) or interaction.user.guild_permissions.administrator):
            await interaction.followup.send(embed=utils.errorEmbed("Command cannot be used in this channel."))
            return

    with open(utils.steamLinkPath, "r") as accLinks:
        steamLinksDict = json.load(accLinks)

    if not str(interaction.user.id) in steamLinksDict:
        await interaction.followup.send(embed=utils.errorEmbed("This command requires a linked steam account. Use /linksteam [steamID] to link your steam account."))
        return
    
    userAchStats = requests.get("https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/", params={"key":steamKey, "appid":"2140510", "steamid":steamLinksDict[str(interaction.user.id)]}).json()

    if "error" in userAchStats["playerstats"]:
        await interaction.followup.send(embed=utils.errorEmbed(f"Failed to access achievement completions: {userAchStats["playerstats"]["error"]}"))
        return
    
    orderedAchs = requests.get("https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/", params={"gameid":"2140510", "format":"json"}).json()

    if not "achievementpercentages" in orderedAchs:
        await interaction.followup.send(embed=utils.errorEmbed(f"Failed to access global achievement percentages."))
        return
    
    with open(utils.achInfoPath, "r") as achInfoJson:
        achInfoDict = json.load(achInfoJson)
    
    for ach in orderedAchs["achievementpercentages"]["achievements"]:

        roleName, achCategory = utils.getAchievementRoleAndCategory(ach["name"])

        for achFromDict in achInfoDict[roleName][achCategory]:
            if not achFromDict["apiName"] == ach["name"]:
                continue

            completionJsonIndex = achFromDict["apiIndex"]
            achInfo = achFromDict

        if not userAchStats["playerstats"]["achievements"][completionJsonIndex]["achieved"]:
            
            aEmbed = discord.Embed(title="Next Unobtained Achievement", color=Tos2Info.getRoleColour(roleName))
            aEmbed.set_thumbnail(url=achInfo["icon"])

            if achInfo["isSecret"]:
                aEmbed.add_field(name=(f"||{achInfo["displayName"]}||"), value=f"||Hidden achievement...||\n-# `{achInfo["percent"]}% of players unlocked`", inline=False)
            else:
                aEmbed.add_field(name=(f"{achInfo["displayName"]}"), value=f"{achInfo["description"]}\n-# `{achInfo["percent"]}% of players unlocked`",inline=False)

            await interaction.followup.send(embed=aEmbed)
            return

    await interaction.followup.send("If you are seeing this, the bot thinks you have completed _every_ achievement in TOS2.\n\nNot to discredit you or anything, but that seems unlikely.\n\nIf you haven't completed _every_ achievement in TOS2, please contact silph5. This command is broken.")
            
#----------------------------------------------------------------------------------------

@bot.tree.command(name="help", description="Lists all commands")
async def cmdHelp(interaction:discord.Interaction):

    if not interaction.guild is None:

        if not (utils.isValidChannel(interaction.guild.id, interaction.channel.id) or interaction.user.guild_permissions.administrator):
            await interaction.response.send_message(embed=utils.errorEmbed("Command cannot be used in this channel."), ephemeral=True)
            return
    
    helpEmbed = discord.Embed(title="Famine Help", description="-# Famine is an achievement tracking bot for Town Of Salem 2, allowing you to link your steam account and quickly access your progress on achievements for organised categories, such as per role.")
    
    helpEmbed.add_field(name="/linksteam", value="Links your steam account to your discord account so that the bot can access achievement completions.\nThis uses your steamID, which is the 17 digits on the end of the URL of your steam account.\n\n-# Usage example: `/linksteam 12345678912345678`", inline=False)
    helpEmbed.add_field(name="/unlink", value="Unlinks your steam account from the bot. This will make the bot unable to track your achievements.\n\n-# Usage example: `/unlink`", inline=False)
    helpEmbed.add_field(name="/achievements", value="Shows all the achievements of a specific role (and which ones you have completed if your steam account is linked)\n\n-# Usage example: `/achievements Admirer`", inline=False)
    helpEmbed.add_field(name="/winstats", value="Shows your highest win achievement in every role, alongside a minimum estimate of your total wins. Requires a linked account.\n\n-# Usage example: `/winstats`", inline=False)
    helpEmbed.add_field(name="/nextunobtained", value="Shows the next most common achievement that you have not completed. Requires a linked account.\n\n-# Usage example: `/nextunobtained`", inline=False)


    await interaction.response.send_message(embed=helpEmbed)
#----------------------------------------------------------------------------------------
#Admin-only commands (except admin help) are not slash commands

@bot.tree.command(name="adminhelp", description="Lists admin commands")
async def adminHelp(interaction:discord.Interaction):

    if interaction.guild is None:
        await interaction.response.send_message(embed=utils.errorEmbed("This command is for guilds only"))
        return

    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message(embed=utils.errorEmbed("This command is administrator only."), ephemeral=True)

    gSettings = utils.getGuildSettings(interaction.guild.id)
    
    aHelpEmbed = discord.Embed(title="Famine Admin Commands Guide", description="-# Guide to the admin commands for this bot.\n-# ALL admin commands (except this one) are prefixed with \"f!\" and are not accessible via the slash command autofill.")
    
    aHelpEmbed.add_field(name="f!restrictToChannel", value=f"Restricts command usages by non-admins to a specific channel. Use either the channel ID or a link to the channel as the parameter. To lift the restriction, type \"none\" as the parameter.\n\nUsage example: `f!restrictToChannel 1433446281514188872`\n\nCommands are currently restricted to channel: <#{gSettings["cmdChannel"]}>")
    aHelpEmbed.add_field(name="f!setUpdatesChannel", value=f"Sets a channel for the bot to send patch notes/privacy policy update notices. To make it send to no channels, type \"none\" as the parameter.\n\nUsage example: `f!setUpdatesChannel 1433446281514188872`\n\nPatch notes are currently sent to channel: <#{gSettings["patchChannel"]}>")
    aHelpEmbed.add_field(name="f!deleteGuildSettings", value=f"Deletes all settings for this guild. Use this command when you about to remove this application if you want to ensure that no data about your guild is kept by the bot.")

    await interaction.response.send_message(embed=aHelpEmbed, ephemeral=True)


@bot.command(name="restrictToChannel")
async def restrictCommandsToChannel(ctx, channel:discord.TextChannel):

    if ctx.guild is None:
        await ctx.send(embed=utils.errorEmbed("This command is for guilds only"))
        return
    
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("This command is guild administrator only.")
        return

    gSettings = utils.getGuildSettings(ctx.guild.id)

    gSettings["cmdChannel"] = str(channel.id)

    with open(os.path.join(utils.guildSDirPath, f"{ctx.guild.id}.json"), "w") as settings:
        json.dump(gSettings, settings, indent=4)
    
    await ctx.send("updated channel restriction settings for this guild.")

@bot.command(name="deleteGuildSettings")
async def deleteSettings(ctx):
    if ctx.guild is None:
        await ctx.send(embed=utils.errorEmbed("This command is for guilds only"))
        return
    
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("This command is guild administrator only.")
        return
    
    os.remove(os.path.join(utils.guildSDirPath, f"{ctx.guild.id}.json"))

    await ctx.send("Deleted guild settings file.\n\nNote: use of ANY command in this guild will create a new settings file with the default guild settings.")

@bot.command(name="setUpdatesChannel")
async def setUpdateChannel(ctx, channel:discord.TextChannel):

    if ctx.guild is None:
        await ctx.send(embed=utils.errorEmbed("This command is for guilds only"))
        return
    
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("This command is guild administrator only.")
        return
    
    gSettings = utils.getGuildSettings(ctx.guild.id)

    gSettings["patchChannel"] = str(channel.id)

    with open(os.path.join(utils.guildSDirPath, f"{ctx.guild.id}.json"), "w") as settings:
        json.dump(gSettings, settings, indent=4)
    
    await ctx.send("updated settings.")

#Dev only commands.

@bot.command(name="sendPatch")
async def sendPatch(ctx, *, message: str = None):
    
    if ctx.author.id != 1255077468130381874:
        await ctx.send("Dev only.")
        return
    
    for guild in bot.guilds:

        gSettings = utils.getGuildSettings(guild.id)
        patchChannel = gSettings["patchChannel"]

        if patchChannel == "none":
            continue

        channel = bot.get_channel(int(patchChannel))
        try:
            await channel.send(f"Famine update:\n{message}")
        except:
            print(f"failed to send patch to {guild.id}")
            


    
#command error handler
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=utils.errorEmbed(f"Missing argument: {error.param.name}."))
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=utils.errorEmbed("That command does not exist."))
    elif isinstance(error, commands.BadArgument):

        if ctx.command.name == "restrictToChannel":
            if ctx.message.content.lower().split()[1] == "none":
                gSettings = utils.getGuildSettings(ctx.guild.id)

                gSettings["cmdChannel"] = "none"
                
                with open(os.path.join(utils.guildSDirPath, f"{ctx.guild.id}.json"), "w") as settings:
                    json.dump(gSettings, settings, indent=4)

                await ctx.send("Removed channel restrictions.")
                return
        elif ctx.command.name == "setUpdatesChannel":
            if ctx.message.content.lower().split()[1] == "none":
                gSettings = utils.getGuildSettings(ctx.guild.id)

                gSettings["patchChannel"] = "none"
                
                with open(os.path.join(utils.guildSDirPath, f"{ctx.guild.id}.json"), "w") as settings:
                    json.dump(gSettings, settings, indent=4)

                await ctx.send("Removed update notifs.")
                return
            
        await ctx.send(embed=utils.errorEmbed("Bad argument"))

bot.run(token)

#should migrate this bot to cogs at some point if more features are added