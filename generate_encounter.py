import enemy_filter as filter
from encounter_param import Encounter_Param
from enemy_class import Enemy
import random
import enemy_files
import copy
from os import system, name


NO_VALID_ENEMIES = -10


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
            current_params.maxHealth -= new_enemy.health
            current_params.maxDamage -= new_enemy.damage + new_enemy.pierce
            current_params.maxDefense -= new_enemy.defense
        else:
            break
    
    return encounter




def GetEnemyWithinBounds(enemies, params):
    filtered_enemies = filter.FilterByDamage(enemies, 0, params.maxDamage)
    filtered_enemies = filter.FilterByHealth(filtered_enemies, 0, params.maxHealth)
    filtered_enemies = filter.FilterByDefense(filtered_enemies, 0, params.maxDefense)

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
        maxHealth = int(input("Max Health: "))
        maxDamage = int(input("Max Damage: "))
        maxDefense = int((input("Max Defense: ")))
        return [maxHealth, maxDamage, maxDefense]


if __name__ == "__main__":

    maxHealth = 0
    maxDamage = 0
    maxDefense = 0
    [maxHealth, maxDamage, maxDefense] = setParams()
    params = Encounter_Param()

    while(True):
        ClearScreen()
        print(" ********  ENCOUNTER GENERATOR ********")
        print()
        print("  -- Max Health: " + str(maxHealth))
        print("  -- Max Damage: " + str(maxDamage))
        print("  -- Max Defense: " + str(maxDefense))
        print()
        params.maxHealth = maxHealth
        params.maxDamage = maxDamage
        params.maxDefense = maxDefense
        encounter = GenerateEncounterAOE(enemy_files.GetEnemiesFromFile(enemy_files.GetEnemyFilenames()), params)
        for enemy in encounter:
            print(enemy)
            print()

        userInput = input("Generate Encounter (q to quit, e to edit params) ").lower()
        if userInput == "q":
            break
        elif userInput == "e":
            [maxHealth, maxDamage, maxDefense] = setParams()