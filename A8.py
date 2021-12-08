import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from dash import dcc

#Aufgabe 36
print("\nAufgabe 36\nProjektgruppe:\nBenito Rusconi\nRaphael Brunold\n")

#Aufgabe 37
#(a)
df = pd.read_csv(r'.\Summer-Olympic-medals-1976-to-2008.csv', encoding="utf-8")
df['Country'] = df['Country'].astype(str)
print("Aufgabe 37 (a)\n",df.head(),"\n\n")

#(b)
print(df.info())
count_row = df.shape[0]  # Gives number of rows
count_col = df.shape[1]  # Gives number of columns
print("Aufgabe 37 (b)\nDer Datensatz hat insgesamt",count_col,"Spalten und",count_row,"Zeilen.\n\n\n\n\n")

#Aufgabe 38
#a)
Land = df.groupby('Country')
#print(Land.head())

#b)
Sportart = df.groupby('Sport')
#print(Sportart.head())

#c)
CSdf= df.groupby(['Country', 'Sport']).size().reset_index(name='counts')
print("here")
print(CSdf)
fig = px.bar(CSdf, x="Sport",
             y='counts',color='Country',
             title="Medal Occurence by Country",
             height=600
            )

fig.show()

#Aufgabe 39
df_max = df.groupby(['Country','Year'])['Medal'].count().reset_index(drop=False)
swiss = df_max[df_max["Country"] == 'Switzerland']
#print(swiss)
#a)
fig = px.scatter(x=swiss['Year'], y=swiss['Medal'])
#fig.show()
#b)
df = px.data.tips()
fig = px.histogram(df, x=swiss['Medal'])
#fig.show()
#c)
fig = px.line(x=swiss['Year'], y=swiss['Medal'], title='Switzerland Medal per Year')
#fig.show()
df = pd.read_csv(r'.\Summer-Olympic-medals-1976-to-2008.csv', encoding="utf-8")

#Aufgabe 40
df['Bronze'] = np.where(df['Medal']== 'Bronze', 1, 0)
df['Silver'] = np.where(df['Medal']== 'Silver', 1, 0)
df['Gold'] = np.where(df['Medal']== 'Gold', 1, 0)
df1=pd.pivot_table(df, index=['Country','Year'],values=['Bronze','Silver','Gold'],aggfunc=np.sum)
print(df1)
df1.to_csv('summary.csv')
df1=pd.read_csv(r'.\summary.csv', encoding="utf-8")
print(df1.info())
fig = px.bar(df1, x=df1['Year'], y=[df1['Bronze'],df1['Silver'],df1['Gold']], color_discrete_map={'Bronze': 'orange', 'Silver': 'silver', 'Gold':'gold'}, title="By Country")
#fig.show()

#Siehe Dashboard -> Dort ist es mit Dropdown und Callback wie gewünscht implementiert