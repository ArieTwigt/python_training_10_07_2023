#%% Assignment 2

# create 4 dictionaries with persons
person_1 = {"name": "Jim",
            "age": 50}

person_2 = {}
person_2['name'] = "Mary"
person_2['age'] = 40

person_3 = {}
person_3['name'] = "James"
person_3['age'] = 20
person_3['hobbies'] = ['football', 'tennis']

person_4 = {}
person_4['name'] = 'Tim'
person_4['age'] = 8
person_4['hobbies'] = ['gaming', 'cycling']

# %%
family_dict = {}
family_dict['name'] = 'Jones'
family_dict['members'] = [person_1, person_2, person_3, person_4]


# %%
person_5 = {}
person_5['name'] = "Bobby"
person_5['age'] = 0

#%%
family_dict['members'].append(person_5)
# %%
