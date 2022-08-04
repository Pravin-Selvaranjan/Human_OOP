from human import Human

class Male(Human):   #write the name of the parent class in order to inherit!!


    def __init__(self):
        super().__init__() #used to inherit everything from the base class!!
        self.testes = True
        self.chromxy = True
        self.special_power = ("speed")



    def work(self):
        return "gotta make a living!"
    def play_games(self):
        return "gotta play Warzone!"
    def drive(self):
        return "gotta get away from the mrs!!"



male_object = Male()

