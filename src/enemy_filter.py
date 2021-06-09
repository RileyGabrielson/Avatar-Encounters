import src.enemy_files as enemy_files



def FilterByHealth(enemyList, minHealth, maxHealth):
    new_enemies = []
    
    for enemy in enemies:
        if enemy.health <= maxHealth and enemy.health >= minHealth:
            new_enemies.append(enemy)
    return new_enemies

def FilterByDamage(enemyList, minDamage, maxDamage):
    new_enemies = []
    
    for enemy in enemies:
        if enemy.damage <= maxDamage and enemy.damage >= minDamage:
            new_enemies.append(enemy)
    return new_enemies

def FilterByDefense(enemyList, minDefense, maxDefense):
    new_enemies = []
    
    for enemy in enemies:
        if enemy.defense <= maxDefense and enemy.defense >= minDefense:
            new_enemies.append(enemy)
    return new_enemies

def FilterByPierce(enemyList, minPierce, maxPierce):
    new_enemies = []
    
    for enemy in enemies:
        if enemy.pierce <= maxPierce and enemy.pierce >= minPierce:
            new_enemies.append(enemy)
    return new_enemies

def FilterByReflect(enemyList, minReflect, maxReflect):
    new_enemies = []
    
    for enemy in enemies:
        if enemy.reflect <= maxReflect and enemy.reflect >= minReflect:
            new_enemies.append(enemy)
    return new_enemies

def FilterBySingleTarget(enemyList):
    new_enemies = []
    
    for enemy in enemies:
        if enemy.singleTarget:
            new_enemies.append(enemy)
    return new_enemies


"""
def FilterByAOE(enemyList):
    new_enemies = []
    
    for enemy in enemies:
        if enemy.singleTarget:
            new_enemies.append(enemy)
    return new_enemies
"""

def FilterByCategory(enemyList, category):
    new_enemies = []

    for enemy in enemies: 
        if enemy.category == category.lower():
            new_enemies.append(enemy)
    return new_enemies

def FilterBylevel(enemyList, level):
    new_enemies = []

    for enemy in enemies: 
        if enemy.level == level.lower():
            new_enemies.append(enemy)
    return new_enemies

def FilterByGiveStrength(enemyList, giveStrength):
    new_enemies = []

    for enemy in enemies: 
        if enemy.giveStrength:
            new_enemies.append(enemy)
    return new_enemies


if __name__ == "__main__":
    enemies = enemy_files.GetEnemiesFromFile(enemy_files.GetEnemyFilenames())
    
    """
    new_enemies = FilterByDamage(enemies, 1, 4)
    new_enemies = FilterByDefense(new_enemies, 0, 0)
    new_enemies = FilterByHealth(new_enemies, 0, 3)
    new_enemies = FilterByPierce(new_enemies, 0, 0)
    new_enemies = FilterByReflect(enemies, 1, 5)
    new_enemies = FilterByCategory(new_enemies, "")
    new_enemies = FilterBylevel(new_enemies, "")
    new_enemies = FilterByGiveStrength(new_enemies, "giveStrength")
    for enemy in new_enemies:
    
    """

    new_enemies = FilterByGiveStrength(enemies, "giveStrength")


    for enemy in new_enemies:
        print("---------------------")
        print(enemy)
        print("---------------------")
        print()
    

    

