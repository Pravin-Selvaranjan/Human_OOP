from male import Male
class Boy(Male):

    def __init__(self):
        super().__init__()
        self.blue_hair = True
        self.webbed_feet = True
        self.short_arms = True

    def play_tag(self):
        return "Its fun to run around"

    def cry(self):
        return "everyone needs a cry once in a while"
    def fight(self):
        return "boys will be boys"
    def play_games(self):
        return "gotta have fun!"

    def _number_of_fights(self):
        try:
            return boy_object.__record()
        except AttributeError:
            return "Information redacted"


boy_object = Boy()

print(boy_object._number_of_fights())