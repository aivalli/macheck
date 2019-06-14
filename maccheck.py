#!/usr/bin/env python3

import os
import sys
import requests


## Let us do the prequsites first.


# Let us check the key
key = os.environ["key"]


# we shall accept only one argument 

if len(sys.argv) == 2:
    # we stitch the URL first
    url = 'https://api.macaddress.io/v1?apiKey=' + key + '&output=json&search=' + sys.argv[1].lower()
    print(url)
    # We try to "curl" using python
    response = requests.get(url)
    print(response.content)
    

else:
    print("This script takes one MAC address as an argument!")
    exit(1)
