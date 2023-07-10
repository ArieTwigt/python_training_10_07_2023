#%%
number = "6"
print(number)
# %%
int(number)

# %%
name = "Arie"
list(name)
# %%
my_list = []
# %%
my_list.append(4)
# %%
names_list = ["Arie", "James", "James", "James"]
# %%
names_list.remove("James")
# %%
4 + 4
# %%
"Arie" + "Twigt"
# %%
names_list + names_list
# %%
"Arie" + 4
# %%
4 + "Arie"
# %%
names_list


#%%
names_list = ["Dirk", "Arie", "James", "James", "James", "Bert"]
# %%
names_list.sort(reverse=True)

# %%
list(set(names_list))

# %%
my_shop = {"name": "Arie's Bar",
           "location": "Enschede",
           "established": 2020,
           "products": ["a", "b", "c"]}

# %%
my_person = {}
# %%
my_person['name'] = "Arie"

# %%
my_names = ['Jaap', 'Dirk', 'Arie']
my_ages = [10, 20, 30]
# %%
dict(zip(my_names, my_ages))
# %%
