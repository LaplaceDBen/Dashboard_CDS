import pandas as pd
import plotly.express as px

#Aufgabe 37
df = pd.read_csv(r'.\Summer-Olympic-medals-1976-to-2008.csv', encoding="utf-8")
print(df.head())
print(df.info)
#Aufgabe 38
#a)
Land = df.groupby('Country')
#b)
Sportart = df.groupby('Sport')
print(Land.head())
#c)
CSdf= df.groupby(['Country', 'Sport']).size().reset_index(name='counts')

fig = px.bar(CSdf, x="Country",
             y='counts',
             title="Medal Occurence by Country",
             barmode='group',
             height=600
            )

fig.show()

#Aufgabe 39

#a)
