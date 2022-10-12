"""
Name: {Marisa Inkaew}
SID: {363411760002}
Group: {MIT431}
"""

class Person:
    def __init__(self,id,name):
        self.__id = id # private member
        self.__name = name
        self._nation = "Thai" # protectede member
    # getter and serter mathod
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def person_info(self):
        print(f'I am Person ID: {self.__name} Name: {self.__name} Nantion: {self._nation}')
class Student(Person):
    def __init__(self,id,name,uni):
        self.uni = uni
        Person.__init__(self,id,name)
    def student_info(self):
        print(f'I am student, ID: {self.get_id()}, Name: {self.get_name()}, Nation: {self._nation} University: {self.uni}')

# create abject
std = Student("001","Marisa Inkaew","RUTS")
print(std.get_id())
print(std.get_name())

p = Person("002","Parichat Sakkuna")
print(p.get_id())
print(p.get_name())


std.student_info()
p.person_info()