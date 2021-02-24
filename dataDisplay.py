import pandas as pd
import plotly.express as px

df = pd.read_csv('Covid_Data.csv')

chart = px.scatter(df, x = 'Date', y = 'Cases', color = 'Country', title = 'Covid Cases Per Day')

chart.show()