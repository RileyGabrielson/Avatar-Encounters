from difficulty import getDifficulty
import enemy_filter as filter
from encounter_param import Encounter_Param
from enemy import Enemy
import random
import enemy_files
import copy
from os import system, name


NO_VALID_ENEMIES = 'NO VALID ENEMIES'


def GenerateEncounterAOE(enemies, params):
    
    if not isinstance(params, Encounter_Param):
        raise ValueError("Params must be an Encounter_Param Object")

    current_params = copy.deepcopy(params)
    encounter = []
    filtered_enemies = filter.FilterByAOE(enemies)
    new_enemy = None

    while True:
        new_enemy = GetEnemyWithinBounds(filtered_enemies, current_params)
        if new_enemy != NO_VALID_ENEMIES:
            encounter.append(new_enemy)
            current_params.maxDifficulty -= getDifficulty(new_enemy)
        else:
            break
    
    return encounter

def GetEnemyWithinBounds(enemies, params):
    filtered_enemies = filter.FilterByDifficulty(enemies, 0, params.maxDifficulty)

    if len(filtered_enemies) == 0:
        return NO_VALID_ENEMIES

    return filtered_enemies[random.randint(0, len(filtered_enemies) - 1)]

def ClearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def setParams():
        ClearScreen()
        print()
        maxDifficulty = int(input("Max Difficulty: "))
        return [0, maxDifficulty]

def getTotals(enemies):
    health = 0
    damage = 0
    defense = 0
    pierce = 0
    reflect = 0
    statusEffects = 0
    difficulty = 0

    for enemy in enemies:
        health += enemy.health
        damage += enemy.damage
        defense += enemy.defense
        pierce += enemy.pierce
        reflect += enemy.reflect
        statusEffects += enemy.burn + enemy.stun + enemy.fatigue + enemy.loseCoin
        difficulty += getDifficulty(enemy)

    return [health, damage, defense, pierce, reflect, statusEffects, difficulty]



if __name__ == "__main__":

    minDifficulty = 0
    maxDifficulty = 0
    [minDifficulty, maxDifficulty] = setParams()
    params = Encounter_Param()

    while(True):
        ClearScreen()
        print(" ********  ENCOUNTER GENERATOR ********")
        print()
        print("  -- Max Difficulty: " + str(maxDifficulty))
        print()
        params.minDifficulty = minDifficulty
        params.maxDifficulty = maxDifficulty
        encounter = GenerateEncounterAOE(enemy_files.GetEnemiesFromFile(enemy_files.GetEnemyFilenames()), params)

        for enemy in encounter:
            print(enemy)
            print()
        [health, damage, defense, pierce, reflect, statusEffects, difficulty] = getTotals(encounter)
        print("Total Health: " + str(health))
        print("Total Damage: " + str(damage))
        print("Total Defense: " + str(defense))
        print("Total Pierce: " + str(pierce))
        print("Total Reflect: " + str(reflect))
        print("Total Status Effect: " + str(statusEffects))
        print()
        print("Total Difficulty: " + str(round(difficulty, 2)))
        print()
        

        userInput = input("Generate Encounter (q to quit, e to edit params) ").lower()
        if userInput == "q":
            break
        elif userInput == "e":
            [minDifficulty, maxDifficulty] = setParams()