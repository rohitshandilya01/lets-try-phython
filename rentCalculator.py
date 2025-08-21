# variable

# rent
#food ordered
#Electricity
#travelling
#other

print("Hello Rohit i am Rent Calculator I split monthly Expense for Easy Payment")

rent = int(input("Enter Your Total rent : "))
food = int(input("Enter your food expence : "))
travelling = int(input("Enter your tavelling expence : "))

electricity_unit = 8

electricity = int(input("Enter no. of Electricty unit used "))

total_electricity = electricity_unit * electricity

total = rent + food + travelling + total_electricity

print(f"Total Expense of this Month is {total}")

members = int(input("Enter no. of member to split bill : "))

finalBill = total / members
print(f"per head {finalBill}")