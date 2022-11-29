import pandas as pd
import numpy as np


df = pd.read_csv("crimedata.csv")[["state", "communityName", "population", "medIncome", "numbUrban", "PctUnemployed", "murders", "rapes", "robberies", "assaults", "burglaries", "larcenies", "autoTheft", "arsons"]]
df = df.dropna()
df["numbUnemployed"] = df["population"]*df["PctUnemployed"]/100
df = df.drop("PctUnemployed", axis=1)
df = df.groupby(["state", "communityName"]).agg({"population":"sum", "numbUrban":"mean", "numbUnemployed":"mean", "medIncome":"mean", "murders":"sum", "rapes":"sum", "robberies":"sum", "assaults":"sum", "burglaries":"sum",
                              "larcenies":"sum", "autoTheft":"sum", "arsons":"sum"})
df["pctUnemployed"] = 100*df["numbUnemployed"]/df["population"]
df["pctUrban"] = 100*df["numbUrban"]/df["population"]
df = df.drop("numbUnemployed", axis=1)
df = df.drop("numbUrban", axis=1)
df = df.reset_index()



df_population = df.groupby(["state", "population"]).agg({"murders":"mean", "rapes":"mean", "robberies":"mean", "assaults":"mean", "burglaries":"mean",
                                                         "larcenies":"mean", "autoTheft":"mean", "arsons":"mean"}).reset_index()




df_income = df.groupby(["state", "medIncome"]).agg({"murders":"mean", "rapes":"mean", "robberies":"mean", "assaults":"mean", "burglaries":"mean",
                                                     "larcenies":"mean", "autoTheft":"mean", "arsons":"mean"}).reset_index()
df_income["rounded_income"] = df_income["medIncome"]/100000
df_income["rounded_income"] = df_income["rounded_income"].apply(lambda x: round(x, 2))*100000

df_income = df_income.groupby(["state", "rounded_income"]).agg(
    {"murders": "mean", "rapes": "mean", "robberies": "mean", "assaults": "mean", "burglaries": "mean",
     "larcenies": "mean", "autoTheft": "mean", "arsons":"mean"}).reset_index()





df_pct_unemp = df.groupby(["state", "pctUnemployed"]).agg({"murders":"mean", "rapes":"mean", "robberies":"mean", "assaults":"mean", "burglaries":"mean",
                                                      "larcenies":"mean", "autoTheft":"mean", "arsons":"mean"}).reset_index()

df_pct_unemp["rounded_pct"] = df_pct_unemp["pctUnemployed"]/100
df_pct_unemp["rounded_pct"] = df_pct_unemp["rounded_pct"].apply(lambda x: round(x, 1))*100

df_pct_unemp = df_pct_unemp.groupby(["state", "rounded_pct"]).agg(
    {"murders": "mean", "rapes": "mean", "robberies": "mean", "assaults": "mean", "burglaries": "mean",
     "larcenies": "mean", "autoTheft": "mean", "arsons":"mean"}).reset_index()




df_pct_urban = df.groupby(["state", "pctUrban"]).agg({"murders":"mean", "rapes":"mean", "robberies":"mean", "assaults":"mean", "burglaries":"mean",
                                                           "larcenies":"mean", "autoTheft":"mean"}).reset_index()

df_pct_urban["rounded_pct"] = df_pct_urban["pctUrban"]/100
df_pct_urban["rounded_pct"] = df_pct_urban["rounded_pct"].apply(lambda x: round(x, 1))*100

df_pct_urban = df_pct_urban.groupby(["state", "rounded_pct"]).agg(
    {"murders": "mean", "rapes": "mean", "robberies": "mean", "assaults": "mean", "burglaries": "mean",
     "larcenies": "mean", "autoTheft": "mean"}).reset_index()









