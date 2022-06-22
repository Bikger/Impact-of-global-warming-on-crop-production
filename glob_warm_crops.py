import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

glob_temp = pd.read_csv("annual.csv")

glob_temp = glob_temp[glob_temp["Source"] == "GISTEMP"] 
glob_temp.head(n=50)

# Global temperature increase graph
plt.figure(figsize=(12,6))
plt.title("Global temperature increase")
sns.lineplot(x=glob_temp["Year"] ,y=glob_temp["Mean"])

crops_df = pd.read_csv("Sorted_crops.csv")
crops_df.head()
crops_df = crops_df.fillna(method="bfill")
print(crops_df["Entity"].nunique())
print(crops_df["Entity"].unique())

crops_bih = crops_df[crops_df["Entity"] == "Bosnia and Herzegovina"].reset_index()

plt.figure(figsize=(12,6))
sns.lineplot(y=crops_df["rice_yield_gap"], x=crops_df["Year"])

crops_df = crops_df[crops_df["Entity"] == "Nigeria"].reset_index()
crops_df["avg_rice_yield"] = crops_df["rice_attainable"] - crops_df["rice_yield_gap"]
crops_df = crops_df[["Entity", "Year", "rice_yield_gap", "avg_rice_yield"]]
crops_df.head()

sns.lineplot(y=crops_df["avg_rice_yield"], x=crops_df["Year"])
plt.legend(labels=["Gloabal rice yield gap", "", "Average farmer rice yield in Nigeria"])

plt.figure(figsize=(12,6))
plt.title("Rice production in Nigeria and global mean temperature")
sns.lineplot(x=glob_temp["Year"], y=glob_temp["Mean"])
plt.ylabel("Mean")

# plot rice production in Nigeria
sns.lineplot(x=crops_df["Year"], y=crops_df["avg_rice_yield"])

print(crops_bih.head())
plt.figure(figsize=(12,6))
plt.title("BiH crops")