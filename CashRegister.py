# DSC 510 - Summer Semester 2020
# Week 10 Programming Assignment 10.1
# Author: Manish Kalkar
# 08/08/2020

import locale

# Set the locale for use in currency formatting
result = locale.setlocale(locale.LC_ALL, '')
if result == 'C':
    locale.setlocale(locale.LC_ALL, 'en_US')


# Define class CashRegister
class CashRegister(object):

    def __init__(self):
        # Initialize the price and the item count
        self.totalPrice = 0
        self.itemCount = 0

    # Instance method called addItem
    def addItem(self, price):
        self.totalPrice = self.totalPrice + float(price)
        self.itemCount = self.itemCount + 1  # keeping track of the number of items in the cart

    # Returns the total price
    def getTotal(self):
        return self.totalPrice

    # Returns the item count
    def getCount(self):
        return self.itemCount


def main():

    # Creating an instance of the CashRegister class
    checkout = CashRegister()

    # Set pickitem flag = True to enter into the loop
    pickitem = True

    # Loop that allows the user to continue to add items to the cart until they request to quit
    while pickitem:

        # Prompt the user to add items to the cart
        collectitems = input("Would you like to add item to the cart? Enter Y or N: ")

        # Converting User Response into upper case to avoid error if user enter lower case value - y or n
        collectitems = collectitems.upper()

        if collectitems == "Y":

            # Allow user to enter price of the item
            price = input("Please enter the price of the item: ")

            # Add the item in the cart
            checkout.addItem(price)

        else:

            # Get the final item count in the cart
            itemcount = checkout.getCount()

            # Get the total price formatted as currency
            amount = checkout.getTotal()
            amount = locale.currency(amount, grouping=True)

            # Format and display the result
            print("--------------------------------------")
            print("Total number of items in the cart: {}".format(itemcount))
            print("Total $ amount of the cart: {}".format(amount))

            # Set pickitem flag = False for user to Quit
            pickitem = False


if __name__ == "__main__":
    print("--------------------------------------------")
    print("Welcome to the Online Cash Register System")
    print("--------------------------------------------")
    main()
