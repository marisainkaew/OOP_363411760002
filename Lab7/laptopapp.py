from exercise_lab7 import Labtop

def display_laptop():
    if len(my_laptop) ==0:
        print("\nYou had no laptop data.\n")
    else:
        num = 1
        print(f"Your had {len(my_laptop)}) following: ")
        for x in my_laptop:
            print(f'{num}. ',end="")
            x.display_data_Laptop()
            num +=1
        print("\n")

def display_option():
    print("Welcome to Laptop Data store system (LDSS)")
    print("1.add Laptop")
    print("2.display all Laptop")
    print("3.delete")
    print("4.Edit Labtop")
    print("5.exit")
    select = int(input("select(1-5)? : "))
    if select ==1:
        input_laptop_data()
    elif select ==2:
        display_laptop()
    elif select ==3:
        delete_labtop()
    elif select ==4:
        edit_labtop_price()
    elif  select ==5:
        print("Good Bey.")
        exit(0)
    else:
        print("Please, select number 1-5.")


# edit data
def edit_labtop_price():
    display_laptop()
    # length of my_labtop
    n = len(my_laptop)
    s = 1
    while s:
        s = int(input(f"select 1-{n} or type 0 to main option: "))
        if s in range(1, n + 1):
            print(f"current price: {my_laptop[s-1].get_price()}")
            newprice = float(input("enter new price: "))
            my_laptop[s-1].set_price((newprice))
            print("\nAlrady updated labtop data.\n")
            break
        elif s == 0:
            print(f"please,enter number 1-{n} or type 0 to main option: ")
        else:
            print(f"Please")

#delete data
def delete_labtop():
    display_laptop()
    # length of my_labtop
    n = len(my_laptop)
    s =1
    while s:
        s = int(input(f"select 1-{n} or type 0 to main option: "))
        if s in range(1,n+1):
            my_laptop.pop(s-1)
            print("\nAlrady deleted labtop data.\n")
            break
        elif s == 0:
            print(f"please,enter number 1-{n} or type 0 to main option: ")
        else:
            print(f"Please")
# input data
def input_laptop_data():
    brand = input("Enter laptop brand: ")
    model = input("Enter laptop model: ")
    cpu = input("Enter laptop cpu: ")
    ram = int(input("Enter laptop ram: "))
    display = float(input("Enter laptop display: "))
    price = float(input("Enter laptop price: "))

    my_laptop.append(Laptop(brand,model,cpu,ram,display,storage,price))

    print("\n----------------------------------")
    print("Already add Laptop to store.")
    print("\n----------------------------------")


my_laptop = []
my_laptop.append(Labtop("ASUS","Vivobook","Intel Core i5-12500H",8,15.6,512,27990))
my_laptop.append(Labtop("Lenovo","Ldeapad gaming 3","Intel Core i5-11320H",8,15.6,512,25990))

s = 0
while s == 0:
    display_option()