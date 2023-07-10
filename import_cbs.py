#%%
import requests
import pandas

response = requests.get("https://opendata.cbs.nl/ODataApi/odata/37478eng/UntypedDataSet")
# %%
data = response.json()
# %%
data_df = pandas.DataFrame(data['value'])
# %%
data_df.to_csv("data.csv", index=False, sep=";")
# %%
