## inputs we need from the user
# Total rent
# Total food ordered for snacking/
# electricity unit spend
# Charge per unit
# persong living in room/flat

# output
# Total amount you've to pay is

rent = int(input("Enter the Total rent of room/flat = "))
food = int(input("Enter the amount of food ordered = "))
electricity_unit = int(input("Enter the total of electricity spend = "))
charge_per_unit = float(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room = "))

total_bill = electricity_unit * charge_per_unit

Output = (rent + food + total_bill) // persons

print("Each person will pay : ", Output)