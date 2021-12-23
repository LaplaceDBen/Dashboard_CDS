
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

sportarten = ['Aquatics', 'Archery', 'Athletics', 'Basketball', 'Boxing', 'Canoe / Kayak',
 'Cycling', 'Equestrian', 'Fencing', 'Football', 'Gymnastics', 'Handball',
 'Hockey', 'Judo', 'Modern Pentathlon', 'Rowing', 'Sailing', 'Shooting',
 'Volleyball', 'Weightlifting', 'Wrestling', 'Table Tennis', 'Tennis',
 'Badminton', 'Baseball', 'Softball', 'Taekwondo', 'Triathlon']

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

    html.Br(),

    dcc.Dropdown(id='dropCountry',
                 options = [{'label': i, 'value': i} for i in df1['Country'].unique()],
                 multi = False,
                 value = 'Switzerland',
                 style = {"width": "40%"}
                 ),

    html.Br(),

    dcc.RangeSlider(
        id='sliderYear',
        min=1976,
        max=2008,
        step=None,
        marks={
            1976: '1976',
            1980: '1980',
            1984: '1984',
            1988: '1988',
            1992: '1992',
            1996: '1996',
            2000: '2000',
            2004: '2004',
            2008: '2008'
        },
        value=[1976, 2008],
        allowCross=False
    ),

    dcc.Graph(id='country_year', figure = {}),

    html.Br(),

    dcc.Dropdown(id='dropSport',
                 options=[{'label': i, 'value': i} for i in (sportarten)],
                 multi=False,
                 value='Archery',
                 style={"width": "40%"}
                 ),

    html.Br(),

    dcc.RangeSlider(
        id='sliderYear2',
        min=1976,
        max=2008,
        step=None,
        marks={
            1976: '1976',
            1980: '1980',
            1984: '1984',
            1988: '1988',
            1992: '1992',
            1996: '1996',
            2000: '2000',
            2004: '2004',
            2008: '2008'
        },
        value=[1976, 2008],
        allowCross=False
    ),

    dcc.Graph(id = 'sportPie', figure = {}),


    #  Plot ohne Dropdown und Callback zum Schauen ob Plots sauber abgebildet werden
   # dcc.Graph(
   #     id='example-graph',
   #     figure=fig
   # ),

])

#Callback (Raffi)
@app.callback(
    [Output(component_id='countryplot', component_property='figure')],      #1. Diagramm: Es kommt das angepasste Diagramm raus
    [Output(component_id='country_year', component_property='figure')],     #2. Diagramm
    [Output(component_id='sportPie', component_property='figure')],         #3. Diagramm

    [Input(component_id='dropdownCountry', component_property='value')],    #1. Diagramm:Es kommt die Auswahl vom Dropdown rein
    [Input(component_id='dropCountry', component_property='value')],        #2. Diagramm: Auswahl Länder-Dropdown
    [Input(component_id='sliderYear',component_property='value')],         #2. Diagramm: Auswahl Range-Slider fürs Jahr
    [Input(component_id='dropSport', component_property='value')],          #3. Diagramm: Auswahl Sportart
    [Input(component_id='sliderYear2', component_property='value')]         #3. Diagramm: Auswahl Range-Slider fürs Jahr
)
def update_graph(option_slctd, country_selected, year_selected, sport_selected, year2_selected):
#1. Diagramm - Datensatz
    dff = df1.copy()
    dff = dff[dff["Country"] == option_slctd]

#1. Diagramm - Diagramm erstellen
    fig = px.bar(dff, x='Year', y=['Bronze', 'Silver', 'Gold'],
                 color_discrete_map={'Bronze': 'orange', 'Silver': 'silver', 'Gold': 'gold'},
                 labels=dict(value="Number of medals won", year="Year", variable="Medal"),
                 title="Medals won by selected country")
    fig.update_xaxes(dtick=4)
    fig.update_xaxes(title_font=dict(size=18, color='crimson'))
    fig.update_yaxes(title_font=dict(size=18, color='crimson'))

#2. Diagramm - Datensatz
    df2 = df.copy()
    df2['Bronze'] = np.where(df2['Medal'] == 'Bronze', 1, 0)
    df2['Silver'] = np.where(df2['Medal'] == 'Silver', 1, 0)
    df2['Gold'] = np.where(df2['Medal'] == 'Gold', 1, 0)
    country = country_selected
    year1 = year_selected[0]
    year2 = year_selected[1]
    df2 = df2[df2['Country'] == country]
    df2 = df2[df2['Year'] >= year1]
    df2 = df2[df2['Year'] <= year2]
    df2['Count']= df2.groupby(by='Sport')['Sport'].transform('count')
    df2 = df2.sort_values(by=['Count'], ascending=False)

#2. Diagramm - Diagramm erstellen
    fig2 = px.bar(df2, x='Sport', y=['Bronze', 'Silver', 'Gold'],
                  color_discrete_map={'Bronze': 'orange', 'Silver': 'silver', 'Gold': 'gold'},
                  category_orders={'variable':['Bronze','Silver','Gold']},
                  labels=dict(value="Number of medals won", Sport="Sport", variable="Medal"),
                  title="Medals won by selected country in selected year(s) - hover over entries for further details",
                  hover_name = 'Athlete',           #Coole Funktion: Wenn man übers Diagramm fährt kommen customized Infos
                  hover_data={'value':False,
                              'Sport':True,
                              'Discipline':True,
                              'Event':True,
                              'Year': True,
                              'City': True,
                              }
                  )
    fig2.update_xaxes(title_font=dict(size=18, color='crimson'))
    fig2.update_yaxes(title_font=dict(size=18, color='crimson'))

#3. Diagramm - Datensatz
    df3 = df.copy()
    df3['Gold'] = np.where(df3['Medal'] == 'Gold', 1, 0)
    sport = sport_selected
    year3 = year2_selected[0]
    year4 = year2_selected[1]
    df3 = df3[df3['Gold'] == 1]
    df3 = df3[df3['Sport'] == sport]
    df3 = df3[df3['Year'] >= year3]
    df3 = df3[df3['Year'] <= year4]

#3. Diagramm - Diagramm erstellen
    fig3 = px.pie(df3, values='Gold', names='Country',)
    fig3.update_traces(textposition='inside', textinfo='percent+label')
    fig3.update(layout_showlegend=False)
    fig3.update_layout(title_text='Gold medals won by selected country in selected year(s)', title_x=0.5)
    fig3.update_layout(margin=dict(t=50, b=0, l=0, r=0))

#Returns (Achtung auf Reihenfolge)
    return fig, fig2, fig3  #Komma zwingend, muss ein Tupel sein


if __name__ == '__main__':
    app.run_server(debug=True)