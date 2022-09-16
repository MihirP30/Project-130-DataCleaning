import pandas as pd

df = pd.read_csv("total_stars.csv")

del df["Luminosity"]
del df["id.1"]
del df["Star_name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]


df.to_csv('main.csv') 