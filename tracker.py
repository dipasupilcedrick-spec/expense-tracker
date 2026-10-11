
# Expense Tracker - Installment 3: Tracker do the math
# Author: John Cedrick D. Dipasupil
# Calculates expenses, tax, and the remaining budget.

print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nWelcome! This is your personal expense tracker.\n")

print("MAIN MENU")
print("\t[1] Add an expense\t(coming soon)")
print("\t[2] View all expenses\t(coming soon)")
print("\t[3] Show total spent\t(coming soon)")
print("\t[4] Exit\t\t(coming soon)")


name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

subtotal = 0

item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

average = subtotal / 2

tax_percent = int(input("\nEnter tax rate %:"))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

budget = float(input("Enter your budget: "))
over_budget = total > budget
remaining_budget = budget - total

print()
print("-" * 40)
print("SUMMARY")
print(f"\t- {item1}:\t${amount1}")
print(f"\t- {item2}:\t${amount2}")
print(f"Subtotal:\t\t${subtotal}")
print(f"Average:\t\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Total:\t\t\t${total}")
print(f"Remaining Budget:\t${remaining_budget}")
print("-" * 40)

print("Made by: John Cedrick D. Dipasupil  |  Installment 3")
print("=" * 40)
