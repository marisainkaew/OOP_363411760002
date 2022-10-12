from Laptop import Laptop
"""
1.เพิ่มข้อมูล  Laptop
2.แสดงข้อมูล Laptop
3.ออกจากระบบ
"""
def input_laptop_data():
    number = input("Enter your laptop number: ")
    brand = int(input("Enter your  brand: "))
    price = input("Enter your  price: ")

    laptop_list.append(Laptop(number,brand,price))

def display_laptop():
    if len(laptop_list) ==0:
        print("You had no laptop data.")
    else:
        print(f"Your had {len(laptop_list)}) following: ")
        for x in laptop_list:
            x.display_info()
def display_option():
    print("Welcome,data store system---")
    print("1.add laptop data.")
    print("2.display laptop data.")
    print("3.exit.")

    select = int(input("select(1-3)?"))
    if select ==1:
        input_laptop_data()
    elif select ==2:
        display_laptop()
    elif  select ==3:
        print("Good Bey.")
        exit(0)
    else:
        print("Please, enter 1-3 only. Thank.\n")

laptop_list = []
s=0
while s ==0:
    display_option()


