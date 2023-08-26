# DSC 510 - Summer Semester 2020
# Week 7 Programming Assignment 7.1
# Author: Manish Kalkar
# 07/17/2020
import string


# work to be done to process each line
def processline(line, d):

    # Remove the leading spaces and newline character
    line = line.strip()

    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()

    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))

    # Split the line into words
    words = line.split(" ")

    # Iterate over each word in line by calling addword function
    for word in words:
        addword(word, d)


# Add each word to the dictionary. Parameters are the word and a dictionary. No return value.
def addword(word, d):

    # Check if the word is already in dictionary
    if word != "":
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1


# the printing function
def prettyprint(d):

    # Calculate and print the total words
    print("Length of the dictionary:", len(d))

    # Output the number of occurrences of each word in the file
    print("Word" + "          " + "Count")
    print("--------------------")

    # sort from high to low frequency
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

    # print(d)
    for key in d:
        print("{dickey:<15} {dictvalue}".format(dickey=key, dictvalue=d[key]))


def main():

    # open the .txt file - gettysburg.txt
    gba_file = open("gettysburg.txt", "r")

    # Create an empty dictionary
    d = dict()

    # Loop through each line of the file by calling processline function
    for line in gba_file:
        processline(line, d)

    # Print the contents of dictionary
    prettyprint(d)


if __name__ == "__main__":
    print("-----------------------------------")
    print("Program will read the text file gettysburg.txt")
    print("Program will Calculate the total words, and output the number of occurrences of each word in the file")
    print("-----------------------------------")
    main()
