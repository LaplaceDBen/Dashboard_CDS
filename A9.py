import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from dash import dcc

df = pd.read_csv(r'.\Summer-Olympic-medals-1976-to-2008.csv', encoding="utf-8")
df1 = pd.read_csv(r'.\summary.csv', encoding="utf-8") #Zusammenfassung des grossen Datensatzes
#print(df.info())
#Aufgabe 41

def A_41(df):
    Sportarten = df['Sport'].astype(str).tolist()
    #print(type(Sportarten))
    Sportarten.sort()

    Disziplinen = df['Discipline'].astype(str).tolist()
    Disziplinen.sort()

    Events = df['Event'].astype(str).tolist()
    Events.sort()

    SDE = Sportarten + Disziplinen + Events
    SDE.sort()
    #print(SDE)

    Medaillengewinner= df['Athlete'].astype(str).tolist()
    Medaillengewinner.sort()

    Länder = df['Country'].astype(str).tolist()
    Länder.sort()

    return SDE,Medaillengewinner,Länder

#A_41(df)

#Aufgabe 42
def A_42(df):
    df_m = df.groupby(['Country']).size().reset_index(name='counts')
    m= df_m.sort_values(by=['counts'], ascending=False)
    print(m.head(10))
    return m

#A_42(df)

#Aufgabe 43

def A_43(df):
    df_cd = df.groupby(['Country','Discipline']).size().reset_index(name='counts')
    cd = df_cd.sort_values(by=['Country','Discipline'], ascending=True)
    print(cd)
    return cd
A_43(df)