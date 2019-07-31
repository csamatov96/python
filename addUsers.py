#!/usr/bin/env python
import sys #This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import subprocess #The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
while True: #infinite loop which will never stop  
        print "\nSudo users have special privileges. Be careful!\n" #will be displayed
        print "\nSudo users list\n: " #will be displayed
        subprocess.call(["grep","wheel","/etc/group"]) #The list of command line arguments passed to a Python script. argv[0] is the script name (it is operating system dependent whether this is a full pathname or not). If the command was executed using the -c command line option to the interpreter, argv[0] is set to the string '-c'. If no script name was passed to the Python interpreter, argv[0] is the empty string.
        if len(sys.argv) > 1: #IF the length of argv values which is the argument of sys is bigger than 0 so then 
                name = sys.argv[1] #assign them to name 
        else: #otherwise 
                name = raw_input('Enter User Name:') #prompt the following
        if name == 'root': #if the value is equal to the following 
                print("\nCan't do anything with the 'root' user account") #display the following 
		print("\nBreaking the program\n") #display the following 
                sys.exit() #and stop the script 
         
        opt = int(raw_input("Select option: 1 to create user. Select option: 2 to delete that user: ")) #one more prompt to choose  

        if opt == 1: #if the value of opt variable is equal to the follwing 
                subprocess.call(["useradd", name]) #by using call function of subprocess library run linux command to add that user 
                subprocess.call(["usermod", "-aG","wheel", name]) #add him to wheel
                subprocess.call(["passwd", name]) #give him a passwpord 
                print('\x1b[6;30;42m' + 'Sudo user creation is a Success!' + '\x1b[0m') #display the following in colorful way 

        elif opt == 2: #or if the value of opt variable is equal to the follwing
                subprocess.call(["userdel","-r", name]) #by using call function of subprocess library run linux command to delete that user
                print('\x1b[6;30;42m' + 'Sudo user deletion is a Success!' + '\x1b[0m') #and display the following in colorful way
        else: #otherwise 
                print "Invalid option" #display the following

        op = raw_input("Do you want to continue YES:NO: ") #one more prompt to choose

        if op == 'NO' or op == 'no': #if the value of that variable is equal to the following string values so then 
                sys.exit() #stop the script
