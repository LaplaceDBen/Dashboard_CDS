import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import datetime
from dash import dcc
import dash
from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html

df = pd.read_csv(r'.\Summer-Olympic-medals-1976-to-2008.csv', encoding="utf-8")
df1 = pd.read_csv(r'.\summary.csv', encoding="utf-8") #Zusammenfassung des grossen Datensatzes
print(df.info())

app = dash.Dash(__name__)
#Aufgabe 46

def A_46(df):
    app.layout = dash_table.DataTable(
        columns=[
            {'name': 'City', 'id': 'City', 'type': 'text'},
            {'name': 'Year', 'id': 'Year', 'type': 'numeric'},
            {'name': 'Sport', 'id': 'Sport', 'type': 'text'},
            {'name': 'Discipline', 'id': 'Discipline', 'type': 'text'},
            {'name': 'Event', 'id': 'Event', 'type': 'text'},
            {'name': 'Athlete', 'id': 'Athlete', 'type': 'text'}
        ],
        data=df.to_dict('records'),
        filter_action='native',

        style_table={
            'height': 200,
        },
        style_data={
            'width': '100px', 'minWidth': '100px', 'maxWidth': '150px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
        }
    )

def A_47(df):
    print(1)
if __name__ == '__main__':
    A_46(df)
    app.run_server(debug=True)