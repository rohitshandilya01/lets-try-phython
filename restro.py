"""
1st greet
2 menu show karega
3 select your food item
4 check is it available or not if availebale 

"""




# restaurant menu is listed in menu
menu = {
    'chiken':100,
    'pizza' : 70,
    'roti': 12,
    'salad' : 50,
    'panner': 130,
    }

#greets
print("Welcome to My Raju Yadav Restaurant")
print("What would you like to order Today! ")

#display items
for i,j in menu.items():
    print(f"{i} : {j}")




item_1 = input("Select Your First item : ")

total_order = 0

if item_1 in menu:
    total_order += menu[item_1]
    if item_1 in menu:

        print(f"{item_1} added to cart")
    else:
        print("Sorry Your choise is not available Yet! ")

    
        

item_2 = input("Please Select another item = ")       

total_order += menu[item_2]
print(f"{item_2} added to cart")

yesorno=print("would You like to order more or End order")
print("Yes or NO")
yes = 1
no = 0
check = input("")

if check is yes:
    print("let restart")
else:
    print(f"Total Bill is to be pay is : {total_order}")    
   


