# Assignment 1 - Create a conditional statement that indicates if your name starts with an "A or not

#%% a
name = "Arie"

if "a" in name.lower():
    print("Your name begins with an A")

#%% b
if name[0].lower() == "a":
    print("Your name begins with an A")


# Assignment 2 - Create a conditional statement that indicates if your name begins with a vowel. If it does, change it into a non-vowel and otherwise. For example: Arie –> Brie or Rose –> Aose

#%%
name = "Arie"

vowels = "aeoui"

if name[0].lower() in vowels:
    name = name.replace(name[0], "B")
    print(name)
else:
    name = name.replace(name[0], "A")


# Assignment 3

#%% a
age = 20

if age > 18 and age < 68:
    print("Your age is between 18 and 68")
else:
    print("It is not")

#%% b
age = 20

if 18 <= age <= 68:
    print("Your age is between 18 and 68")
else:
    print("It is not")
# %%
