# DSC 510 - Summer Semester 2020
# Week 9 Programming Assignment 9.1
# Author: Manish Kalkar
# 07/29/2020

import requests
import json


# Function to process API to retrieve Chuck Norris Joke
def process_api():

    # Uses the Request library to make a GET request of the following API
    # Response is stored in r as JSON Response
    r = requests.get("https://api.chucknorris.io/jokes/random")

    # json.loads() returns the python dictionary object.
    data = json.loads(r.text)

    # Parse the JSON data to obtain the “value” key
    # Joke is displayed for the user
    for key, value in data.items():
        if key == "value":
            Joke = value
            print("Here is your joke. Make sure you laugh.:) - {}".format(Joke))
            print("\n")

    # Allow the user to request a Chuck Norris joke again
    main()


def main():

    # Allow the user to request a Chuck Norris joke as many times as they would like
    user_response = input("Would you like to hear Chuck Norris joke? Enter Y and enjoy the joke: ")

    # Converting User Response into lower case to avoid error if user enter lower case value - y
    # Using lower() string function
    user_response = user_response.lower()

    # If user responds with "Y" or "y" then call the function to process the API
    if user_response == "y":
        process_api()
    else:
        quit()


if __name__ == "__main__":
    print("-------------------------------------------------")
    print("Welcome to the Chuck Norris Online Jokes Library")
    print("-------------------------------------------------")
    main()
