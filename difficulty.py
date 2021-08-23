from enemy import Enemy

def getDifficulty(enemy):
    if not isinstance(enemy, Enemy):
        raise ValueError("enemy must be an Enemy object")

    difficulty = enemy.damage
    difficulty += enemy.health / 5
    difficulty += enemy.defense
    difficulty += enemy.reflect * 2
    difficulty += enemy.pierce * 2
    difficulty += (enemy.burn + enemy.stun + enemy.fatigue + enemy.loseCoin) * 0.66

    return difficulty