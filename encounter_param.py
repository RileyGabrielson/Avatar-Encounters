class Encounter_Param:

    def __init__(self, dict=None):        
        self.maxHealth = None
        self.maxDamage = None
        self.maxDefense = None

        if dict != None:
            vars(self).update(dict)