import pandas as pd

df = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

df["Mortality rate, infant (per 1,000 live births)"]
df["GDP per capita (constant 2010 US$)"]
df["Country Name"]

import matplotlib.pyplot as plt

plt.scatter(
    df["Mortality rate, infant (per 1,000 live births)"],
    df["GDP per capita (constant 2010 US$)"],
)
