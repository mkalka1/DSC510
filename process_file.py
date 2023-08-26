# DSC 510 - Summer Semester 2020
# Week 8 Programming Assignment 8.1
# Author: Manish Kalkar
# 07/22/2020

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


# the file processing function
def processfile(d, outputfile):

    # sort from high to low frequency
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

    # open the file to append
    filehandle = open(outputfile, 'a')
    filehandle.write("\n" + "Word" + "          " + "Count" + "\n")
    filehandle.write("--------------------" + "\n")

    # append the dictionary (d) into the file
    for key in d:
        dline = "{dickey:<15} {dictvalue}".format(dickey=key, dictvalue=d[key])
        filehandle.write(str(dline) + "\n")

    #  explicitly close the file handle
    filehandle.close()


def main():

    # open the .txt file - gettysburg.txt
    gba_file = open("gettysburg.txt", "r")

    # Create an empty dictionary
    d = dict()

    # Loop through each line of the file by calling processline function
    for line in gba_file:
        processline(line, d)

    # Prompt the user for the filename they wish to use to generate the report
    outputfilename = input("Please enter Output File Name: ")

    # Use the filename specified by the user to write the file
    outputfilename = outputfilename + ".txt"

    # Calculate and store the total number of words
    totalwords = "Length of the dictionary: {} ".format(len(d))

    # open the file to write the length of the dictionary
    with open(outputfilename, 'w') as fileHandle:
        fileHandle.write(str(totalwords))

    # call function processfile to write the contents of dictionary into the output file
    processfile(d, outputfilename)

    # once file is processed, notify user that output file has been generated successfully
    print("The output file {} has been generated successfully.".format(outputfilename))


if __name__ == "__main__":
    print("-----------------------------------")
    print("Program will read the text file gettysburg.txt")
    print("Program will Calculate the total words, and output the number of occurrences of each word in the file")
    print("Program will then write the output in the output file")
    print("-----------------------------------")
    main()
