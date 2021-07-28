# Minecraft Hardcore Server Tools 

## True multiplayer hardcore experience ✅

Whenever a player dies, everyone online is instantaneously switched to spectator mode for 90 sec. Then, automatically, the server is shut down, a backup of the deleted world is created and a new seed is generated, playable within ~5 min.

Provided with some scripts for a discord bot and a python script to extract statistics across all backup files.


## Requirements 📑

A linux machine with `Python3`, `cron` and `JAVA`. See *Troubleshooting* section for hardcoded things to change in the code.

Then:

 * Need **[Spigot](https://getbukkit.org/download/spigot)** (worked with 1.16.5) to create the server

 * Need **[Skript](https://github.com/SkriptLang/Skript)** pluggin to trigger the `hardcore.sk` script when someone dies

 * Put in **cron** with `crontab -e`:
    - ```*/1 * * * * $(which python3) /path/to/mc/minecraft.py check >> /path/to/mc/cron.log```
    - It checks every minute if the server is still running. If not, a backup is created, the world is deleted and a new seed is generated.

 * **[ScriptBot](https://github.com/Cubxity/ScriptBot)** (worked with 1.2) for cool discord integration
    - `eventhandler.java` in `server\plugins\ScriptBot\scripts` displays cool messages on death for example.


 > **Bonus**: [Other cool bot](https://github.com/tedztar/mcstatusbot/) to show in status how many players connected: 


## Troubleshooting 🛠

⚠ **Hardcoded things to change**:

- [`minecraft.py`](mc/minecraft.py):
  - **l.22** : path to `mc/server`
  - **l.29** : path to `mc/backup`

- [`getStatistics.py`](getStatistics.py):
  - **l.28** : path to `mc`

- [`ScriptBot/config.yml`](mc/server/plugins/ScriptBot/config.yml):
  - **l.7** : discord bot-token

- [`ScriptBot/scripts/*`](mc/server/plugins/ScriptBot/scripts/):
  - `bot.getTextChannelById` : discord channel ID

⚠ Important to add a **whitelist** to use [`getStatistics.py`](getStatistics.py).

⚠ If JAVA problems: need to have this JAVA version for Spigot to work:
```
java -version
sudo apt-get install openjdk-8-jdk
```
Should see and pick this version with `sudo update-alternatives --config java`:
```
2            /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java   1081      manual mode
```

## Credits ®
`minecraft.py` arranged from:
https://github.com/tschuy/minecraft-server-control
