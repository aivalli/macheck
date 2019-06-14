# macheck
Just an automated way to check the mac 




# (simple) Usage

1. This script requires a token, please generate one at https://macaddress.io/ .
2. Store it in file ~/.macaddress_token
3. Export it to a variable called key. See actual running reference later below.
3. This script may not be as intelligent in addressing a totally random MAC address. Therefore, ambiguity may creep in. I have tried to handle a "blank response" as I tried to check with a random address generator.
4. Run export PYTHONWARNINGS="ignore:Unverified HTTPS request" && export key=`cat ~/.macaddress_token` && ./maccheck.py [mac_address]. This should return another JSON value as the requirements mentions reusablity to be maintained.


# Key setup & running the script

1. export PYTHONWARNINGS="ignore:Unverified HTTPS request" && export key=`~/.macaddress_token` && chmod -v u+x ./macheck.py && ./macheck.py
2. If all has gone well then it should exit asking for an argument comprised of a mac address.
3. This time run ./macheck.py [mac address]

Ex: export key=`cat ~/.macaddress_token` && ./maccheck.py

Security notes:

1. One more step of security could be that we make the image dump available instead of the regular way of installing the docker image. 
2. Neglect of SSL is supressed with export PYTHONWARNINGS="ignore:Unverified HTTPS request".

# example of a query - how it should look like:

~ $ export PYTHONWARNINGS="ignore:Unverified HTTPS request" && export key=`cat ~/.macaddress_token` && ./maccheck.py 00:50:56:C0:00:01
{'companyname': 'VMware, Inc'}
~ $

# Programmer notes, ignorable if you are the end user!

Modules used:

sys
bs4 - BeautifulSoup
requests
json
os

