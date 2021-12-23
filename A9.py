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
    df_cd = df.groupby(['Country','Sport']).size().reset_index(name='counts')
    cd = df_cd.sort_values(by=['Country','Sport'], ascending=True)
    print(cd)
    return cd
#A_43(df)

#Aufgabe 44

def A_44(df):
    country = A_42(df)
    cd_df = A_43(df)
    country = country.rename(columns={'counts': 'counts_all'})
    ratio_df = country.merge(cd_df, how='left', left_on='Country', right_on='Country')
    ratio_df['normalized']= ratio_df['counts']/ ratio_df['counts_all']
    final_df = ratio_df.sort_values(by=['Country','Sport'], ascending=True)
    print(final_df)

    fig = go.Figure(data=go.Heatmap(
        z=final_df['normalized'], x=final_df['Country'],y=final_df['Sport'],hoverongaps=False))
    fig.write_html("file.html")
    fig.show()
    return final_df

A_44(df)

