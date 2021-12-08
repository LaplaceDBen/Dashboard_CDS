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

A_41(df)

def A_42(df):
