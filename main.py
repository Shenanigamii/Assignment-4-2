"""
This program calculates an employee’s productivity bonus and prints the employee’s name and bonus.
"""

# Function to calculate productivity score
def calcProd(transactions, shifts, value):
    if transactions > 0 and shifts > 0:
        prodScore = value / transactions / shifts
        return prodScore
    else:
        return 0

# Function to determine bonus based on productivity score
def detBonus(score):
    if score <= 30:
        return "$50.0"
    elif 31 <= score <= 69:
        return "$75.0"
    elif 70 <= score <= 199:
        return "$100.0"
    else:
        return "$200.0"

# Dictionary of employee names
empNames = {
    1: "Kim Smith",
    2: "Dave Matthews",
    3: "James Patterson",
    4: "Jenna Jenkins"}

# Variables as user inputs
# Employee Names
empNumber = int(input(
    "Enter Employee Number:\n1. Kim Smith\n2. Dave Matthews\n3. James Patterson\n4. Jenna Jenkins\n\nEnter Number 1-4:\n\n "))
empName = empNames.get(empNumber)

while empNumber not in empNames:
    print("Invalid Entry, Try Again.")
    empNumber = int(input(
        "Employee Number?:\n1. Kim Smith\n2. Dave Matthews\n3. James Patterson\n4. Jenna Jenkins\n\nEnter Number 1-4: "))

# Number of shifts
shiftsInput = int(input("Number of Shifts? "))

# Number of Transactions
transInput = int(input("Number of transactions? "))

# Value of transactions
valueInput = float(input("Transaction Dollar Amount? "))

# Calculate productivity score
prodScore = calcProd(transInput, shiftsInput, valueInput)

# Determine bonus based on productivity score
bonus = detBonus(prodScore)

print("Employee Name:", empName)
print("Employee Bonus:", bonus)
