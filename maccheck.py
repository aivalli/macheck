#!/usr/bin/env python3

import os
import sys
import requests
from bs4 import BeautifulSoup
import json

## Let us do the prequsites first.


# Let us check the key
key = os.environ["key"]
if key == '':
    print("Read the README and set your key as described.")
    exit(1)

# we shall accept only one argument 

if len(sys.argv) == 2:
    url = 'https://api.macaddress.io/v1?apiKey=' + key + '&output=json&search=' + sys.argv[1].lower()
    response = requests.get(url)

    # We shall try to  use beautiful soup for parsing the response. We wont be verifying the SSL part
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, "html.parser")
    value = json.loads(str(soup))
    if value['vendorDetails']['companyName'] == '':
        print("The mac address seems to be invalid, please check and try again!")
        exit(1)
    jvalues = value['vendorDetails']['companyName']
    # print in JSON so that the print value can be reused.
    print(dict([("companyname", jvalues)]))

else:
    print("This script takes one MAC address as an argument!")
    exit(1)
