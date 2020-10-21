import pandas as pd

import csv

import plotly.express as px


df = pd.read_csv("The Data.csv")

TheMean = df.groupby(["studentID", "level"], as_index=False)["attempt"].TheMean()
fig = px.scatter(TheMean, a="studentID", b="level", size="attempt", color="attempt")

fig.show()