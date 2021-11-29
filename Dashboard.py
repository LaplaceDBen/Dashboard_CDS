
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import dash
from dash import dcc
import dash_html_components as html
df = pd.read_csv(r'.\Summer-Olympic-medals-1976-to-2008.csv', encoding="utf-8")
df1 = pd.read_csv(r'.\summary.csv', encoding="utf-8")
df.info()
df1.info()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#F0F8FF',
    'text': '#00008B'
}

fig = px.bar(df1, x=df1['Year'], y=[df1['Bronze'],df1['Silver'],df1['Gold']], color_discrete_map={'Bronze': 'orange', 'Silver': 'silver', 'Gold':'gold'}, title="By Country")

app.layout = html.Div(children=[
    html.H1(children='Oympics'),

    html.Div(children='''
        Dashboard_Brunold_Rusconi.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])


app.run_server(debug=True)