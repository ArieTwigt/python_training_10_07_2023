#%% Assignment 1 - Assign a variable that holds the number of days until your next birthday
from datetime import date

next_birthday = date(2024, 4, 1)
date_today = date.today()

difference = next_birthday - date_today
days_difference = difference.days
print(days_difference)

# %%
import math

diameter = 10
radius = diameter / 2

size = math.pow(radius, 2) * math.pi
print(size)
# %%

#%% Assignment 3
import os

files_folders = os.listdir()

# %% Assignment 4
os.mkdir("our_functions")

# %%
