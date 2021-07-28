#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Print stats for players (WIP)
# 
# List all the categories, see https://minecraft.fandom.com/wiki/Statistics
# ['custom', 'mined', 'killed', 'broken', 'dropped', 'used', 'picked_up', 'crafted', 'killed_by']

import json
import os
import datetime

# Tick to HH:MM:SS
def getTime(tick):
    if type(tick)!=int: return None
    seconds = tick//20
    return datetime.timedelta(seconds=seconds)

def printGetTime(dic):
    for key, value in dic.items():
        dic[key] = str(getTime(value))
    print(dic)

# function to return key for any value
def getKey(dic, val):
    for key, value in dic.items():
         if val == value:
             return key
 
    return None


mcDir = '/path/to/mc'
backupDir = mcDir+'backup/'

whitelist = mcDir+'/server/whitelist.json'

# Get a dictionnary of uuid:player_name
players = {}
with open(whitelist) as jsonFile:
    data = json.load(jsonFile)
    for dic in data:
        players[dic['uuid']] = dic['name']

# for i in players:
#     print(players[i])


# Get stat value given jsonfile, category and stat (without minecraft: tag)
def getValue(jsonFile, category, stat):
    category = 'minecraft:'+category
    stat = 'minecraft:'+stat
    data = json.load(jsonFile)
    try:
        return data['stats'][category][stat]
    except:
        return 0
    



# Get stat value given backupfolder and player name
def getValuePlayer(player, backupFolder, category, stat):
    if getKey(players, player) is None: return 'None'
    value = 0
    statsDir = backupDir+backupFolder+'/world/stats/'
    try:
        with open(statsDir+getKey(players, player)+'.json') as jsonFile:
            return getValue(jsonFile, category, stat)
    except:
        return 0

# Examples
print("getValuePlayer")
print(getTime(getValuePlayer('PlayerName','YYYY-MM-DDTHH.MM.SS','custom','play_one_minute')))
print(getTime(getValuePlayer('PlayerName','YYYY-MM-DDTHH.MM.SS','custom','time_since_death')))
    



# Get stat value given backupfolder
def getValueOneSave(backupFolder, category, stat):
    value = 0
    statsDir = backupDir+backupFolder+'/world/stats/'
    for uuid in players:
            try:
                with open(statsDir+uuid+'.json') as jsonFile:
                    value += getValue(jsonFile, category, stat)
            except:
                value += 0
    return value

# Examples
print("getValueOneSave")
print(getTime(getValueOneSave('YYYY-MM-DDTHH.MM.SS','custom','play_one_minute')))
    



# Get stat value from all backup
def getValueFromAllSave(category, stat):
    value = 0
    for entry in os.scandir(backupDir):
        statsDir = backupDir+str(entry.name)+'/world/stats/'
        for uuid in players:
            try:
                with open(statsDir+uuid+'.json') as jsonFile:
                    value += getValue(jsonFile, category, stat)
            except:
                value += 0
    return value

# Examples
print("getValueFromAllSave")
print(getTime(getValueFromAllSave('custom','play_one_minute')))




# Get best stat value and give which save
def getBestSave(category, stat):
    bestDir = ''
    bestValue = 0
    for entry in os.scandir(backupDir):
        value = 0
        statsDir = backupDir+str(entry.name)+'/world/stats/'
        for uuid in players:
            try:
                with open(statsDir+uuid+'.json') as jsonFile:
                    value += getValue(jsonFile, category, stat)
            except:
                value += 0
        if value > bestValue: 
            bestDir = entry
            bestValue = value
    return bestDir, bestValue

# Examples
print("getBestSave")
print(getBestSave('custom','play_one_minute'))




# Get highest or lowest stat value and which player in which save
def getBestPlayerOneSave(category, stat, comparator='higher'):
    bestDir = ''
    bestPlayer = ''
    bestValue = 0
    for entry in os.scandir(backupDir):
        statsDir = backupDir+str(entry.name)+'/world/stats/'
        for uuid in players:
            try:
                with open(statsDir+uuid+'.json') as jsonFile:
                    value = getValue(jsonFile, category, stat)
            except:
                value = 0
            
            if value == bestValue:
                bestValue += value
                bestDir += statsDir
                bestPlayer += players[uuid]
            
            if comparator=='higher':
                if value > bestValue:
                    bestValue = value
                    bestDir = statsDir
                    bestPlayer = players[uuid]
            elif comparator=='lower':
                if value < bestValue:
                    bestValue = value
                    bestDir = statsDir
                    bestPlayer = players[uuid]
            else:
                print('Undefined comparator')
                quit()
    return bestPlayer, bestValue, bestDir

# Examples
print("getBestPlayerOneSave")
print(getBestPlayerOneSave('custom','play_one_minute'))




# Get stat value for all players in all save cumulatively
def getValuePlayersAllSave(category, stat):
    values = {}
    for uuid in players:
        values[players[uuid]] = 0

    for entry in os.scandir(backupDir):
        statsDir = backupDir+str(entry.name)+'/world/stats/'
        for uuid in players:
            try:
                with open(statsDir+uuid+'.json') as jsonFile:
                    values[players[uuid]] += getValue(jsonFile, category, stat)
            except:
                values[players[uuid]] += 0
            
    return {k: v for k, v in sorted(values.items(), key=lambda item: item[1])}

# Examples
print("getValuePlayersAllSave")
print(GetTime(getValuePlayersAllSave('custom','play_one_minute')))
print(getValuePlayersAllSave('used','torch'))




# Get stat values for all players in one save
def getValuePlayers1Save(backupFolder, category, stat):
    values = {}
    for uuid in players:
        values[players[uuid]] = 0

    statsDir = backupDir+backupFolder+'/world/stats/'
    for uuid in players:
        try:
            with open(statsDir+uuid+'.json') as jsonFile:
                values[players[uuid]] += getValue(jsonFile, category, stat)
        except:
            values[players[uuid]] += 0
            
    return {k: v for k, v in sorted(values.items(), key=lambda item: item[1])}

# Examples
print("getValuePlayers1Save")
print(GetTime(getValuePlayers1Save('YYYY-MM-DDTHH.MM.SS','custom','play_one_minute')))