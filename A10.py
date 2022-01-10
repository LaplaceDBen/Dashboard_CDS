import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import datetime
from dash import dcc
import dash
from dash.dependencies import Input, Output
from dash import dash_table
from dash import html as html

df = pd.read_csv(r'.\Summer-Olympic-medals-1976-to-2008.csv', encoding="utf-8")
df1 = pd.read_csv(r'.\summary.csv', encoding="utf-8") #Zusammenfassung des grossen Datensatzes
print(df.info())

app = dash.Dash(__name__)
#Aufgabe 46
#https://dash.plotly.com/datatable/filtering
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
    app.layout = html.Div([

        dcc.RadioItems(
            id='filter-query-read-write',
            options=[
                {'label': 'Read filter_query', 'value': 'read'},
                {'label': 'Write to filter_query', 'value': 'write'}
            ],
            value='read'
        ),

        html.Br(),

        dcc.Input(id='filter-query-input', placeholder='Enter filter query'),

        html.Div(id='filter-query-output'),

        html.Hr(),

        dash_table.DataTable(
            id='datatable-advanced-filtering',
            columns=[
                {'name': i, 'id': i, 'deletable': True} for i in df.columns
                # omit the id column
                if i != 'id'
            ],
            data=df.to_dict('records'),
            editable=True,
            page_action='native',
            page_size=10,
            filter_action="native"
        ),
        html.Hr(),
        html.Div(id='datatable-query-structure', style={'whitespace': 'pre'})
    ])

    @app.callback(
        Output('filter-query-input', 'style'),
        Output('filter-query-output', 'style'),
        Input('filter-query-read-write', 'value')
    )
    def query_input_output(val):
        input_style = {'width': '100%'}
        output_style = {}
        if val == 'read':
            input_style.update(display='none')
            output_style.update(display='inline-block')
        else:
            input_style.update(display='inline-block')
            output_style.update(display='none')
        return input_style, output_style

    @app.callback(
        Output('datatable-advanced-filtering', 'filter_query'),
        Input('filter-query-input', 'value')
    )
    def write_query(query):
        if query is None:
            return ''
        return query

    @app.callback(
        Output('filter-query-output', 'children'),
        Input('datatable-advanced-filtering', 'filter_query')
    )
    def read_query(query):
        if query is None:
            return "No filter query"
        return dcc.Markdown('`filter_query = "{}"`'.format(query))

    @app.callback(
        Output('datatable-query-structure', 'children'),
        Input('datatable-advanced-filtering', 'derived_filter_query_structure')
    )
    def display_query(query):
        if query is None:
            return ''
        return html.Details([
            html.Summary('Derived filter query structure'),
            html.Div(dcc.Markdown('''```json
    {}
    ```'''.format(json.dumps(query, indent=4))))
        ])
def A_48(df):
    app.layout = dash_table.DataTable(
        columns=[
            {'name': 'Country', 'id': 'Country', 'type': 'text'},
            {'name': 'Bronze', 'id': 'Bronze', 'type': 'numeric'},
            {'name': 'Silver', 'id': 'Silver', 'type': 'numeric'},
            {'name': 'Gold', 'id': 'Gold', 'type': 'numeric'}
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
if __name__ == '__main__':
    #A_46(df)
    #A_47(df)
    #A_48(df1)
    app.run_server(debug=True)