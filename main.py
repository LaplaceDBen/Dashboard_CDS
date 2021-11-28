import pandas as pd
import plotly.express as px

#Aufgabe 37
df = pd.read_csv(r'.\Summer-Olympic-medals-1976-to-2008.csv', encoding="utf-8")
df['Country'] = df['Country'].astype(str)
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

#fig.show()

#Aufgabe 39
df_max = df.groupby(['Country','Year'])['Medal'].count().reset_index(drop=False)
swiss = df_max[df_max["Country"] == 'Switzerland']
print(swiss)
#a)
fig = px.scatter(x=swiss['Year'], y=swiss['Medal'])
fig.show()
df.info()
#b)
df = px.data.tips()
fig = px.histogram(df, x=swiss['Medal'])
fig.show()
#c)
fig = px.line(x=swiss['Year'], y=swiss['Medal'], title='Switzerland Medal per Year')
fig.show()