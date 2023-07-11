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



# %%
