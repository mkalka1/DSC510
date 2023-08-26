# DSC 510 - Summer Semester 2020
# Week 6 Programming Assignment 6.1
# Author: Manish Kalkar
# 07/06/2020


# Define the function that print the following using lists:
# Number of temperature recordings, Largest temperature, Smallest temperature
def listtemperatures():

    temperatures = []  # Creating an empty list called temperatures
    temperature = ""
    maximumtemperature = 0
    minimumtemperature = 0
    temperaturereadings = 0

    # Allowing the user to input a series of temperatures
    # Sentinel value - Quit will stop the user input
    while temperature != "Quit":
        temperature = input("Enter temperature: ")
        if temperature != "Quit":
            temperature = int(temperature)
            temperatures.append(temperature)  # adding elements into the list
        else:
            maximumtemperature = max(temperatures)  # recording maximum temperature
            minimumtemperature = min(temperatures)  # recording minimum temperature
            temperaturereadings = len(temperatures)  # recording total number of temperature readings

    print("Largest temperature recorded:", maximumtemperature)
    print("Smallest temperature recorded:", minimumtemperature)
    print("There are total", temperaturereadings, "temperature readings in the list")
    print("The temperatures recorded in the list are " + ", ".join(map(str, temperatures)))


# main function that is used to allow the user to run the program
def main():

    listtemperatures()


if __name__ == "__main__":
    print("-----------------------------------")
    print("INSTRUCTIONS")
    print("Program will determine - number of temperatures, largest temperature, smallest temperature using lists.")
    print("Please enter temperature as numeric value")
    print('Enter "Quit" to stop entering the temperatures')
    print("-----------------------------------")
    main()
