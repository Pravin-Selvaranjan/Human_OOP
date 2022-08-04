# HUMAN OOP PROJECT

## In this project, we will be utilising the OOP method in order to create some functions

### **_Keywords_**

```class``` - This creates a class ie ```class nameofclass:```

```def``` - This creates a function ie ```def funciton.(self):```

```try``` - This is used as exception tool ie ```try return except:```

```return``` - This specifies what is returned from a function as above



# Step 1 - Create the Human class

- Using the functions above you can complete all of the below, we are creating the PARENT CLASS
- syntax ----class name: <-----This is how it should be formatted

```
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
```

# Step 2 - Creating the Male/Female classes 

- Here, we inherit everything created in the last step (Human)
- This is done using ```super().```
- Remember to specify ```from _____ import _____```
```
from human import Human

class Male(Human):   # write the name of the parent class in order to inherit!!

    def __init__(self):
        super().__init__() #used to inherit everything from the base class!!
        self.testes = True
        self.chromxy = True
        self.special_power = ("speed")



    def work(self):
        return "gotta make a living!"
    def play_games(self):
        return "gotta have fun!"
    def drive(self):
        return "gotta get away from the mrs!!"


male_object = Male()
```
```
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
```

# Step 3 - Creating further classes using the above code as the basis 

- Male -> Boy
- Female -> Girl

from male import Male
class Boy(Male):
```
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

print(boy_object.play_games())
```
```
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


girl_object = Girl()

print(girl_object.sing())
```

# Abstraction

Objects only reveal internal mechanisms that are relevant for the use of other objects, hiding any unnecessary implementation code.

The below screenshot shows an example of how Abstraction was used within the above code
The user does not see the implementation behind ```.move```

(image)








# Inheritence 

Classes can reuse code from other classes.

The below screenshot shows an example of inheritence.
Simply using a previous class to attribute to the current creation.

(image)








# Encapsulation 
This principle states that all important information is contained inside an object and only select information is exposed.


The below screenshot shows an example of Encapsulation.
The ```_number_of_fights``` function will return "information redacted to the user"
By using ```__record``` this info becomes private

(image)










# Polymorphism 
Objects are designed to share behaviors and they can take on more than one form. 


The below screenshot shows an example of Polymorphism
The first one shows  ```def play_games(self): return "gotta have fun!"``` but the same function is used within the male class with a different output


(image)

(image)



