import pandas as pd
import csv 
import plotly.graph_objects as go

df=pd.read_csv("Data.csv")
r=df.groupby("level")['attempt'].mean()
print(r)

#instead of 6 and 7 , we can use 
#print(df.groupby("level")['attempt'].mean())

fig=go.Figure(go.Bar(
    x=r,
    y=["Level 1","Level 2","Level 3","Level 4"],
    orientation="h"
))
fig.show()