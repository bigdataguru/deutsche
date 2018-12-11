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

print = input("Press enter to continue.")


more = "yes"

#python 3.7 specific functions having to add 'list'
#choice = random.choice(list(german.keys()))

while more == "yes" or more == "y":
	
    print = input("\nWhat is the meaning of this German word" + " ( " + (random.choice(list(german.keys())))
+ " ) "+"in English? :  ")

    more = input("\nlearn more words?:   ")



