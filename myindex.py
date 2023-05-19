from dash import html, dcc, dash, Dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash_bootstrap_templates import load_figure_template

load_figure_template("zephyr")

from app import *
from componentes import sidebar, dashboards, extratos

app = Dash(
    external_stylesheets=[dbc.themes.ZEPHYR]
)
server = app.server

# =========  Layout   =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Row([
            dbc.Col([
                html.H5('Linha 1, coluna 1')
            ]),
            dbc.Col([
                html.H5('Linha 1, coluna 2')
            ]),
            dbc.Col([
                html.H5('Linha 1, coluna 3')
            ])
        ], style={'background-color': 'red', 'height': '3vh'}),
        dbc.Row([dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
        ], md=2),
        dbc.Col([
            html.H5('Linha 2, coluna 2'),
            content
        ], md=10)
        ])        
    ])

], fluid=True)

# =========  Callback   =========== #
@app.callback(Output('page-content','children'), [Input('url', 'pathname')])
def render_page(pathname):
    if pathname == '/' or pathname =='/dashboards':
        return dashboards.layout
    
    if pathname == '/extratos':
        return extratos.layout

# =========  Server Run  =========== #

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)