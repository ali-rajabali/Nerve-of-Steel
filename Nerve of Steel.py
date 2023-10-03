#!/usr/bin/env python
# coding: utf-8

# # MGTC28 - In Class Excerise 4
# ### Nerve of Steel <br>
# Fall 2023
# 
# **Instructor**: Prof. Bill Chau<br>

# In[17]:


"""
This program is for MGTC28.
nerve.py is a simple Python script that executes a party game where players sit in a circle.
1. The program displays "Players stand"

2. The program sleeps for a random time between 5 to 25 seconds.  While the program is sleeping, players can sit down.  Keep track of the last person to sit down.

3. When sleep is over, the program displays "Time Up.  Last to sit down wins."  Players still standing are eliminated, and the winner is the last person to sit down.
"""


# In[18]:


# This program that executes the Nerve of Steel game. 

import time # The time library has a sleep function that will pause the script for a specifized amount of time
import random 


# In[19]:


print ("Players stand")

#Set the random time interval for when the computer goes to sleep between 5 and 25 seconds
sleep_time = random.randint(5, 25)

#Set the timer for the computer to script to sleep
time.sleep(sleep_time)

print ("The timer was on for ", sleep_time, "seconds.") #This will show the timer actually worked for the seconds in the range devined above
print ("Time Up.  Last to sit down wins.")


# In[ ]:




