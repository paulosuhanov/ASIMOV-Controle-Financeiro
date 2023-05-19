import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd






# ========= Layout ========= #
layout = dbc.Col([
            dbc.Card([
                html.H2("MinhaCarteira", className="text-primary"),
                html.P("Por Paulo Felix", className="text-info"),
                html.Hr(),
            ]),
    #====== Sessão Perfil
            dbc.Button(id='button-avatar',
                        children=[
                            html.Img(
                                src='/assets/img_hom.png', 
                                id='avatar_change', 
                                alt='Avatar', 
                                className='perfil_avatar'
                            )], style={
                                'background-color': 'transparent', 
                                'border-color': 'transparent'}
                        ),
    #====== Sessão Nova Receita e Despesas
            dbc.Row([
                dbc.Col([
                    dbc.Button(
                        color='success', 
                        id='open-nova-receita',
                        children=['+ Receita'])
                ], md=6),
                dbc.Col([
                    dbc.Button(
                        color='danger', 
                        id='open-nova-despensa',
                        children=['- Despensa'])
                ], md=6),
            ]),

            # Modal Receita

            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle('Adicionar Receita')),
                dbc.ModalBody([

                ])
            ], id='modal-novo-receita'),

            # Modal Despesa
            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle('Adicionar Despesa')),
                dbc.ModalBody([

                ])
            ], id='modal-novo-despesa'),



            html.Hr(),
    #====== Sessão Navegação
            dbc.Nav([
                dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
                dbc.NavLink("Extratos", href="/extratos", active="exact"),
            ], vertical=True, pills=True, id="nav_buttons", style={"margin-bottom": "50px"}
            ),

        ], id='sidebar_completa')





# =========  Callbacks  =========== #
# Pop-up receita
@app.callback(
    Output('modal-nova-receita', 'is_open'),
    Input('open-nova-receita', 'n_click'),
    State('modal-novo-receita', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open

# Pop-up despesa
@app.callback(
    Output('modal-nova-despesa', 'is_open'),
    Input('open-nova-despesa', 'n_click'),
    State('modal-novo-despesa', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open