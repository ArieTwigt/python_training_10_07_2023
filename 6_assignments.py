#%% Assignment 1

vowels_list = ['a', 'e', 'o', 'u', 'i']

names_list = ['Jim', 'John', 'Marc', 'Danny', 'Peter']

for name in names_list:
    for letter in name:
        if letter in vowels_list:
            name = name.replace(letter, "")
    
    print(name)

# %% Assignment 2 - Create a loop that prints the name of the day for the following 10 days
from datetime import date, timedelta

current_date = date.today()

num_days = 10

for day_num in range(1, num_days + 1):
    new_date = current_date + timedelta(days=day_num)
    new_day_name = new_date.strftime("%A")
    print(new_day_name)


# %%
