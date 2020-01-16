#!/usr/bin/env python
import os
import crypt

def addnewuser():

    uname=raw_input("Select Username")
    upass=raw_input("Select Password")

 
    ucrypt=crypt.crypt(upass,"123")
    os.system("useradd -m -p "+upass+" "+uname)

addnewuser()

	
