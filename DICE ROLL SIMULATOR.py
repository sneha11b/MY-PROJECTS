#!/usr/bin/env python
# coding: utf-8

# # DICE ROLL SIMULATOR

# In[ ]:


import random
import time


# In[ ]:


num_sides = 6

def get_num_rolls():
    while True:
        try:
            num_rolls = input("How many times would you like to roll the dice? ")
            num_rolls = int(num_rolls)
            if num_rolls <= 0:
                raise ValueError("Please enter a positive integer.")
            elif num_rolls > 50:
                raise ValueError("You can't roll more than 50 dice at a time.")
            break
        except ValueError as e:
            print(e)
    return num_rolls

def roll_dice():
    dice_roll = random.choice(range(1, num_sides+1))
    print("You rolled a " + str(dice_roll))

# Welcome message
print("Welcome to the dice rolling simulator!")
time.sleep(1)

# Get number of rolls
num_rolls = get_num_rolls()

# Roll the dice
for i in range(num_rolls):
    print("Roll #" + str(i+1) + ":")
    roll_dice()
    time.sleep(1)

# Credits message
print("Thanks for playing!\nCreated by: \n[SNEHA BHUNIA] \n[DISHANI GHOSHAL].")


# In[ ]:


import random     
import time      #importing modules

#assigning number of sides of dice to variable.
num_sides = 6

#defining a function to gather rolling inputs from user.
def get_num_rolls(): 
    
    
#The while loop continues until the user enters a valid input that can be converted to a positive integer, 
#at which point the break statement is executed, and the function returns the valid input as an integer.    
    while True:
        
#the try block is attempting to convert the user's input for the number of rolls to an integer using the int() function. 
#If the conversion is successful, the code checks if the resulting integer is greater than 0. 
#If it is not greater than 0, then a ValueError is raised using the raise keyword.  
        try:          
            num_rolls = int(input("How many times would you like to roll the dice? "))
            if num_rolls <= 0:
                

#The except block is executed if an error is raised in the try block, which means that the user entered a non-integer or a negative integer for the number of rolls. 
#In this case, the code in the except block prints a message asking the user to enter a positive integer.

                raise ValueError("Please enter a positive integer.")
            elif num_rolls > 50:
                raise ValueError("You can't roll more than 50 dice at a time.")
            break
        except ValueError as e:
            print(e)
    return num_rolls


#defining  a function to roll the dice
def roll_dice():
    
#In this line of code, random.choice() is a function from the random module in Python that randomly chooses an element from a sequence. 
#In this case, the sequence is generated using the range() function, which creates a sequence of numbers from 1 to num_sides (inclusive).
#So, range(1, num_sides+1) will generate a sequence of numbers from 1 to num_sides, which in this case is 6. 
#The +1 is added to ensure that the sequence includes the upper bound, which is 6 in this case.
#random.choice() then randomly chooses one of the numbers from the sequence, which simulates the roll of a dice with num_sides sides.
#Finally, the result of this random choice is assigned to the variable dice_roll.  
    
    dice_roll = random.choice(range(1, num_sides+1))
    print("You rolled a " + str(dice_roll))

# Welcome message
print("Welcome to the dice rolling simulator!")
time.sleep(1)

# Get number of rolls
#get_num_rolls() function is called to prompt the user to enter the number of times they want to roll the dice. 
#The result of this function call is assigned to the variable num_rolls.
num_rolls = get_num_rolls()

# Roll the dice
for i in range(num_rolls):            #for loop in Python that runs num_rolls number of times.


    print("Roll #" + str(i+1) + ":") #The str() function used to convert the roll no(integer) to a string which can be concatenated with the other parts of the message.
    roll_dice()#the roll_dice() function is called to simulate the rolling of a dice.
    time.sleep(1)#time.sleep(1) function, which creates a brief pause to create a more realistic simulation of rolling dice.

# Thank you message
print("Thanks for playing!\nCreated by: \n[SNEHA BHUNIA] \n[DISHANI GHOSHAL].")

