from female import Female
class Girl(Female):
    def __init__(self):
        super().__init__()
        self.can_run = True
        self.defence = True
        self.can_see = True


    def hide_and_seek(self):
        return "its a fun game"

    def fly(self):
        return "yes its unbelievable"

    def sing(self):
        return "la la la laaaa"


# girl_object = Girl()
#
# print(girl_object.sing())