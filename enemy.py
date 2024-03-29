
class Enemy:

    def __init__(self, dict=None):        
        self.name = ""
        self.category = ""
        self.level = ""

        self.health = 0
        self.damage = 0
        self.defense = 0
        self.pierce = 0
        self.reflect = 0

        self.burn = 0
        self.stun = 0
        self.fatigue = 0
        self.loseCoin = 0

        self.singleTarget = False
        self.targetHighest = False
        self.targetLowest = False

        self.other = ""

        if dict != None:
            vars(self).update(dict)

    def __str__(self):
        string = self.name + ": " + self.level.title() + " (" + self.category.title() + ")"
        string += "\n" + "Health: " + str(self.health)
        string += "\n" + "Damage: " + str(self.damage)
        string += "\n" + "Defense: " + str(self.defense)
        if(self.pierce > 0):
            string += "\n" + "Pierce: " + str(self.pierce)
        if(self.reflect > 0):
            string += "\n" + "Reflect: " + str(self.reflect)

        if(self.burn > 0):
            string += "\n" + "Burn: " + str(self.burn)
        if(self.stun > 0):
            string += "\n" + "Stun: " + str(self.stun)
        if(self.fatigue > 0):
            string += "\n" + "Fatigue: " + str(self.fatigue)
        if(self.loseCoin > 0):
            string += "\n" + "Lose Coin: " + str(self.loseCoin)
        
        if self.singleTarget:
            string += "\n" + "Single Target"
            if self.targetHighest:
                string +=  ": Highest Health"
            if self.targetLowest:
                string +=  ": Lowest Health"

        if self.other != "":
            string += "\n" + "Other: " + self.other

        return string

    

























