# Famine
Famine is a Steam achievement tracking Discord bot for Town Of Salem 2, allowing you to link your steam account and quickly access your progress on achievements in organised categories, such as per role.

Famine is written entirely in python and interfaces with the Steam Web API via HTTP requests to receive achievement info. 

The bots privacy policy contains exhaustive information on what data the bot collects and how much of that data is stored.
https://github.com/Silph5/Famine-docs-legal
## Basic Commands
### /faminehelp
/faminehelp is Famine's /help command equivalent, and will produce an embed with a description of every command available to the bot.
### /linksteam
/linksteam is the command used to link steam accounts to discord accounts in the Famine's internal database. This is necessary to allow the bot to track specific achievement completions via HTTP requests to the Steam Web API. 
It takes one argument, being the steamID of the user's Steam account, and will ephemerally notify the user with the username of the account they just linked to help ensure they are linked to the correct account.

Usage example: `/linksteam 12345678912345678`
### /unlink
/unlink simply deletes the user's Discord and Steam account link from the bot's database, alongside any other user-specific data that may be kept.

### /achievements
/achievements produces all (non-win related) achievements for a given Town of Salem 2 role. This includes the achievement's name, description, secrecy, and global achievement completion percentage. 
If the user of the command has their steam account linked, the bot will also attempt to access their achievement completions from the Steam Web API when this command is used, and will show which of the achievements have been completed.
The command takes one argument, being the name of the role. It also accepts commonly used role aliases such as _CS_ instead of _cursed soul_.

Usage example: `/achievements admirer`
### /winstats
/winstats accesses user achievement completions, iterates through every Town of Salem 2 role, and finds the highest win achievement that the user has obtained. It will then display this for every role, and include a total minimum win count.
This command requires the user to have linked their account via /linksteam.

### /nextunobtained
/nextunobtained fetches user achievement completions and checks through them in order of least rare to most rare by global achievement percentage until it finds an achievement the user hasn't completed yet. 
In other words, it finds the most common unobtained achievement. This command requires the user to have linked their account via /linksteam.
## Guild Admin Commands
Guild Admin commands are used to change the settings of the bot in that guild.
By default, all guild settings are simply set to "none".
### /adminhelp
/adminhelp is the only admin-only command which is visible via the slash command autofill/gui. It produces an embed with a description of all admin-only commands.
It will also show all the current bot settings for the guild it is used in.

### f!restrictToChannel
Restricts command usages by non-admins to a specific channel. 
Takes either the channel ID or a link to the channel as the argument. To lift the restriction, use "none" as the parameter.

Usage example: `f!restrictToChannel 1433446281514188872`

### f!setUpdatesChannel
Sets the channel in which the bot will send patch notes when it is updated. 
Takes either the channel ID or a link to the channel as the argument. To disable this feature, type "none" as the parameter.

Usage example: `f!setUpdatesChannel 1433446281514188872`

### f!deleteGuildSettings
Deletes the guild settings file for the guild. On the user end, this will effectively reset all per-guild bot settings to their defaults for the guild the command is used in.
Any other interaction with the bot will immediately produce a new settings file, so if you wish to wipe the guild from the bots data when removing it from a guild, you must ensure that this is the last command used.

## Storage of Achievement Info

achInfo.json is a (gitignored) json file in the data dir which the bot populates with information from the Steam Web API every 48 hours while it is online. This is the structure from which commands such as /nextUnobtained and /achievements pull non-user-specific achievement information such as the achievements' name, description and global percentages.

This information is pulled from the following Steam Web API endpoints:
 - https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key=XXXXXXXXXXXXX&appid=2140510
 - http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid=2140510&format=json

In the achInfo json populated by the 48 hour looping task, the collected data for each role is stored like this:

```json
{
    "roleName": {
        "winAchievements": [
            {
                "apiIndex": 2,
                "apiName": "WinXGamesAsThisRole",
                "displayName": "Achievement name",
                "description": "Win X games as This Role",
                "isSecret": 0,
                "percent": "20.1",
                "icon": "(URL to ach icon on steam)"
            }
        ],
        "generalAchievements": [
            {
                "apiIndex": 9,
                "apiName": "ThisRoleDoThisThing",
                "displayName": "Achievement name",
                "description": "Do this thing as This Role",
                "isSecret": 0,
                "percent": "5.3",
                "icon": "(URL to ach icon on steam)"
            }
        ]
    }
}
```

This structuring is designed to make accessing specific types of achievements as quick as possible in the context of the Famine's usecases.

