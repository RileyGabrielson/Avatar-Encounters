from enemy import Enemy

def getDifficulty(enemy):
    if not isinstance(enemy, Enemy):
        raise ValueError("enemy must be an Enemy object")

    difficulty = 0.0
    if enemy.singleTarget:
        difficulty += float(enemy.damage) / 4
    else:
        difficulty += enemy.damage
    difficulty += enemy.health / 5
    difficulty += enemy.defense * 1.4
    difficulty += enemy.reflect * 2.4
    difficulty += enemy.pierce * 2
    difficulty += (enemy.burn + enemy.stun + enemy.fatigue + enemy.loseCoin) * 0.66

    return difficulty