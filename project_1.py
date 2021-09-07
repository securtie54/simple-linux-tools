#!/usr/bin/env/python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Simple vulnerability Analysis ")

targetip = raw_input("Target Ip ==> ")
os.system("nikto -h" +targetip)
