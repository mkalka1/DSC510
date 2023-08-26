# DSC 510 - Summer Semester 2020
# Week 9 Web Services Example
# Author: Manish Kalkar
# 07/28/2020

# Import the modules
import requests
import json

# Get the feed
r = requests.get("http://chroniclingamerica.loc.gov/search/pages/results/?format=json&proxtext=fire")
r.text

# Convert it to a Python dictionary
data = json.loads(r.text)

# Loop through the result
for item in data:
    print(item)


