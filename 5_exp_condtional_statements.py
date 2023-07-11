#%%
age = 17

if age > 18:
    print("Proost")
    print("🍻")
else:
    print("Helaas")

print("De rest van de code")

# %%
guests_list = ['Jim', 'Jack', 'James']

name = "Arie"

#%%
if name in guests_list:
    print("Welcome")
    print(guests_list)
else:
    print("Unfortunately")
    guests_list.append(name)
    print(guests_list)

# %%
numbers_list = [1,2,3,4,5]



#%%
number = 8

if number not in numbers_list:
    print(f"{number} not in the list yet")
    numbers_list.append(number)

print(numbers_list)

# %%
age = 17
name = "Arie"


guests_list = ['Jim', 'Jack', 'James', 'Arie']

if name in guests_list or age > 18:
    print("Welcome")
else:
    print("Helaas")



# %%
donation_goal = 1000

donated = 0

while donated <= donation_goal:
    print(f"Current donation {donated}")
    donated += 100
    
# %%
age = 17


if age < 18:
    print("Geen Alcohol")
elif age > 12:
    print("Wel cola")
else:
    print("Proost")


#%%
letter = "a"
name = "Arie"

if letter in name.lower():
    print("Letter in name")
else:
    print("No letter in name")

# %%
