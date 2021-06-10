import enemy_files

def FilterByHealth(enemyList, minHealth, maxHealth):
    new_enemies = []
    
    for enemy in enemyList:
        if enemy.health <= maxHealth and enemy.health >= minHealth:
            new_enemies.append(enemy)
    return new_enemies

def FilterByDamage(enemyList, minDamage, maxDamage):
    new_enemies = []
    
    for enemy in enemyList:
        if enemy.damage <= maxDamage and enemy.damage >= minDamage:
            new_enemies.append(enemy)
    return new_enemies

def FilterByDefense(enemyList, minDefense, maxDefense):
    new_enemies = []
    
    for enemy in enemyList:
        if enemy.defense <= maxDefense and enemy.defense >= minDefense:
            new_enemies.append(enemy)
    return new_enemies

def FilterByPierce(enemyList, minPierce, maxPierce):
    new_enemies = []
    
    for enemy in enemyList:
        if enemy.pierce <= maxPierce and enemy.pierce >= minPierce:
            new_enemies.append(enemy)
    return new_enemies

def FilterByReflect(enemyList, minReflect, maxReflect):
    new_enemies = []
    
    for enemy in enemyList:
        if enemy.reflect <= maxReflect and enemy.reflect >= minReflect:
            new_enemies.append(enemy)
    return new_enemies

def FilterBySingleTarget(enemyList):
    new_enemies = []
    
    for enemy in enemyList:
        if enemy.singleTarget:
            new_enemies.append(enemy)
    return new_enemies

def FilterByAOE(enemyList):
    new_enemies = []
    
    for enemy in enemyList:
        if not enemy.singleTarget:
            new_enemies.append(enemy)
    return new_enemies

def FilterByCategory(enemyList, category):
    new_enemies = []

    for enemy in enemyList: 
        if enemy.category == category.lower():
            new_enemies.append(enemy)
    return new_enemies

def FilterByLevel(enemyList, level):
    new_enemies = []

    for enemy in enemyList: 
        if enemy.level == level.lower():
            new_enemies.append(enemy)
    return new_enemies

def FilterByGiveStrength(enemyList):
    new_enemies = []

    for enemy in enemyList: 
        if enemy.giveStrength:
            new_enemies.append(enemy)
    return new_enemies

def FilterByTargetHighest(enemyList):
    new_enemies = []

    for enemy in enemyList: 
        if enemy.targetHighest:
            new_enemies.append(enemy)
    return new_enemies

def FilterByTargetLowest(enemyList):
    new_enemies = []

    for enemy in enemyList: 
        if enemy.targetLowest:
            new_enemies.append(enemy)
    return new_enemies

def FilterByGiveDefense(enemyList):
    new_enemies = []

    for enemy in enemyList: 
        if enemy.giveDefense:
            new_enemies.append(enemy)
    return new_enemies


if __name__ == "__main__":
    enemies = enemy_files.GetEnemiesFromFile(enemy_files.GetEnemyFilenames())

    new_enemies = FilterBySingleTarget(enemies)

    for enemy in new_enemies:
        print("---------------------")
        print(enemy)
        print("---------------------")
        print()
    

    

