from A8 import df,df1
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html

df.info()
df1.info()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#F0F8FF',
    'text': '#00008B'
}

fig = px.bar(df1, x=df1['Year'], y=[df1['Bronze'],df1['Silver'],df1['Gold']],  title="By Country")

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