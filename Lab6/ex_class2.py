"""
Name: {Marisa Inkaew}
SID: {363411760002}
Group: {MIT431}
"""

class MyPet:
    # class attribute
    mypet = []
    def __init__(self,name,age,breed):
        # object attributes
        self.name = name
        self.age = age
        self.breed = breed
        self.mypet.append(self)

    def display_info(self):
        print(f'Name: {self.name} Age: {self.age} Breed: {self.breed}')

    def display_all_mypet(self):
        if len(self.mypet) ==0:
            print("You had no pet.")
        else:
            for x in self.mypet:
                x.display_info()