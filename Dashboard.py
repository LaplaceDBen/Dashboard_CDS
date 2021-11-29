
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

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
    html.H1('Oympics',style={'text-align': 'center'}),

    html.Div('''
        Dashboard by Brunold & Rusconi
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    # Raffi: Dropdown (sollte gehen)
    dcc.Dropdown(id="auswahlLand",
                 options=[
                     {"label": "Switzerland", "value": "Switzerland"},
                     {"label": "Germany", "value": "Germany"},
                     {"label": "United States", "value": "United States"},
                     {"label": "Russia", "value": "Russia"}, ],
                 multi=False,
                 value="Switzerland",
                 style={'width': "40%"}
                 ),

    html.Br(),
    dcc.Graph(
        id='dropdownLand',
        figure={})
])

#Raffi: Callback (geht noch gar nicht)
@app.callback(
    [Output(component_id='dropdownLand', component_property='figure')],
    [Input(component_id='auswahlLand', component_property='value')]
)
def update_graph(auswahl):
    container = "Your selection was: {}".format(auswahl)
    dff = df1.copy()
    dff = dff[dff["Country_Code"] == auswahl]

    fig = px.bar(df1, x=df1['Year'], y=[df1['Bronze'], df1['Silver'], df1['Gold']], color_discrete_map={'Bronze': 'orange', 'Silver': 'silver', 'Gold': 'gold'}, title="By Country")

    return container, fig

app.run_server(debug=True)