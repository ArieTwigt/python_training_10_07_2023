#%% Assignment 1

vowels_list = ['a', 'e', 'o', 'u', 'i']

names_list = ['Jim', 'John', 'Marc', 'Danny', 'Peter']

for name in names_list:
    for letter in name:
        if letter in vowels_list:
            name = name.replace(letter, "")
    
    print(name)
# %%
