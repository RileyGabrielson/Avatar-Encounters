class Encounter_Param:

    def __init__(self, dict=None):
        self.minDifficulty = 0
        self.maxDifficulty = 15
        self.category = None
        self.generateAttempts = 50

        if dict != None:
            vars(self).update(dict)