from enemy import Enemy
import json
from os import system, name, path, listdir

ENEMIES_FOLDER = ".\enemies"


def GetEnemyFileName(playerEnemy):
    return ENEMIES_FOLDER + "/" + playerEnemy.level.replace(" ","") + "_" + playerEnemy.name.replace(" ","")


def GetEnemiesFromFile(filenames):
    enemyList = []
    
    for file in filenames:
        f = open(file, "r")
        jsonString = f.read()
        enemyObject = json.loads(jsonString, object_hook= Enemy)
        enemyList.append(enemyObject)
    
    return enemyList

def GetEnemyFilenames():
    return [path.join(ENEMIES_FOLDER, f) for f in listdir(ENEMIES_FOLDER) if path.isfile(path.join(ENEMIES_FOLDER, f))]

def SaveEnemy(playerEnemy):
    file = open(GetEnemyFileName(playerEnemy), "w")
    file.write(json.dumps(playerEnemy.__dict__))
    file.close()