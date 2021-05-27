from os import system, name, path
from enemy_class import Enemy
import commands
import json

input_marker = "-> "

def PrintOptions():
    print()
    print("  --------Main Menu--------")
    print("  1. Save New Enemy")
    print("  q. Quit")
    print()

def ClearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def NewEnemy():
    ClearScreen()
    print()
    print("  -------Enemy Creation-------")
    print()

    newEnemy = CollectEnemyData()
    if newEnemy != None:
        if ConfirmEnemy(newEnemy):
            SaveEnemy(newEnemy)
            print("Saved")
        else:
            print("Discarded")

    
    print()
    print("  Press Enter to continue")
    _ = input(input_marker)
       
def CollectEnemyData():
    playerEnemy = Enemy()
    
    print("  Enter Enemy Name")
    name = input(input_marker)
    playerEnemy.name = name
    print()

    print("  Enter Enemy Category (Fire Nation, Creature, Other Nation)")
    category = input(input_marker)
    category = category.lower()
    playerEnemy.category = category
    print()

    print("  Enter Enemy Level (Minion, Sub-Boss, Boss)")
    level = input(input_marker)
    level = level.lower()
    playerEnemy.level = level
    print()

    print("  Enter Enemy Health")
    health = GetPlayerInt()
    if health == None:
        return
    playerEnemy.health = health
    print()

    print("  Enter Enemy Damage")
    dmg = GetPlayerInt()
    if dmg == None:
        return
    playerEnemy.damage = dmg
    print()

    print("  Enter Enemy Defense")
    defense = GetPlayerInt()
    if defense == None:
        return
    playerEnemy.defense = defense
    print()

    print("  Enter Enemy Pierce")
    pierce = GetPlayerInt()
    if pierce == None:
        return
    playerEnemy.pierce = pierce
    print()

    print("  Single Target?")
    singleTarget = GetPlayerBool()
    if singleTarget == None:
        return
    playerEnemy.singleTarget = singleTarget
    print()

    if singleTarget:
        print("  Target Highest Health?")
        targetHighestHealth = GetPlayerBool()
        if targetHighestHealth == None:
            return
        playerEnemy.targetHighest = targetHighestHealth
        print()

        if not targetHighestHealth:
            print("  Target Lowest Health?")
            targetLowestHealth = GetPlayerBool()
            if targetLowestHealth == None:
                return
            playerEnemy.targetLowest = targetLowestHealth
            print()

    print("  Give Strength to other enemies?")
    giveStrength = GetPlayerBool()
    if giveStrength == None:
        return
    playerEnemy.giveStrength = giveStrength
    
    ClearScreen()

    return playerEnemy
    
def GetPlayerInt():
    playerString = input(input_marker)
    if playerString in commands.default:
        return 0

    if playerString.isdigit():
        playerInt = int(playerString)
        return playerInt
    else:
        print("  Error: Invalid integer input")
        return None

def GetPlayerBool():
    playerString = input(input_marker)
    if playerString in commands.default:
        return False
    
    if playerString in commands.true:
        return True
    elif playerString in commands.false:
        return False
    else: 
        print("  Error: Invalid boolean input")
        return None

def ConfirmEnemy(playerEnemy):
    print(str(playerEnemy))
    print()
    print("  Filename: " + GetEnemyFileName(playerEnemy))
    print()
    print("  Is this correct? [y/N]")
    response = GetPlayerBool()

    if path.exists(GetEnemyFileName(playerEnemy)):
        print("  File already exists. Overwrite?")
        response = GetPlayerBool()

    if response == None:
        return False
    else:
        return response

def SaveEnemy(playerEnemy):
    file = open(GetEnemyFileName(playerEnemy), "w")
    file.write(json.dumps(playerEnemy.__dict__))
    file.close()

def GetEnemyFileName(playerEnemy):
    return "enemies/" + playerEnemy.level.replace(" ","") + "_" + playerEnemy.name.replace(" ","")


if __name__ == "__main__":
    userInput = ""
    
    while userInput not in commands.quit:
        ClearScreen()
        PrintOptions()
        userInput = input(input_marker)
        if userInput in commands.newEnemy:
            NewEnemy()

