#%%
import requests
import sys

selected_brand = input("Voer merk in:\n")
selected_brand_upper = selected_brand.upper()

endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={selected_brand_upper}"

response = requests.get(endpoint)

# %%
data = response.json()

#%%
if len(data) == 0:
    print(f"No cars found for {selected_brand}")
    sys.exit()

#%%
print(data[0])
# %%
