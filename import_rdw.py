#%%
import requests
import sys

selected_brand = input("Voer merk in:\n")

selected_brands_list = selected_brand.split(" ")

for brand in selected_brands_list:
    print(f"Downloading cars for brand {brand}")
    selected_brand_upper = brand.upper()

    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={selected_brand_upper}"

    response = requests.get(endpoint)

    # %%
    data = response.json()

    #%%
    if len(data) == 0:
        print(f"No cars found for {brand}")
        continue

    #%%
    print(data[0])

    print(f"Finished downloading for brand {brand}")
# %%
