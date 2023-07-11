#%% Assignment 1
names_list = ['Jim', 'John', 'Marc', 'Danny', 'Peter']

vowels_list = ['a', 'e', 'o', 'u', 'i', 'y']

new_names_list = []

for name in names_list:
    print(name)
    for letter in name:
        if letter.lower() in vowels_list:
            name = name.replace(letter, "")
    new_names_list.append(name)


## Assignment 2

# %%
from datetime import date, timedelta

current_date = date.today()

days = 10

for day_num in range(0, days + 1):
    new_date = current_date + timedelta(days=day_num)
    new_day = new_date.strftime("%A")
    print(new_day)
