"""
Name: {Marisa Inkaew}
SID: {363411760002}
Group: {MIT431}
"""

# encapsulation

class Student:
    def __init__(self,id,name,major):
        self.__id = id # PRIVATE MEMBER
        self.name = name
        self.major = major
    def display_data_object(self):
        print(f'{self.__id} {self.name} {self.major}')

    # getter and setter mathods
    def get_id(selfs):
        return selfs.__id
    def set_id(selfs,newid):
        selfs.__id = newid



# outside class]
std = Student("001","Marisa Inkaew","MIT431")

# display data of attributes
#print(std.id,std.name,std.major)

# access to private method
# 1.use puplic method
std.display_data_object()
# 2.name mangling -->object._Classname__attributes
print(std._Student__id)

std._Student__id = "002"
print(std._Student__id)


# use getter and setter mathods
print(std.get_id())

std.set_id("003")
std.display_data_object()
