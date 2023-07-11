#%%
import requests
import pandas as pd
import os

selected_brand = input("Voer merk in:\n")

selected_brands_list = selected_brand.split(" ")

for brand in selected_brands_list:
    print(f"Downloading cars for brand {brand}")

    # Convert the value of the brand to an uppercase
    selected_brand_upper = brand.upper()

    # Define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={selected_brand_upper}"

    # Execute the request
    response = requests.get(endpoint)

    # Get the data from the response
    data = response.json()

    # Conditional statement that checks if the list with cars is not empty
    if len(data) == 0:
        print(f"No cars found for {brand}")
        continue

    # Convert the list with cars to a DataFrame
    data_df = pd.DataFrame(data)

    # Only keep the columns specified in the list
    columns = ['merk', 'handelsbenaming', 'catalogusprijs', 'eerste_kleur']
    data_df_filtered = data_df[columns]

    # create the folder for the brand
    files_folders = os.listdir()

    # provide the name of the folder
    folder_name = brand

    # check if the folder already exists
    if folder_name.lower() not in files_folders:
        print(f"Creating folder {folder_name}")
        os.mkdir(folder_name.lower())

    # define the path for the export
    file_path = f"{folder_name}/export_{brand}.csv"

    # export the DataFrame
    data_df_filtered.to_csv(file_path, sep=";", index=False)

    print(f"Finished exporting for brand {brand}")
# %%
