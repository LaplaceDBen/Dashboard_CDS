
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output #Wichtig für Callbacks

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(r'.\Summer-Olympic-medals-1976-to-2008.csv', encoding="utf-8")
df1 = pd.read_csv(r'.\summary.csv', encoding="utf-8")
#df.info()
#df1.info()

colors = {
    'background': '#F0F8FF',
    'text': '#00008B'
}

#Funktionnierender Plot von Benito
#fig = px.bar(df1, x=df1['Year'], y=[df1['Bronze'],df1['Silver'],df1['Gold']], color_discrete_map={'Bronze': 'orange', 'Silver': 'silver', 'Gold':'gold'}, title="By Country")

app.layout = html.Div([
    html.H1('Oympics', style= {'text-align':'center'}),

    html.Div('''
        Dashboard by Brunold & Rusconi
    '''),


    html.Br(),

    #Dropdown (Raffi)
    dcc.Dropdown(id='dropdownCountry',
                 options = [
                     {"label": "Switzerland", "value": 'Switzerland'},
                     {"label": "Germany", "value": 'Germany'},
                     {"label": "United States", "value": 'United States'},
                     {"label": "Russia", "value": 'Russia'},
                     {"label": "China", "value": 'China'}],
                 multi = False,
                 value = 'Switzerland',
                 style = {"width": "40%"}
                 ),

    dcc.Graph(id='countryplot', figure = {}),

#Funktionnierender Plot von Benito
   # dcc.Graph(
   #     id='example-graph',
   #     figure=fig
   # )
])

#Callback (Raffi)
@app.callback(
    [Output(component_id='countryplot', component_property='figure')],  #Es kommt das angepasste Diagramm raus
    [Input(component_id='dropdownCountry', component_property='value')] #Es kommt die Auswahl vom Dropdown rein
)
def update_graph(option_slctd):
    dff = df1.copy()
    dff = dff[dff["Country"] == option_slctd]
    print(dff.head()) #Schaut gut aus, Schweiz wird Standardmässig ausgewählt.
#Plotly Express (Diagramm definieren)
    fig = px.bar(dff, x='Year', y=['Bronze', 'Silver', 'Gold'],
                 color_discrete_map={'Bronze': 'orange', 'Silver': 'silver', 'Gold': 'gold'},
                 title="Medals won by selected country")
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)