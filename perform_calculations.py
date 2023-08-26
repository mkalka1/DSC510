# DSC 510 - Summer Semester 2020
# Week 5 Programming Assignment 5.1
# Author: Manish Kalkar
# 07/03/2020


# Define the function that performs the calculation and print the outcome of the mathematical operation
def performcalculation(operation):
    firstnumber = input("Please enter first number: ")

    # Check if user has entered first number
    if firstnumber == "":
        firstnumber = input("Please enter first number again: ")  # Request user to enter value again
    else:
        firstnumber = float(firstnumber)

    if firstnumber == "":
        firstnumber = "0"  # If user still choose not to enter any value, default the value to 0
        firstnumber = float(firstnumber)
    else:
        firstnumber = float(firstnumber)

    secondnumber = input("Please enter second number: ")

    # Check if user has entered second number
    if secondnumber == "":
        secondnumber = input("Please enter second number again: ")  # Request user to enter value again
    else:
        secondnumber = float(secondnumber)

    if secondnumber == "":
        secondnumber = "0"  # If user still choose not to enter any value, default the value to 0
        secondnumber = float(secondnumber)
    else:
        secondnumber = float(secondnumber)

    # Check for the operation and perform the calculation
    if operation == 1:  # Addition
        calculatedvalue = firstnumber + secondnumber
        printcalculation("+", firstnumber, secondnumber, calculatedvalue)  # call the print function
    elif operation == 2:  # Subtraction
        calculatedvalue = firstnumber - secondnumber
        printcalculation("-", firstnumber, secondnumber, calculatedvalue)  # call the print function
    elif operation == 3:  # Multiplication
        calculatedvalue = firstnumber * secondnumber
        printcalculation("*", firstnumber, secondnumber, calculatedvalue)  # call the print function
    elif operation == 4:  # Division

        if secondnumber == 0.0:  # if user miss entering second number or enter 0
            print("Invalid second number. Second number can not be 0 or empty for division")
            quit()
        else:
            pass

        calculatedvalue = firstnumber / secondnumber
        printcalculation("/", firstnumber, secondnumber, calculatedvalue)  # call the print function


# Define the function to print calculated value for each Mathematical Operation
def printcalculation(ops, numberone, numbertwo, calculatedvaluetoprint):
    calculatedvaluetoprint = round(calculatedvaluetoprint, 2)  # Round the calculated value to two decimals
    print(numberone, ops, numbertwo, "=", calculatedvaluetoprint)


# Define the function that print the calculated average
def calculateaverage():
    sumforavg = 0
    totalnumbers = input("How many numbers you wish to enter for calculating the average?: ")
    totalnumbers = int(totalnumbers)
    for number in range(0, totalnumbers, 1):
        number = input("Enter number: ")
        number = float(number)
        sumforavg = sumforavg + number

    average = sumforavg / totalnumbers
    average = round(average, 2)  # Round the average value to two decimals
    print("Average = ", average)


# main function that is used to allow the user to run the program
def main():
    mathoperation = input("Enter 1 to Add, 2 to Subtract, 3 to Multiply, 4 to Divide, or 5 for Average 1: ")

    if mathoperation == "":  # if user miss entering the option to perform mathematical operation
        print("Invalid option for mathematical operation")
        quit()
    else:
        pass

    mathoperation = int(mathoperation)

    while mathoperation in range(1, 6):

        if mathoperation == 5:
            calculateaverage()
            break
        else:
            performcalculation(mathoperation)
            break
    else:
        print("Invalid option for mathematical operation")


if __name__ == "__main__":
    print("The program will perform various math operations")
    print("Would you like to add, subtract, multiply, divide, or calculate Average?")
    main()
