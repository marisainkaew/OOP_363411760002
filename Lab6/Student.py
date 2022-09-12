"""
Name: {Marisa Inkaew}
SID: {363411760002}
Group: {MIT431}
"""

class Student:
    # class attribute
    Student = []
    def __init__(self,name,age,class):
        # object attributes
        self.name = name
        self.age = age
        self.class = class
        self.Student.append(self)


