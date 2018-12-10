# German vocabulary Exercise program
# use of dictionary function  
# python version = 3.7 - someo fo random functions won't work on Python 2.* 

#import random function - use of randomdict 
import os 
import random
from dic_data import german

# sample dictionary 
# german = {'das Haus':'House', 'gelb':'yellow', 'rot':'red', 'das Decke':'desk'}

os.system('clear')

#Greeting 
print ("")
print ("Wilkommen Deutsch Wörter Übungen!")
print ("")

print = input("Press anykey continue. \n")

#python 3.7 specific functions having to add 'list'
choice = random.choice(list(german.keys()))

#question to user and asking to input an answer  
question = input("What is the meaning of this German word" + " ( " +choice+ " ) "+"in English? :  ")

#Continue or exit the program 


more_stop = input ("Plase enter 1 to continue and 2 to exit the program:  \n")



