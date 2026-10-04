# Expense Tracker - Installment 2 
# Mikael Santino T. Pineda 

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nWelcome! This is your personal expense tracker.\n")

print("MAIN MENU")
print("\t[1] Add an expense" + " " * 12 + "(coming soon)")
print("\t[2] View all expenses" + " " * 9 + "(coming soon)")
print("\t[3] Show total spent" + " " * 10 + "(coming soon)")
print("\t[4] Exit" + " " * 22 + "(coming soon)")
name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")
print("-" * 40)
print("Made by: Mikael Santino Pineda  |  Installment 2")