from difficulty import getDifficulty
import enemy_filter as filter
from encounter_param import Encounter_Param
import random
import enemy_files
import copy
from os import system, name


NO_VALID_ENEMIES = 'NO VALID ENEMIES'


def GenerateEncounterAOE(enemies, params):
    
    if not isinstance(params, Encounter_Param):
        raise ValueError("Params must be an Encounter_Param Object")
    encounter = []
    i = 0
    while i < params.generateAttempts and len(encounter) == 0:
        current_params = copy.deepcopy(params)
        encounter = []
        filtered_enemies = filter.FilterByAOE(enemies)
        if params.category != None:
            filtered_enemies = filter.FilterByCategory(filtered_enemies, params.category)
        new_enemy = None

        while True:
            new_enemy = GetEnemyWithinBounds(filtered_enemies, current_params)
            if new_enemy != NO_VALID_ENEMIES:
                encounter.append(new_enemy)
                current_params.maxDifficulty -= getDifficulty(new_enemy)
            else:
                break

        if current_params.maxDifficulty < params.maxDifficulty - params.minDifficulty:
            return encounter
    
    return []

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

def setParams(enemies):
        categories = filter.GetEnemyCategories(enemies)
        categories_list = ''
        for c in categories:
            categories_list += c + ", "
        
        ClearScreen()
        print()
        minDifficulty = int(input("Min Difficulty: "))
        maxDifficulty = int(input("Max Difficulty: "))
        print()
        print("Available Categories: " + categories_list.title())
        category = input("Category? (Hit Enter for any category): ")
        if category == '':
            category = None
        return [minDifficulty, maxDifficulty, category]

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

    enemies = enemy_files.GetEnemiesFromFile(enemy_files.GetEnemyFilenames())
    maxDifficulty = 0
    category = None
    [minDifficulty, maxDifficulty, category] = setParams(enemies)
    params = Encounter_Param()

    while(True):
        ClearScreen()
        print(" ********  ENCOUNTER GENERATOR ********")
        print()
        print("  -- Min Difficulty: " + str(minDifficulty))
        print("  -- Max Difficulty: " + str(maxDifficulty))
        print("  -- Category: " + str(category))
        print()
        params.minDifficulty = minDifficulty
        params.maxDifficulty = maxDifficulty
        params.category = category
        encounter = GenerateEncounterAOE(enemies, params)

        if len(encounter) == 0:
            print("Could not generate encounter in " + str(params.generateAttempts) + " attempts. Try again!")
        else:
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
        

        userInput = input("Press enter to generate another encounter (q to quit, e to edit params): ").lower()
        if userInput == "q":
            break
        elif userInput == "e":
            [minDifficulty, maxDifficulty, category] = setParams(enemies)