#!/usr/bin/env python

import re

regex = r"(\w+(\.?\w+)*(\w+)?)\+?\w*@(\w+(\.?\w+?)*\.\D{2,3})"

def emailCheck (email):
    if re.search(regex, email):
        match = re.search(regex, email)
        print "Congrats! Your email checks out."
        print "Your username is %s, and your domain is %s" % (match.group(1), match.group(4))
    else:
        print "Please, enter a valid email."

email = raw_input("Enter your email: ")

emailCheck(email)
