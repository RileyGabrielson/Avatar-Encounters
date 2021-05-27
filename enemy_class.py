#List of all the Enemy Classes
#Separated by fire nation, creatures, pirates, ect. 

class Enemy:

    def __init__(self, ):
        self.name = ""
        self.category = ""
        self.level = ""

        self.health = 0
        self.damage = 0
        self.defense = 0
        self.pierce = 0

        self.singleTarget = False
        self.giveStrength = False
        self.targetHighest = False
        self.targetLowest = False

    def __str__(self):
        string = self.name + ": " + self.level + " (" + self.category + ")"
        string += "\n" + "Health: " + str(self.health)
        string += "\n" + "Damage: " + str(self.damage)
        string += "\n" + "Defense: " + str(self.defense)
        string += "\n" + "Pierce: " + str(self.pierce)

        if self.singleTarget:
            string += "\n" + "Single Target"
            if self.targetHighest:
                string +=  ": Highest Health"
            if self.targetLowest:
                string +=  ": Lowest Health"
        
        if self.giveStrength:
            string += "\n" + "Gives Strength to Allies"

        return string

    
























