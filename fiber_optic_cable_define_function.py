# DSC 510 - Summer Semester 2020
# Week 4 Programming Assignment 4.1
# Author: Manish Kalkar
# 06/23/2020

# Retrieve Name of the User
UserName = input('Name: ')

# Display a welcome message for the user
print('Welcome ' + UserName)

# Retrieve the company name from the user
CompanyName = input("Company Name: ")

# Retrieve the number of feet of fiber optic cable to be installed from the user
total_feet = input("Total No. of feet: ")

# Convert total no. of feet into float
total_feet = float(total_feet)

# Store Default Unit Price of 0.87 into the variable
DefaultUnitPrice = 0.87


# Define the function that performs the calculation and return the calculated cost
def cost_calculation(feet, price):
    calculated_cost = feet * price
    return calculated_cost


# Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87
# Apply conditional if statements per the requirement
if 100.00 < total_feet <= 250:
    UnitPrice = 0.80
    InstallationCost = cost_calculation(total_feet, UnitPrice)  # Calling the function
elif 250.00 < total_feet <= 500:
    UnitPrice = 0.70
    InstallationCost = cost_calculation(total_feet, UnitPrice)  # Calling the function
elif total_feet > 500.00:
    UnitPrice = 0.50
    InstallationCost = cost_calculation(total_feet, UnitPrice)  # Calling the function
else:
    InstallationCost = cost_calculation(total_feet, DefaultUnitPrice)  # Calling the function
    UnitPrice = DefaultUnitPrice

# round the InstallationCost float value to 2 decimals
InstallationCost = round(InstallationCost, 2)

# Print a receipt for the user
print('______________________________________________________________________________')
print('                                  RECEIPT')
print('                              ' + CompanyName)
print('Item No.' + "    " + 'Item Description' + '    ' + 'Total Feet' + '    ' + 'Unit Price' + '    ' + 'Installation Cost')
print('1001        Fiber Optic Cable      ' + str(total_feet) + '          $' + str(UnitPrice) + '           $' + str(InstallationCost))
print('                                                                              ')
print('                             Total Cost: $' + str(InstallationCost))
print('______________________________________________________________________________')
