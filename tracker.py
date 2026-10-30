# Expense Tracker - Installment 4
# Mikael Santino T. Pineda 

print("========================================")
print("            EXPENSE TRACKER")
print("        Know where your money goes.")
print("========================================")
print()
print("MAIN MENU")
print("  [1] Add an expense            (coming soon)")
print("  [2] View all expenses         (coming soon)")
print("  [3] Show total spent          (coming soon)")
print("  [4] Exit                      (coming soon)")
print()

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")
print()

subtotal = 0.0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")
subtotal += amount2

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

over_budget = total > budget
left = budget - total
amount_diff = abs(left)

print()
print("----------------------------------------")
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent:.1f}%):\t${tax}")
print(f"Grand total:\t${total}")

if over_budget:
    print(f"Over budget by ${amount_diff}!")
elif total > (0.90 * budget):
    print(f"Careful: only ${amount_diff} left.")
else:
    print(f"Within budget. ${amount_diff} left.")

print("----------------------------------------")
print("Made by: Mikael Santino T. Pineda  |  Installment 4")