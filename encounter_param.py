class Encounter_Param:

    def __init__(self, dict=None):        
        self.minDifficulty = None
        self.maxDifficulty = None

        if dict != None:
            vars(self).update(dict)