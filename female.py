from human import Human

class Female(Human):

    def __init__(self):
        super().__init__()
        self.testes = False
        self.chromxy = False
        self.special_power = "Speed"


    def golf(self):
        return "nothing better than playing golf "

    def skydiving(self):
        return "what a rush"

    def dance(self):
        return "its fun and also exercise"


# female_object = Female()
#
# print(female_object.skydiving())