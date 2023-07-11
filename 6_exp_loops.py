#%%
import math

diameters = [10, 20, 30, 40, 50]
sizes = []

for diameter in diameters:
    radius = diameter / 2
    size = math.pow(radius, 2) * math.pi
    sizes.append(size)


# %%
names_list = ['Arie', "Jim", "Bob", "Jaap", "Gerrit", "Annie", "Peter"]

names_with_an_a = []
names_without_an_a = []
names_with_an_a_index = []

for idx, name in enumerate(names_list):
    if "a" in name.lower():
        names_with_an_a.append(name)
        names_with_an_a_index.append
    else:
        names_without_an_a.append(name)


# %%
numbers_list = [1,2,3,4,5]


[number * 10 for number in numbers_list]

#%% filter in list comprehension
new_numbers = [number for number in numbers_list if number > 3]


#%%
new_list = []

for number in numbers_list:
    new_list.append(number * 10)