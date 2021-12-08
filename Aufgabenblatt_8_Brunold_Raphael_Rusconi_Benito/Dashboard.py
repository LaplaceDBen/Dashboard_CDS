
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
df1 = pd.read_csv(r'.\summary.csv', encoding="utf-8") #Zusammenfassung des grossen Datensatzes
#df.info()
#df1.info()

colors = {
    'background': '#F0F8FF',
    'text': '#00008B'
}

# #Funktionnierender Plot für Tests
# fig = px.bar(df1, x=df1['Year'], y=[df1['Bronze'],df1['Silver'],df1['Gold']], color_discrete_map={'Bronze': 'orange', 'Silver': 'silver', 'Gold':'gold'}, title="By Country")

app.layout = html.Div([
    html.H1('Oympics', style = {'text-align':'center'}),

    html.Div(
        html.Img(src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Olympic_rings_without_rims.svg/1920px-Olympic_rings_without_rims.svg.png',width=120, alt="Olympic Rings"), style = {'text-align':'center'}
    ),

    html.Div(
        "Dashboard by Brunold & Rusconi"
    ),

    html.Br(),

    #Dropdown
    dcc.Dropdown(id='dropdownCountry',
                 options = [{'label': i, 'value': i} for i in df1['Country'].unique()],
                 multi = False,
                 value = 'Switzerland',
                 style = {"width": "40%"}
                 ),

    dcc.Graph(id='countryplot', figure = {}), #Plot abbilden. in {} kommt der Return von der Callback-Funktion

#  Plot ohne Dropdown und Callback zum Schauen ob Plots sauber abgebildet werden
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
#Plotly Express (Diagramm definieren)
    fig = px.bar(dff, x='Year', y=['Bronze', 'Silver', 'Gold'],
                 color_discrete_map={'Bronze': 'orange', 'Silver': 'silver', 'Gold': 'gold'},
                 labels=dict(value="Number of medals won", year="Year", variable="Medal"),
                 title="Medals won by selected country")
    fig.update_xaxes(
        dtick=4)
    return fig,


if __name__ == '__main__':
    app.run_server(debug=True)