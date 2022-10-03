"""
Name: {Marisa Inkaew}
SID: {363411760002}
Group: {MIT431}
"""

class Labtop:
    def __init__(self,brand,model,cpu,ram,display,storage,price):

        self.__brand = brand
        self.__modle = model
        self.__cpu = cpu
        self.__ram = ram
        self.__display = display
        self.__storage = storage
        self.__price = price

    def display_data_Laptop(self):
            print(f'{self.__brand} {self.__modle} {self.__cpu} {self.__ram} {self.__display} {self.__storage} {self.__price}')

            # getter and setter mathods
    def get_brand(self):
        return self.__brand
    def set_brand(self,brand):
        self.__modle = modle
    def get_modle(self):
        return self.__brand
    def set_modle(self,modle):
        self.__modle = modle
    def get_cpu(self):
        return self.__cpu
    def set_cpu(self,cpu):
        self.__cpu = cpu
    def get_ram(self):
        return self.__ram
    def set_ram(self,ram):
        self.__ram = ram
    def get_display(self):
        return self.__display
    def set_display(self,display):
        self.__display = display
    def get_storage(self):
        return self.__storage
    def set_storage(self, storage):
        self.__storage = storage
    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price






