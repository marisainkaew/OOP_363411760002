"""
Name: {Marisa Inkaew}
SID: {363411760002}
Group: {MIT431}
"""

class Labtop:
    # class attribute
    labtop = []
    def __init__(self,number,brand,price,RAM):
        # object attributes
        self.number = number
        self.brand = brand
        self.price = price
        self.RAM = RAM
    def __str__(self):
        print(f'My number is {self.number}, I am Labtop in {self.brand}I am Labtop in {self.price}I am Labtop in {self.RAM}')

# create object
s1 = Labtop("1","ASUS","27990","8")
s2 = Labtop("2","Lenovo","25990","8")
s3 = Labtop("3","Acer","33990","8")

print(s1.number,s1.brand,s1.price,s1.RAM)
print(s2.number,s2.brand,s2.price,s2.RAM)
print(s3.number,s3.brand,s3.price,s3.RAM)


