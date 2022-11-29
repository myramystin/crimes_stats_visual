import pandas as pd

df = pd.read_csv("crimedata.csv")[["state", "communityName", "population", "medIncome", "numbUrban", "PctUnemployed",
                                   "PctNotSpeakEnglWell", "TotalPctDiv",
                                   "murders", "rapes", "robberies", "assaults", "burglaries", "larcenies", "autoTheft",
                                   "arsons"]]
df = df.dropna()
df["numbUnemployed"] = df["population"] * df["PctUnemployed"] / 100
df["numbNotSpeakEnglWell"] = df["population"] * df["PctNotSpeakEnglWell"] / 100
df["numbDiv"] = df["population"] * df["TotalPctDiv"] / 100
df = df.drop(["PctUnemployed", "PctNotSpeakEnglWell", "TotalPctDiv"], axis=1)
df = df.groupby(["state", "communityName"]).agg({"population": "sum", "numbUrban": "sum",
                                                 "numbUnemployed": "sum",
                                                 "numbNotSpeakEnglWell": "sum", "numbDiv": "sum",
                                                 "medIncome": "mean",
                                                 "murders": "sum", "rapes": "sum",
                                                 "robberies": "sum", "assaults": "sum", "burglaries": "sum",
                                                 "larcenies": "sum", "autoTheft": "sum", "arsons": "sum"})
df["pctDiv"] = (100 * df["numbDiv"] / df["population"]).apply(lambda x: int(x))
df["pctNotSpeakEnglWell"] = (100 * df["numbNotSpeakEnglWell"] / df["population"]).apply(lambda x: int(x))
df["pctUnemployed"] = (100 * df["numbUnemployed"] / df["population"]).apply(lambda x: int(x))
df["pctUrban"] = (100 * df["numbUrban"] / df["population"]).apply(lambda x: int(x))
df["medIncome"] = df["medIncome"].apply(lambda x: round(x))
df = df.drop(["numbUnemployed", "numbUrban", "numbNotSpeakEnglWell"], axis=1)
df["crimes_count"] = df["murders"] + df["rapes"] + df["robberies"] + df["assaults"] + df["burglaries"] + df[
    "larcenies"] + df["autoTheft"] + df["arsons"]

df = df.reset_index()

# print(df.head())
