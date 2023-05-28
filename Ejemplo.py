import pandas as pd
from pandas import *

df = pd.read_csv("COVID19.csv")

#print(df[df["deaths"] > 4000])

#print(df[['countriesAndTerritories', 'deaths']][df["dateRep"] == "14/12/2020"])

df = df[['countriesAndTerritories', 'deaths']][df["cases"] >= 100000]
#df = df[['countriesAndTerritories']]
df = pd.DataFrame(df)
df.to_csv('file.csv')

# data = read_csv("Paises3.csv")
# listaPaises = data['countriesAndTerritories'].tolist()
# print("Month: ", listaPaises)
