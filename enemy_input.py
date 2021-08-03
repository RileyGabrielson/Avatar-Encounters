from os import system, name, path, listdir
from enemy import Enemy
import commands
import enemy_files

INPUT_MARKER = "-> "


def PrintOptions():
    print()
    print("  --------Main Menu--------")
    print()
    print("  1. Create New Enemy")
    print("  2. Enemy Gallery")
    print("  3. Help")
    print("  q. Quit")
    print()

def ClearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def Help():
    ClearScreen()
    print()
    print("  -------Help-------")
    print()
    print("  Commands")
    print("  If inputting a number, press enter to default to 0")
    print("  If inputting a boolean, press enter to default to False")
    print()
    _ = input(INPUT_MARKER)

def NewEnemy():
    ClearScreen()
    print()
    print("  -------Enemy Creation-------")
    print()

    newEnemy = CollectEnemyData()
    if newEnemy != None:
        if ConfirmEnemy(newEnemy):
            enemy_files.SaveEnemy(newEnemy)
            print("Saved")
        else:
            print("Discarded")

    
    print()
    print("  Press Enter to continue")
    _ = input(INPUT_MARKER)
       
def CollectEnemyData():
    playerEnemy = Enemy()
    
    print("  Enter Enemy Name")
    name = input(INPUT_MARKER)
    playerEnemy.name = name
    print()

    print("  Enter Enemy Category (Fire Nation, Creature, Other Nation)")
    category = input(INPUT_MARKER)
    category = category.lower()
    playerEnemy.category = category
    print()

    print("  Enter Enemy Level (Minion, Sub-Boss, Boss)")
    level = input(INPUT_MARKER)
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

    print("  Enter Enemy Reflect")
    reflect = GetPlayerInt()
    if reflect == None:
        return
    playerEnemy.reflect = reflect
    print()

    print("  Enter Enemy Burn")
    burn = GetPlayerFloat()
    if burn == None:
        return
    playerEnemy.burn = burn
    print()

    print("  Enter Enemy Stun")
    stun = GetPlayerFloat()
    if stun == None:
        return
    playerEnemy.stun = stun
    print()

    print("  Enter Enemy Fatigue")
    fatigue = GetPlayerFloat()
    if fatigue == None:
        return
    playerEnemy.fatigue = fatigue
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

    print("  Give strength to other enemies?")
    giveStrength = GetPlayerBool()
    if giveStrength == None:
        return
    playerEnemy.giveStrength = giveStrength
    print()

    print("  Give defense to other enemies?")
    giveDefense = GetPlayerBool()
    if giveDefense == None:
        return
    playerEnemy.giveDefense = giveDefense
    print()

    if giveDefense:
        print("  How much defense is given to other enemies?")
        defense = GetPlayerInt()
        if defense == None:
            return
        playerEnemy.giveDefenseAmount = defense
        print()
    
    ClearScreen()

    return playerEnemy
    
def GetPlayerInt():
    playerString = input(INPUT_MARKER)
    if playerString in commands.default:
        return 0

    if playerString.isdigit():
        playerInt = int(playerString)
        return playerInt
    else:
        print("  Error: Invalid integer input")
        return None

def GetPlayerFloat():
    playerString = input(INPUT_MARKER)
    if playerString in commands.default:
        return 0.0

    try:
        playerFloat = float(playerString)
        return playerFloat
    except ValueError:
        print("  Error: Invalid float input")
        return None


def GetPlayerBool():
    playerString = input(INPUT_MARKER)
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
    print("  Filename: " + enemy_files.GetEnemyFileName(playerEnemy))
    print()
    print("  Is this correct?")
    response = GetPlayerBool()

    if path.exists(enemy_files.GetEnemyFileName(playerEnemy)):
        print("  File already exists. Overwrite?")
        response = GetPlayerBool()

    if response == None:
        return False
    else:
        return response

def EnemyGallery():
    ClearScreen()
    print()
    print("  -------Enemy Gallery-------")
    print("  Enter a number to examine an enemy")
    print("  (Press Enter to return)")
    print()

    filenames = enemy_files.GetEnemyFilenames()
    enemies = enemy_files.GetEnemiesFromFile(filenames)
    ListEnemies(enemies)

    playerIndex = input(INPUT_MARKER)
    if not playerIndex.isdigit():
        return
    else:
        index = int(playerIndex)
        index -= 1
        if index < 0 or index >= len(enemies):
            return
        else:
            DisplayEnemy(enemies[index])
            EnemyGallery()

def DisplayEnemy(enemy):
    ClearScreen()
    print()
    print("  " + AddSpacesToLines(str(enemy)))
    print()
    print("  Press Enter to return to gallery")
    print()
    _ = input(INPUT_MARKER)

def AddSpacesToLines(s):
    return '  '.join(s.splitlines(True))

def ListEnemies(enemies):
    for i in range(0, len(enemies)):
        if(i < 9):
            extraSpace = ' '
        else:
            extraSpace = ''
        
        print("  " + str(i+1) + ". " + extraSpace + enemies[i].level.title()+ ": " + enemies[i].name)
    print()




if __name__ == "__main__":
    userInput = ""
    
    while userInput not in commands.quit:
        ClearScreen()
        PrintOptions()
        userInput = input(INPUT_MARKER)
        if userInput in commands.newEnemy:
            NewEnemy()
        if userInput in commands.help:
            Help()
        if userInput in commands.enemyGallery:
            EnemyGallery()


