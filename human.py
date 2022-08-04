# create a Human class
# syntax class name:

class Human:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True



    def sleep(self):
        return "sleep is vital to the survival of the human species"

    def eat(self):
        return "eating is vital to the survival of the human species"

    def move(self):
        return "exercise is vital to the survival of the human species"


John = Human()

print(John.move())