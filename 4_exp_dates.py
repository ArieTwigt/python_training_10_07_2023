#%%
from datetime import date, datetime, timedelta



# %%
current_date = date.today()

# %%
current_date_time = datetime.now()

# %%
current_date_time.strftime("Het is nu %H uur")

# %%
pakjesavond = date(2023, 12, 5)
# %%
difference = pakjesavond - current_date
# %%
days_difference = difference.days
# %%
print(f"Pakjesavond is over {days_difference} dagen")

# %%
current_date + timedelta(days=10000)

# %%
date_str = "01-2023-01"
datetime.strptime(date_str, "%m-%Y-%d")

# %%
