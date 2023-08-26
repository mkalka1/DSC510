# DSC 510 - Summer Semester 2020
# Week 2 Programming Assignment 2.1
# Author: Manish Kalkar
# 06/11/2020

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

# Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87
InstallationCost = total_feet * 0.87

# Print a receipt for the user
print('______________________________________________________________________________')
print('                                  RECEIPT')
print('                              ' + CompanyName)
print('Item No.' + "    " + 'Item Description' + '    ' + 'Total Feet' + '    ' + 'Unit Price' + '    ' + 'Installation Cost')
print('1001        Fiber Optic Cable      ' + str(total_feet) + '          $0.87           $' + str(InstallationCost))
print('                                                                              ')
print('                             Total Cost: $' + str(InstallationCost))
print('______________________________________________________________________________')
