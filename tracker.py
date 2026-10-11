
# Expense Tracker - Installment 2: Talking to the User
# Author: John Cedrick D. Dipasupil
# An expense tracker that asks for two expenses and calculates the total and average.

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

item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
print(f"\t- {item1}:\t${amount1}")
print(f"\t- {item2}:\t${amount2}")
print(f"Total spent:\t\t${total}")
print(f"Average:\t\t${average}")
print("-" * 40)

print("Made by: John Cedrick D. Dipasupil  |  Installment 2")
print("=" * 40)
