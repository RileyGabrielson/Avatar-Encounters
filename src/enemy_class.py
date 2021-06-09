
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

        self.singleTarget = False
        self.giveStrength = False
        self.targetHighest = False
        self.targetLowest = False
        self.giveDefense = False

        self.giveDefenseAmount = 0

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

        if self.singleTarget:
            string += "\n" + "Single Target"
            if self.targetHighest:
                string +=  ": Highest Health"
            if self.targetLowest:
                string +=  ": Lowest Health"
        
        if self.giveStrength:
            string += "\n" + "Gives Strength to Other Enemies"

        if self.giveDefense:
            string += "\n" + "Gives " + str(self.giveDefenseAmount) + " Defense to Other Enemies"

        return string

    

























