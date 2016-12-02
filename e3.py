import pandas as pd
import matplotlib.pyplot as plt
import json

with open("ELECTION_ID") as f:
    yeid = json.load(f)

df_list = []
for year, eid in yeid:
    header = pd.read_csv(year + ".csv", nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv(year + ".csv",
                        index_col = 0,
                        thousands = ",",
                        skiprows = [1])
    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["Year"] = year
    df_list.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])
df = pd.concat(df_list)
df["Republican Share"] = df["Republican"] / df["Total Votes Cast"]

def county_plot(county_name):
    ### The following line is too long. Use \ to break lines
    df.ix[county_name + " County", ["Year", "Republican Share"]].sort(["Year"], ascending = True).plot(x = "Year", y = "Republican Share")
    plt.savefig(county_name.lower() + '.png')

county_plot("Accomack")
