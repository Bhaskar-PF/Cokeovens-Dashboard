import dash
from dash import dcc
from dash import html , callback
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import os
import json
import re
#
import plotly.offline as pyo
import datetime
#

from datetime import timedelta
from datetime import date
import dash_auth
from datetime import datetime as dt
import numpy as np

from datetime import datetime
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
import plotly.offline as pyo
import plotly.express as px
from dash import dash_table
import dash_extensions as de
import time
import re
import schedule
import threading

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"

app = dash.Dash(__name__,external_stylesheets=[ FONT_AWESOME, dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}],
                            update_title=None
                            )
server=app.server
app.title="JSW Steel-Coke Ovens"
app.config.suppress_callback_exceptions=True

VALID_USERNAME_PASSWORD_PAIRS = {
    'jsw': '12345'
}

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

JSW_LOGO = "https://upload.wikimedia.org/wikipedia/en/3/3c/JSW_Group_logo.svg"

header=html.Div([
    html.Img(src=JSW_LOGO,height="100px",style={'margin':"0 20px 50px 0", 'display' : 'inline'}),
    html.H1(
        "Coke Ovens, CDQ & CDQ-PP Dashboard",
        style={"margin-bottom": "0px", 'color': '#FF1700', 'fontSize': 70, 'display' : 'inline'},
    )
], style={'textAlign': 'center', 'padding':'10px 0 0 0'}
)
card_safety = dbc.CardGroup(
    [
        dbc.Card(
            [
                dbc.CardHeader([html.H1(children='Safety Performance',className='cards-md')]),
                dbc.CardBody(
                    [
                        html.Div([
                            dbc.RadioItems(
                                    id='safety_input',
                                    className="btn-group",
                                    labelClassName="btn btn-secondary",
                                    labelCheckedClassName="active",
                                    options=[
                                        {"label": "LTI-Days", "value": 1},
                                        {"label": "Details", "value": 2},
                                    ],
                                    value=1,
                                ),
                        ],
                        className="radio-group",style={'display':'inline'}
                            ),
                        html.Div(id='safety_output',style={'margin-top':'25px'})
                    ]
                )
            ],
            color='#fff'
        ),
        dbc.Card(
            [
            dbc.CardBody([
                html.Div([html.I(className='fas fa-hard-hat fa-3x',style={'width':'30px','color':'yellow','margin':'100px 0 0 5px'})])
            ]),
            ],
            className="cards-ico",
            style={"maxWidth": 85},
            )
    ],
    className="shadow mt-2",
)
card1 = dbc.CardGroup(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                         html.Div([
                            html.H1(id='sp_power',children='54.6',
                            className='cards-big',
                            style={'display': 'inline'}),
                            html.H5(children='kWh/T',
                            style={
                            'display': 'inline',
                            'padding-left':'2px'
                            },
                            className='cards-small')
                         ]),
                        html.H5(children='Sp. Power Consumption',
                        style={
                        'display': 'inline',
                        'color':'#FF3F00',
                        },
                        className='cards-small pr-1',
                        )
                    ]
                )
            ],
            color='#fff'
        ),
        dbc.Card(
            [
            dbc.CardHeader([html.H1(children='Coke 3',className='cards-md')]),
            dbc.CardBody([
                html.Div([html.I(className='fas fa-bolt fa-3x',style={'width':'30px','color':'yellow','margin':'3px 0 0 15px'})])
            ]),
            ],
            className="cards-ico",
            style={"maxWidth": 85},
            )
    ],

    className="shadow",
)
card2 = dbc.CardGroup(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                         html.Div([
                            html.H1(id='sp_water',children='0.8',
                            className='cards-big',
                            style={'display': 'inline'}),
                            html.H5(children='kL/T',
                            style={
                            'display': 'inline',
                            'padding-left':'2px'
                            },
                            className='cards-small')
                         ]),
                        html.H5(children='Sp. Water Consumption',
                        style={
                        'display': 'inline',
                        'color':'#FF3F00',
                        },
                        className='cards-small pr-1',
                        )
                    ]
                )
            ],
            color='#fff'
        ),
        dbc.Card(
            [
            dbc.CardHeader([html.H1(children='Coke 3',className='cards-md')]),
            dbc.CardBody([
                html.Div([html.I(className='fas fa-tint fa-3x',style={'width':'30px','color':'#5DADF1','margin':'3px 0 0 10px'})])
            ]),
            ],
            className="cards-ico",
            style={"maxWidth": 85},
            )
    ],
    className="shadow",
)
card3 = dbc.CardGroup(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                         html.Div([
                            html.H1(id='sp_gas',children='0.827',
                            className='cards-big',
                            style={'display': 'inline'}),
                            html.H5(children='G',
                            style={
                            'display': 'inline',
                            'padding-left':'2px'
                            },
                            className='cards-small')
                         ]),
                        html.H5(children='Sp. Heat Consumption',
                        style={
                        'display': 'inline',
                        'color':'#FF3F00',
                        },
                        className='cards-small pr-1',
                        )
                    ]
                )
            ],
            color='#fff'
        ),
        dbc.Card(
            [
            dbc.CardHeader([html.H1(children='Coke 3',className='cards-md')]),
            dbc.CardBody([
                html.Div([html.I(className='fas fa-fire fa-3x',style={'width':'30px','color':' #F73718','margin':'3px 0 0 10px'})])
            ]),
            ],
            className="cards-ico",
            style={"maxWidth": 85},
            )
    ],
    className="shadow",
)
card11 = dbc.CardGroup(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                         html.Div([
                            html.H1(id='sp_power',children='54.6',
                            className='cards-big',
                            style={'display': 'inline'}),
                            html.H5(children='kWh/T',
                            style={
                            'display': 'inline',
                            'padding-left':'2px'
                            },
                            className='cards-small')
                         ]),
                        html.H5(children='Sp. Power Consumption',
                        style={
                        'display': 'inline',
                        'color':'#FF3F00',
                        },
                        className='cards-small pr-1',
                        )
                    ]
                )
            ],
            color='#fff'
        ),
        dbc.Card(
            [
            dbc.CardHeader([html.H1(children='Coke 4',className='cards-md')]),
            dbc.CardBody([
                html.Div([html.I(className='fas fa-bolt fa-3x',style={'width':'30px','color':'yellow','margin':'3px 0 0 15px'})])
            ]),
            ],
            className="cards-ico",
            style={"maxWidth": 85},
            )
    ],

    className="shadow",
)
card22 = dbc.CardGroup(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                         html.Div([
                            html.H1(id='sp_water',children='0.8',
                            className='cards-big',
                            style={'display': 'inline'}),
                            html.H5(children='kL/T',
                            style={
                            'display': 'inline',
                            'padding-left':'2px'
                            },
                            className='cards-small')
                         ]),
                        html.H5(children='Sp. Water Consumption',
                        style={
                        'display': 'inline',
                        'color':'#FF3F00',
                        },
                        className='cards-small pr-1',
                        )
                    ]
                )
            ],
            color='#fff'
        ),
        dbc.Card(
            [
            dbc.CardHeader([html.H1(children='Coke 4',className='cards-md')]),
            dbc.CardBody([
                html.Div([html.I(className='fas fa-tint fa-3x',style={'width':'30px','color':'#5DADF1','margin':'3px 0 0 10px'})])
            ]),
            ],
            className="cards-ico",
            style={"maxWidth": 85},
            )
    ],
    className="shadow",
)

card33 = dbc.CardGroup(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                         html.Div([
                            html.H1(id='sp_gas',children='0.827',
                            className='cards-big',
                            style={'display': 'inline'}),
                            html.H5(children='G',
                            style={
                            'display': 'inline',
                            'padding-left':'2px'
                            },
                            className='cards-small')
                         ]),
                        html.H5(children='Sp. Heat Consumption',
                        style={
                        'display': 'inline',
                        'color':'#FF3F00',
                        },
                        className='cards-small pr-1',
                        )
                    ]
                )
            ],
            color='#fff'
        ),
        dbc.Card(
            [
            dbc.CardHeader([html.H1(children='Coke 4',className='cards-md')]),
            dbc.CardBody([
                html.Div([html.I(className='fas fa-fire fa-3x',style={'width':'30px','color':' #F73718','margin':'3px 0 0 10px'})])
            ]),
            ],
            className="cards-ico",
            style={"maxWidth": 85},
            )
    ],
    className="shadow",
)

card111 = dbc.CardGroup(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                         html.Div([
                            html.H1(id='sp_power',children='54.6',
                            className='cards-big',
                            style={'display': 'inline'}),
                            html.H5(children='kWh/T',
                            style={
                            'display': 'inline',
                            'padding-left':'2px'
                            },
                            className='cards-small')
                         ]),
                        html.H5(children='Sp. Power Consumption',
                        style={
                        'display': 'inline',
                        'color':'#FF3F00',
                        },
                        className='cards-small pr-1',
                        )
                    ]
                )
            ],
            color='#fff'
        ),
        dbc.Card(
            [
            dbc.CardHeader([html.H1(children='Coke 5',className='cards-md')]),
            dbc.CardBody([
                html.Div([html.I(className='fas fa-bolt fa-3x',style={'width':'30px','color':'yellow','margin':'3px 0 0 15px'})])
            ]),
            ],
            className="cards-ico",
            style={"maxWidth": 85},
            )
    ],

    className="shadow",
)


card222 = dbc.CardGroup(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                         html.Div([
                            html.H1(id='sp_water', children='0.8',
                            className='cards-big',
                            style={'display': 'inline'}),
                            html.H5(children='kL/T',
                            style={
                            'display': 'inline',
                            'padding-left':'2px'
                            },
                            className='cards-small')
                         ]),
                        html.H5(children='Sp. Water Consumption',
                        style={
                        'display': 'inline',
                        'color':'#FF3F00',
                        },
                        className='cards-small pr-1',
                        )
                    ]
                )
            ],
            color='#fff'
        ),
        dbc.Card(
            [
            dbc.CardHeader([html.H1(children='Coke 5', className='cards-md')]),
            dbc.CardBody([
                html.Div([html.I(className='fas fa-tint fa-3x', style={'width':'30px','color':'#5DADF1','margin':'3px 0 0 10px'})])
            ]),
            ],
            className="cards-ico",
            style={"maxWidth": 85},
            )
    ],
    className="shadow",
)

card333 = dbc.CardGroup(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                         html.Div([
                            html.H1(id='sp_gas', children='0.827',
                            className='cards-big',
                            style={'display': 'inline'}),
                            html.H5(children='G',
                            style={
                            'display': 'inline',
                            'padding-left':'2px'
                            },
                            className='cards-small')
                         ]),
                        html.H5(children='Sp. Heat Consumption',
                        style={
                        'display': 'inline',
                        'color':'#FF3F00',
                        },
                        className='cards-small pr-1',
                        )
                    ]
                )
            ],
            color='#fff'
        ),
        dbc.Card(
            [
            dbc.CardHeader([html.H1(children='Coke 5', className='cards-md')]),
            dbc.CardBody([
                html.Div([html.I(className='fas fa-fire fa-3x', style={'width':'30px','color':' #F73718','margin':'3px 0 0 10px'})])
            ]),
            ],
            className="cards-ico",
            style={"maxWidth": 85},
            )
    ],
    className="shadow",
)

'''-------------layout---------------'''
#Production Layout
app.layout=dbc.Container([
    dbc.Row([
        dbc.Col([
            header,
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card(
                [
                dbc.CardHeader([
                dbc.Row([
                    dbc.Col([
                        html.H1(['I. Production Section',],className='SubHeading_dashboard', style={'text-align': 'left', 'margin':'0', 'display' :'inline'}),
                    ]),
                    dbc.Col([
                        dcc.DatePickerSingle(
                               id='date_input_main',
                               display_format='MMM Do, YY',
                               style={'width':'auto', 'display' :'inline'}
                           ),
                    ], align = 'center', className = 'text-end')
                ])
                ]),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardHeader([html.H1(children='Daily, Monthly & Annual Trends ',className='cards-md')]),
                                dbc.CardBody([
                                        html.Div([
                                            html.Div([
                                                dbc.RadioItems(
                                                        id='graph_type',
                                                        className="btn-group",
                                                        labelClassName="btn btn-secondary",
                                                        labelCheckedClassName="active",
                                                        options=[
                                                            {"label": "Tonnage", "value": 1},
                                                            {"label": "Pushings", "value": 2},
                                                            {"label": "Yield", "value": 3},
                                                            {"label": "CDQ Power", "value": 4},
                                                        ],
                                                        value=1,
                                                    ),
                                            ],

                                            className="radio-group"
                                                ),
                                            html.Div(id='graph_tab_output',className="radio-group")
                                        ], style = {'display':'flex', 'justify-content':'space-between'}),
                                        dcc.Loading(children=[html.Div(id='production_output_div',style={'margin-top':'50px'})],
                                        type='cube',color='red',fullscreen=False)
                                ],style={'margin':'35px 0 0 0'})
                                ],
                                color='#fff',
                                style={'width':'auto','height':'800px','padding':'0','margin':'0'})
                        ],
                        # width=5,
                        xl = 5,
                        # md = 12
                        ),
                        dbc.Col([
                            dbc.Row([
                                dbc.Col([
                                    dbc.Card([
                                        dbc.CardHeader([html.H1(children='Coke 3|Coal Blend Distribution',className='cards-md')]),
                                        dbc.CardBody([
                                            html.Div([
                                                dbc.RadioItems(
                                                        id='blend_details3',
                                                        className="btn-group",
                                                        labelClassName="btn btn-secondary",
                                                        labelCheckedClassName="active",
                                                        options=[
                                                            {"label": "Distribution", "value": 1},
                                                            {"label": "Details", "value": 2},
                                                        ],
                                                        value=1,
                                                    ),
                                            ],
                                            className="radio-group",style={'display':'inline'}
                                                ),
                                            html.Div(id='coal_blend_3',style={'margin-top':'25px'})
                                        ])
                                        ],
                                        color='#fff',
                                        className='mb-1',
                                        style={'width':'auto','height':'auto','padding':'0','margin':'0'}),
                                ],xl=4),
                                dbc.Col([
                                    dbc.Card([
                                        dbc.CardHeader([html.H1(children='Coke 4|Coal Blend Distribution',className='cards-md')]),
                                        dbc.CardBody([
                                            html.Div([
                                                dbc.RadioItems(
                                                        id='blend_details4',
                                                        className="btn-group",
                                                        labelClassName="btn btn-secondary",
                                                        labelCheckedClassName="active",
                                                        options=[
                                                            {"label": "Distribution", "value": 1},
                                                            {"label": "Details", "value": 2},
                                                        ],
                                                        value=1,
                                                    ),
                                            ],
                                            className="radio-group",style={'display':'inline'}
                                                ),
                                            html.Div(id='coal_blend_4',style={'margin-top':'25px'})
                                        ])
                                        ],
                                        color='#fff',
                                        className='mb-1',
                                        style={'width':'auto','height':'auto','padding':'0','margin':'0'}),
                                ],xl=4),
                                dbc.Col([
                                    dbc.Card([
                                        dbc.CardHeader([html.H1(children='Coke 5|Coal Blend Distribution',className='cards-md')]),
                                        dbc.CardBody([
                                            html.Div([
                                                dbc.RadioItems(
                                                        id='blend_details5',
                                                        className="btn-group",
                                                        labelClassName="btn btn-secondary",
                                                        labelCheckedClassName="active",
                                                        options=[
                                                            {"label": "Distribution", "value": 1},
                                                            {"label": "Details", "value": 2},
                                                        ],
                                                        value=1,
                                                    ),
                                            ],
                                            className="radio-group",style={'display':'inline'}
                                                ),
                                            html.Div(id='coal_blend_5',style={'margin-top':'25px'})
                                        ])
                                        ],
                                        color='#fff',
                                        className='mb-1',
                                        style={'width':'auto','height':'auto','padding':'0','margin':'0'}),
                                ],xl=4)
                            ]),
                        dbc.Row([
                            dbc.Col([
                                dbc.CardLink([
                                    dbc.Card([
                                        dbc.CardBody([
                                            html.H1(children='Pushings',className='cards-big',style={'color':'green'}),
                                            html.Div([
                                                html.H1('Coke 3',style={'display':'inline'},className='cards-small-pushing'),
                                                html.H1( id='coke3_pushing_number', style={'display':'inline'},className='cards-big-pushing'),
                                            ],style={'display':'block'}),
                                            html.Div([
                                                html.H1('Coke 4',style={'display':'inline'},className='cards-small-pushing'),
                                                html.H1(id='coke4_pushing_number', style={'display':'inline'},className='cards-big-pushing'),
                                            ],style={'display':'block'}),
                                            html.Div([
                                                html.H1('Coke 5',style={'display':'inline'},className='cards-small-pushing'),
                                                html.H1(id='coke5_pushing_number', style={'display':'inline'},className='cards-big-pushing'),
                                            ],style={'display':'block'}),
                                        ])
                                        ],
                                        color='#fff',
                                        className='mb-1 mt-2 ml-2',
                                        style={'width':'auto','height':'auto','padding':'0','margin':'0'}),
                                    dbc.Card([
                                        dbc.CardBody([
                                            html.H1(children='Dry-Wet Pushings',className='cards-big',style={'color':'green'}),
                                            dcc.Loading(children=[dcc.Graph( id='Dry_Wet',style=dict(width='auto',height='225px'),
                                            config={"displayModeBar": False, "showTips": False}
                                            )],
                                            type='cube',color='red',fullscreen=False),
                                        ])
                                        ],
                                        color='#fff',
                                        className='mb-1 mt-2 ml-3',
                                        style={'width':'auto','height':'auto','padding':'0','margin':'0'}),
                                    dbc.Card([
                                        html.Div([
                                            html.H1('CDQ Power',className='cards-big mt-1 ml-2',style={'color':'green'}),
                                            html.Div([
                                                html.H1(id='cdq_power_number',style={'display':'inline'},className='cards-big-pushing'),
                                                html.H1('MWh',style={'display':'inline'},className='cards-small-cdq'),
                                            ],style={'display':'block'}),
                                        ],style={'padding':'16px 0 0 10px'}),
                                        dcc.Loading(children=[dcc.Graph( id='cdq_power', style=dict(width='auto',height='150px'),
                                        config={"displayModeBar": False, "showTips": False}
                                        )],
                                        type='cube',color='red',fullscreen=False),
                                        ],
                                        color='#fff',
                                        className='mb-1 mt-2 ml-3 mr-2',
                                        style={'width':'auto','height':'auto','padding':'0','margin':'0'}),
                                ])
                            ],width=12),
                            ]),
                        ],
                        # width=7,
                        # md = 12,
                        xl = 7
                        )
                    ]),
                    dbc.Row([
                    dbc.Col([
                            card_safety
                            ],xl=3),
                    dbc.Col([
                                dbc.CardGroup([
                                    dbc.Card([
                                        dbc.CardBody([
                                            html.H1(children='CSR',className='cards-big mt-1',style={'color':'green'}),
                                            dcc.Loading(children=[dcc.Graph( id='CSR',style=dict(width='200px',height='50px'),
                                            config={"displayModeBar": False, "showTips": False}
                                            )],
                                            type='cube',color='red',fullscreen=False),
                                            html.H1(children='Yield',className='cards-big mt-1',style={'color':'green'}),
                                            dcc.Loading(children=[dcc.Graph( id='Yield',style=dict(width='200px',height='50px'),
                                            config={"displayModeBar": False, "showTips": False}
                                            )],
                                            type='cube',color='red',fullscreen=False),
                                            html.H1(children='Quality Index',className='cards-big mt-1',style={'color':'green'}),
                                            dcc.Loading(children=[dcc.Graph( id='quality_index',style=dict(width='200px',height='50px'),
                                            config={"displayModeBar": False, "showTips": False}
                                            )],
                                            type='cube',color='red',fullscreen=False),
                                        ])
                                        ],
                                        color='#fff',
                                        className='mb-1 mt-2',
                                        style={'width':'auto','height':'auto','padding':'0','margin':'0'}),
                                    dbc.Card([
                                        dbc.CardBody([
                                            html.H1(children='Sp. Power Cons.',className='cards-big mt-1',style={'color':'green'}),
                                            dcc.Loading(children=[dcc.Graph( id='sp_power_graph', style=dict(width='200px',height='50px'),
                                            config={"displayModeBar": False, "showTips": False}
                                            )],
                                            type='cube',color='red',fullscreen=False),
                                            html.H1(children='Sp. Steam Cons',className='cards-big mt-1',style={'color':'green'}),
                                            dcc.Loading(children=[dcc.Graph( id='sp_steam_graph', style=dict(width='200px',height='50px'),
                                            config={"displayModeBar": False, "showTips": False}
                                            )],
                                            type='cube',color='red',fullscreen=False),
                                            html.H1(children='Sp. Gas Cons',className='cards-big mt-1',style={'color':'green'}),
                                            dcc.Loading(children=[dcc.Graph( id='sp_gas_graph',style=dict(width='200px',height='50px'),
                                            config={"displayModeBar": False, "showTips": False}
                                            )],
                                            type='cube',color='red',fullscreen=False),
                                        ])
                                        ],
                                        color='#fff',
                                        className='mb-1 mt-2',
                                        style={'width':'auto','height':'auto','padding':'0','margin':'0'}),
                                    dbc.Card([
                                        dbc.CardBody([
                                            html.H1(children='Tar Generation',className='cards-big mt-1',style={'color':'green'}),
                                            dcc.Loading(children=[dcc.Graph( id='tar_gen',style=dict(width='200px',height='50px'),
                                            config={"displayModeBar": False, "showTips": False}
                                            )],
                                            type='cube',color='red',fullscreen=False),
                                            # html.H1(children='Gas Generation',className='cards-big mt-1',style={'color':'green'}),
                                            # dcc.Loading(children=[dcc.Graph( id='gas_gen',style=dict(width='200px',height='50px'),
                                            # config={"displayModeBar": False, "showTips": False}
                                            # )],
                                            # type='cube',color='red',fullscreen=False),
                                            html.H1(children='Steam Generation',className='cards-big mt-1',style={'color':'green'}),
                                            dcc.Loading(children=[dcc.Graph( id='steam_gen',style=dict(width='200px',height='50px'),
                                            config={"displayModeBar": False, "showTips": False}
                                            )],
                                            type='cube',color='red',fullscreen=False),
                                        ])
                                        ],
                                        color='#fff',
                                        className='mb-1 mt-2',
                                        style={'width':'auto','height':'auto','padding':'0','margin':'0'}),
                                ])
                            ],xl=9)]),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Card([
                                        dbc.CardHeader([html.H1(children='Daily Delay Report',className='cards-md')]),
                                        dbc.CardBody([
                                            html.Div(id='delay_div', style={'padding':'2rem 2rem'})
                                        ])
                                        ],
                                        color='#fff',
                                        className='mb-1 mt-2',
                                        style={'width':'auto','height':'auto','padding':'0','margin':'0'})
                                ], width=12)
                            ]),
                ])
                ]
            )
        ], style={'margin-bottom':'1rem'})
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([ html.H1(['II. Quality Section'],className='SubHeading_dashboard', style={'text-align': 'left', 'margin':'0rem 0 0rem 0'})]),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                # dbc.CardHeader([html.H1(children='Daily Delay Report',className='cards-md')]),
                                dbc.CardBody([
                                    html.Div([
                                        dbc.RadioItems(
                                                id='tab_selection',
                                                className="btn-group",
                                                labelClassName="btn btn-secondary",
                                                labelCheckedClassName="active",
                                                options=[
                                                    {"label": "Quality Index", "value": '1'},
                                                    {"label": "CSR", "value": '2'},
                                                    {"label": "Coke Fines Generation", "value": '3'},
                                                    {"label": "MPS", "value": '4'},
                                                ],
                                                value='1',
                                            ),
                                    ],
                                    className="radio-group",style={'display':'inline'}
                                        ),
                                    dcc.Loading(children=[html.Div(id='tab_selection_div',style={'background-color' : 'white', 'padding': '1rem 6rem 3rem 6rem'})],
                                    type='cube',color='red',fullscreen=False),
                                    dcc.Loading(children=[html.Div(id='quality_parameter_div',style={'background-color' : 'white', 'padding': '1rem 6rem 3rem 6rem'})],
                                    type='cube',color='red',fullscreen=False)
                                ])
                                ],
                                color='#fff',
                                className='mb-1 mt-2 pt-4',
                                style={'width':'auto','height':'auto','padding':'0','margin':'0'})

                        ], width=12),
                    ]),
                ])
            ])
        ], style={'margin-bottom':'1rem'})
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([html.H1(['III. Cost Section'],className='SubHeading_dashboard', style={'text-align': 'left', 'margin':'0rem 0 0rem 0'})]),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                html.Div([
                                    dbc.RadioItems(
                                            id='tab_selection_cost',
                                            className="btn-group",
                                            labelClassName="btn btn-secondary",
                                            labelCheckedClassName="active",
                                            options=[
                                                {"label": "Sp. Power Consumption", "value": '1'},
                                                {"label": "Sp. Steam Consumption", "value": '2'},
                                                {"label": "Sp. Gas Consumption", "value": '3'},
                                                {"label": "Blend Cost", "value": '4'},
                                            ],
                                            value='1',
                                        ),
                                ],
                                className="radio-group",style={'display':'inline'}
                                    ),
                                    dcc.Loading(children=[html.Div(id='tab_selection_cost_div', style={'background-color' : 'white', 'padding': '1rem 6rem 2rem 6rem'})],
                                    type='cube',color='red',fullscreen=False)
                                ])
                                ],
                                color='#fff',
                                className='mb-1 mt-2 pt-4',
                                style={'width':'auto','height':'auto','padding':'0','margin':'0'})

                        ], width=12),
                    ]),
                ])
            ])
        ])
    ])
],
fluid=True,
className='dashboard_container')

#Setting intial date equals to current date
@app.callback(Output('date_input_main', 'date'), Input('date_input_main', 'date'))
def current_Date(date_value):
    if date_value == None:
        return dt.date(dt.today())
    else:
        return date_value

#Production numbers coke3 & coke4
@app.callback(
    Output('coke3_pushing_number', 'children'),
    Output('coke4_pushing_number', 'children'),
    Output('coke5_pushing_number', 'children'),
    Output('cdq_power_number', 'children'),
    Output('CSR', 'figure'),
    Output('Yield', 'figure'),
    Output('quality_index', 'figure'),
    Output('sp_power_graph', 'figure'),
    Output('sp_steam_graph', 'figure'),
    Output('sp_gas_graph', 'figure'),
    Output('tar_gen', 'figure'),
    # Output('gas_gen', 'figure'),
    Output('steam_gen', 'figure'),
    Output('cdq_power', 'figure'),
    Output('Dry_Wet', 'figure'),
    Input('production','clickData')
    )
def pushing_number(n):
    if n == None:
        date= dt.today().replace(hour=0, minute=0, second=0, microsecond=0) -timedelta(days=1)
        date_minus_2days= dt.today().replace(hour=0, minute=0, second=0, microsecond=0) -timedelta(days=2)

    else:
        date=dt.strptime(n['points'][0]['x'], '%Y-%m-%d')
        date_minus_2days = date -timedelta(days=1)
    df_1=pd.read_csv('./datasets/CSV/TE Data/DM Data.csv',parse_dates=['Month'])
    df_1.rename(columns={'CO #3.5':'CO3_sp_power',
                         'CO #4.5':'CO4_sp_power',
                         'CO #5.5':'CO5_sp_power',
                         'CO #3.6':'CO3_sp_steam',
                         'CO #4.6':'CO4_sp_steam',
                         'CO #5.6':'CO5_sp_steam',
                         'CO #3.7':'CO3_sp_gas',
                         'CO #4.7':'CO4_sp_gas',
                         'CO #5.7':'CO5_sp_gas',
                         'CO #3.8':'CO3_sp_tar',
                         'CO #4.8':'CO4_sp_tar',
                         'CO #5.8':'CO5_sp_tar',
                         'CDQ':'coke3_dry',
                         'Wet ':'coke3_wet',
                         'Total':'total3',
                         'CDQ.1':'coke4_dry',
                         'Wet .1':'coke4_wet',
                         'Total.1':'total4',
                         'CDQ.2':'coke5_dry',
                         'Wet.2':'coke5_wet',
                         'Total.2':'total5',
                            }, inplace=True)

    df_1=df_1[['Month', '3 Pushings', '4 Pushings', '5 Pushings','CDQ POWER GEN', '3 CSR', '4 CSR', '5 CSR','3 Quality Index',
     '4 Quality Index', '5 Quality Index', '3 Yield', '4 Yield', '5 Yield','CO3_sp_power', 'CO4_sp_power', 'CO5_sp_power','CO3_sp_steam', 'CO4_sp_steam', 'CO5_sp_steam',
      'CO3_sp_gas', 'CO4_sp_gas', 'CO5_sp_gas','CO3_sp_tar', 'CO4_sp_tar', 'CO5_sp_tar','CDQ 1&2', 'CDQ 3&4', 'CDQ 5&6','coke3_dry', 'coke3_wet', 'total3', 'coke4_dry', 'coke4_wet', 'total4','coke5_dry', 'coke5_wet', 'total5']]
    df_1_filter=df_1.loc[df_1['Month'] == date, :].reset_index(drop=True)
    df_1_filter_minus_2days=df_1.loc[df_1['Month'] == date_minus_2days, :].reset_index(drop=True)


    df_1_filter.fillna(0, inplace=True)
    
    if not(df_1_filter.empty):
        coke3_number=int(df_1_filter.iloc[0,1])
        coke4_number=int(df_1_filter.iloc[0,2])
        coke5_number=int(df_1_filter.iloc[0,3])
        cdq_power_number=df_1_filter.iloc[0,4].round(1)
       
    else:
        coke3_number='--'
        coke4_number='--'
        coke5_number='--'
        cdq_power_number='--'

    #Dataframe for CDQ POWER
    df_2=df_1.loc[df_1['Month'].between((date-timedelta(days=15)), date), :]

    #CDQ Power scatter plot
    data=go.Scatter(
        x=df_2['Month'],
        y=df_2['CDQ POWER GEN'],
        mode='lines',
        fill='tozeroy',
        line={'shape': 'spline', 'smoothing': 1}
    )
    fig_cdq=go.Figure(data=data,layout=go.Layout(plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                    margin={'t':0.3,'l':0,'r':0,'b':0},
                    xaxis=dict(linecolor='#fff',visible=False, showgrid=False),
                    yaxis=dict(linecolor='#fff',visible=False,showgrid=False),
                    font=dict(size=15),
                    showlegend=False))

    data_sp_power_3=go.Bar(
        y=['Coke 3'],
        x=df_1_filter['CO3_sp_power'].astype(float).astype(int),
        text=df_1_filter['CO3_sp_power'].astype(float).astype(int),
        textposition='inside',
        orientation='h'
    )
    data_sp_power_4=go.Bar(
        y=['Coke 4'],
        x=df_1_filter['CO4_sp_power'].astype(float).astype(int),
        text=df_1_filter['CO4_sp_power'].astype(float).astype(int),
        textposition='inside',
        orientation='h'
    )
    data_sp_power_5=go.Bar(
        y=['Coke 5'],
        x=df_1_filter['CO5_sp_power'].astype(float).astype(int),
        text=df_1_filter['CO5_sp_power'].astype(float).astype(int),
        textposition='inside',
        orientation='h'
    )
    fig_sp_power=go.Figure(data=[data_sp_power_3,data_sp_power_4,data_sp_power_5],layout=go.Layout(plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                    margin={'t': 0,'l':0,'r':0,'b':0},
                    xaxis=dict(range=[45,65],linecolor='#fff',visible=False, showgrid=False),
                    yaxis=dict(linecolor='#fff',visible=True,showgrid=False),
                    font=dict(size=12),
                    showlegend=False))
    fig_sp_power.update_layout(legend=dict(yanchor='top', y=0.99,  xanchor='left', x=0.01) )
    fig_sp_power.update_layout(hovermode="x unified")

    data_sp_steam_3=go.Bar(
        y=['Coke 3'],
        x=df_1_filter['CO3_sp_steam'].astype(float),
        text=df_1_filter['CO3_sp_steam'].astype(float).round(3),
        textposition='inside',
        orientation='h'
    )
    data_sp_steam_4=go.Bar(
        y=['Coke 4'],
        x=df_1_filter['CO4_sp_steam'].astype(float),
        text=df_1_filter['CO4_sp_steam'].astype(float).round(3),
        textposition='inside',
        orientation='h'
    )
    data_sp_steam_5=go.Bar(
        y=['Coke 5'],
        x=df_1_filter['CO5_sp_steam'].astype(float),
        text=df_1_filter['CO5_sp_steam'].astype(float).round(3),
        textposition='inside',
        orientation='h'
    )
    fig_sp_steam=go.Figure(data=[data_sp_steam_3,data_sp_steam_4,data_sp_steam_5],layout=go.Layout(plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                    margin={'t': 0,'l':0,'r':0,'b':0},
                    xaxis=dict(range=[0,0.5],linecolor='#fff',visible=False, showgrid=False),
                    yaxis=dict(linecolor='#fff',visible=True,showgrid=False),
                    font=dict(size=12),
                    showlegend=False))
    fig_sp_steam.update_layout(legend=dict(yanchor='top', y=0.99,  xanchor='left', x=0.01) )
    fig_sp_steam.update_layout(hovermode="x unified")
    data_sp_gas_3=go.Bar(
        y=['Coke 3'],
        x=df_1_filter_minus_2days['CO3_sp_gas'].astype(float),
        text=df_1_filter_minus_2days['CO3_sp_gas'].astype(float).round(3),
        textposition='inside',
        orientation='h'
    )
    data_sp_gas_4=go.Bar(
        y=['Coke 4'],
        x=df_1_filter_minus_2days['CO4_sp_gas'].astype(float),
        text=df_1_filter_minus_2days['CO4_sp_gas'].astype(float).round(3),
        textposition='inside',
        orientation='h'
    )
    data_sp_gas_5=go.Bar(
        y=['Coke 5'],
        x=df_1_filter_minus_2days['CO5_sp_gas'].astype(float),
        text=df_1_filter_minus_2days['CO5_sp_gas'].astype(float).round(3),
        textposition='inside',
        orientation='h'
    )
    fig_sp_gas=go.Figure(data=[data_sp_gas_3,data_sp_gas_4,data_sp_gas_5],layout=go.Layout(plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                    margin={'t': 0,'l':0,'r':0,'b':0},
                    xaxis=dict(range=[0.55,0.7],linecolor='#fff',visible=False, showgrid=False),
                    yaxis=dict(linecolor='#fff',visible=True,showgrid=False),
                    font=dict(size=12),
                    showlegend=False))
    fig_sp_gas.update_layout(legend=dict(yanchor='top', y=0.99,  xanchor='left', x=0.01) )
    fig_sp_gas.update_layout(hovermode="x unified")

    data_gen_tar_3=go.Bar(
        y=['Coke 3'],
        x=df_1_filter['CO3_sp_tar'].astype(float).astype(int),
        text=df_1_filter['CO3_sp_tar'].astype(float).astype(int),
        textposition='inside',
        orientation='h'
    )
    data_gen_tar_4=go.Bar(
        y=['Coke 4'],
        x=df_1_filter['CO4_sp_tar'].astype(float).astype(int),
        text=df_1_filter['CO4_sp_tar'].astype(float).astype(int),
        textposition='inside',
        orientation='h'
    )
    data_gen_tar_5=go.Bar(
        y=['Coke 5'],
        x=df_1_filter['CO5_sp_tar'].astype(float).astype(int),
        text=df_1_filter['CO5_sp_tar'].astype(float).astype(int),
        textposition='inside',
        orientation='h'
    )
    fig_gen_tar=go.Figure(data=[data_gen_tar_3,data_gen_tar_4,data_gen_tar_5],layout=go.Layout(plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                    margin={'t': 0,'l':0,'r':0,'b':0},
                    xaxis=dict(linecolor='#fff',visible=False, showgrid=False),
                    yaxis=dict(linecolor='#fff',visible=True,showgrid=False),
                    font=dict(size=12),
                    showlegend=False))
    fig_gen_tar.update_layout(legend=dict(yanchor='top', y=0.99,  xanchor='left', x=0.01) )
    fig_gen_tar.update_layout(hovermode="x unified")

    data_gen_gas_3=go.Bar(
        y=['Coke 3'],
        x=[351],
        text='351',
        textposition='inside',
        orientation='h'
    )
    data_gen_gas_4=go.Bar(
        y=['Coke 4'],
        x=[348],
        text='348',
        textposition='inside',
        orientation='h'
    )
    data_gen_gas_5=go.Bar(
        y=['Coke 5'],
        x=[348],
        text='348',
        textposition='inside',
        orientation='h'
    )
    fig_gen_gas=go.Figure(data=[data_gen_gas_3,data_gen_gas_4,data_gen_gas_5],layout=go.Layout(plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                    margin={'t': 0,'l':0,'r':0,'b':0},
                    xaxis=dict(linecolor='#fff',visible=False, showgrid=False),
                    yaxis=dict(linecolor='#fff',visible=True,showgrid=False),
                    font=dict(size=12),
                    showlegend=False))
    fig_gen_gas.update_layout(legend=dict(yanchor='top', y=0.99,  xanchor='left', x=0.01) )
    fig_gen_gas.update_layout(hovermode="x unified")

    data_gen_steam_3=go.Bar(
        y=['Coke 3'],
        x=df_1_filter['CDQ 1&2'].astype(float).astype(int),
        text=df_1_filter['CDQ 1&2'].astype(float).astype(int),
        textposition='inside',
        orientation='h'
    )
    data_gen_steam_4=go.Bar(
        y=['Coke 4'],
        x=df_1_filter['CDQ 3&4'].astype(float).astype(int),
        text=df_1_filter['CDQ 3&4'].astype(float).astype(int),
        textposition='inside',
        orientation='h'
    )
    data_gen_steam_5=go.Bar(
        y=['Coke 5'],
        x=df_1_filter['CDQ 5&6'].astype(float).astype(int),
        text=df_1_filter['CDQ 5&6'].astype(float).astype(int),
        textposition='inside',
        orientation='h'
    )
    fig_gen_steam=go.Figure(data=[data_gen_steam_3, data_gen_steam_4,data_gen_steam_5],layout=go.Layout(plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                    margin={'t': 0,'l':0,'r':0,'b':0},
                    xaxis=dict(linecolor='#fff',visible=False, showgrid=False),
                    yaxis=dict(linecolor='#fff',visible=True,showgrid=False),
                    font=dict(size=12),
                    showlegend=False))
    fig_gen_steam.update_layout(legend=dict(yanchor='top', y=0.99,  xanchor='left', x=0.01) )
    fig_gen_steam.update_layout(hovermode="x unified")

    data31=go.Bar(
        y=['Coke 3'],
        x=df_1_filter['3 CSR'].astype(float).astype(int),
        text=df_1_filter['3 CSR'].astype(float).astype(int),
        textposition='inside',
        orientation='h'
    )
    data41=go.Bar(
        y=['Coke 4'],
        x=df_1_filter['4 CSR'].astype(float).astype(int),
        text=df_1_filter['4 CSR'].astype(float).astype(int),
        textposition='inside',
        orientation='h'
        # mode='lines',
        # line={'shape': 'spline', 'smoothing': 1}
    )
    data51=go.Bar(
        y=['Coke 5'],
        x=df_1_filter['5 CSR'].astype(float).astype(int),
        text=df_1_filter['5 CSR'].astype(float).astype(int),
        textposition='inside',
        orientation='h'
        # mode='lines',
        # line={'shape': 'spline', 'smoothing': 1}
    )
    data32=go.Bar(
        y=['Coke 3'],
        x=df_1_filter['3 Quality Index'].astype(float),
        text=df_1_filter['3 Quality Index'].astype(float).round(3),
        textposition='inside',
        orientation='h'
        # mode='lines',
        # line={'shape': 'spline', 'smoothing': 1}
    )
    data42=go.Bar(
        y=['Coke 4'],
        x=df_1_filter['4 Quality Index'].astype(float),
        text=df_1_filter['4 Quality Index'].astype(float).round(3),
        textposition='inside',
        orientation='h'
        # mode='lines',
        # line={'shape': 'spline', 'smoothing': 1}
    )
    data52=go.Bar(
        y=['Coke 5'],
        x=df_1_filter['5 Quality Index'].astype(float),
        text=df_1_filter['5 Quality Index'].astype(float).round(3),
        textposition='inside',
        orientation='h'
        # mode='lines',
        # line={'shape': 'spline', 'smoothing': 1}
    )

    data3_yield=go.Bar(
        y=['Coke 3'],
        x=df_1_filter['3 Yield'].astype(float).astype(int),
        text=df_1_filter['3 Yield'].astype(float).astype(int),
        textposition='inside',
        orientation='h'
        # mode='lines',
        # line={'shape': 'spline', 'smoothing': 1}
    )
    data4_yield=go.Bar(
        y=['Coke 4'],
        x=df_1_filter['4 Yield'].astype(float).astype(int),
        text=df_1_filter['4 Yield'].astype(float).astype(int),
        textposition='inside',
        orientation='h'
        # mode='lines',
        # line={'shape': 'spline', 'smoothing': 1}
    )
    data5_yield=go.Bar(
        y=['Coke 5'],
        x=df_1_filter['5 Yield'].astype(float).astype(int),
        text=df_1_filter['5 Yield'].astype(float).astype(int),
        textposition='inside',
        orientation='h'
        # mode='lines',
        # line={'shape': 'spline', 'smoothing': 1}
    )

    fig_csr=go.Figure(data=[data31,data41,data51],layout=go.Layout(plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                    margin={'t': 0,'l':0,'r':0,'b':0},
                    xaxis=dict(range=[60,70], linecolor='#fff', visible=False, showgrid=False),
                    yaxis=dict(linecolor='#fff',visible=True,showgrid=False),
                    font=dict(size=12),
                    showlegend=False))

    fig_csr.update_layout(legend=dict(yanchor='top', y=0.99,  xanchor='left', x=0.01) )
    fig_csr.update_layout(hovermode="x unified")
    fig_quality=go.Figure(data=[data32,data42,data52],layout=go.Layout(plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                    margin={'t': 0,'l':0,'r':0,'b':0},
                    xaxis=dict(linecolor='#fff',visible=False, showgrid=False),
                    yaxis=dict(linecolor='#fff',visible=True,showgrid=False),
                    font=dict(size=12),
                    showlegend=False))
    fig_yield=go.Figure(data=[data3_yield,data4_yield,data5_yield],layout=go.Layout(plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                    margin={'t': 0,'l':0,'r':0,'b':0},
                    xaxis=dict(range=[65,80],linecolor='#fff',visible=False, showgrid=False),
                    yaxis=dict(linecolor='#fff',visible=True,showgrid=False),
                    font=dict(size=12),
                    showlegend=False))
    fig_quality.update_layout(legend=dict(yanchor='top', y=0.99,  xanchor='left', x=0.01) )
    fig_quality.update_layout(hovermode="x unified")

    '''-----------dry vs wet---------------'''
    data_dry_wet3=go.Bar(
        x=['CDQ 1&2','CDQ 3&4','CDQ 5&6'],
        y=[df_1_filter.loc[0, 'coke3_dry'], df_1_filter.loc[0, 'coke4_dry'], df_1_filter.loc[0, 'coke5_dry']],
        text=[df_1_filter.loc[0, 'coke3_dry'].astype(int), df_1_filter.loc[0, 'coke4_dry'].astype(int), df_1_filter.loc[0, 'coke5_dry'].astype(int)],
        name='Dry',
        textposition='inside',
    )
    data_dry_wet4=go.Bar(
        x=['CDQ 1&2','CDQ 3&4','CDQ 5&6'],
        y=[df_1_filter.loc[0, 'coke3_wet'].astype(int), df_1_filter.loc[0, 'coke4_wet'].astype(int)],
        name='Wet',
        text=[df_1_filter.loc[0, 'coke3_wet'].astype(int), df_1_filter.loc[0, 'coke4_wet'].astype(int), df_1_filter.loc[0, 'coke5_wet'].astype(int)],
        textposition='outside',
    )
    
    fig_dry_wet=go.Figure(data=[data_dry_wet3,data_dry_wet4],layout=go.Layout(plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                    margin={'t': 0,'l':0,'r':0,'b':0},
                    barmode='stack',
                    xaxis=dict(linecolor='#fff',visible=True, showgrid=False),
                    yaxis=dict(linecolor='#fff',visible=True,showgrid=False),
                    font=dict(size=15),
                    showlegend=True))

    fig_dry_wet.update_layout(hovermode="x unified")
    fig_dry_wet.update_yaxes(range=[50,400])


    return coke3_number, coke4_number,coke5_number , cdq_power_number, fig_csr, fig_yield, fig_quality, fig_sp_power, fig_sp_steam, fig_sp_gas, fig_gen_tar, fig_gen_steam, fig_cdq, fig_dry_wet
    # fig_gen_gas,



@app.callback(Output('graph_tab_output','children'),
              Input('graph_type','value'))
def graph_type(tab):
    if tab==1:
        tab_selection=[
            dbc.RadioItems(
                    id='overall_coke3_coke4_coke5',
                    className="btn-group",
                    labelClassName="btn btn-secondary",
                    labelCheckedClassName="active",
                    options=[
                        {"label": "Overall", "value": 1},
                        {"label": "Coke-3", "value": 2},
                        {"label": "Coke-4", "value": 3},
                        {"label": "Coke-5", "value": 4},
                    ],
                    value=1,
                )
        ]
    elif tab==2:
        tab_selection=[
            dbc.RadioItems(
                    id='overall_coke3_coke4_coke5',
                    className="btn-group",
                    labelClassName="btn btn-secondary",
                    labelCheckedClassName="active",
                    options=[
                        {"label": "Coke-3", "value": 1},
                        {"label": "Coke-4", "value": 2},
                        {"label": "Coke-5", "value": 3},
                    ],
                    value=2,
                )
        ]
    elif tab==3:
        tab_selection=[
            dbc.RadioItems(
                    id='overall_coke3_coke4_coke5',
                    className="btn-group",
                    labelClassName="btn btn-secondary",
                    labelCheckedClassName="active",
                    options=[
                        {"label": "Coke-3", "value": 1},
                        {"label": "Coke-4", "value": 2},
                        {"label": "Coke-5", "value": 3},
                    ],
                    value=2,
                )
        ]
    elif tab==4:
        tab_selection=None


    return tab_selection


@app.callback(Output('production_output_div','children'),
             Input('graph_type','value'),
             Input('overall_coke3_coke4_coke5','value'), Input('date_input_main', 'date'))
def production(graph_type,graph_area, date_value):
    df_1=pd.read_csv('./datasets/CSV/TE Data/DM Data.csv',parse_dates=['Month'])
    # df_1.dropna(thresh=10,inplace=True,axis=1)
    # for c in df_1.columns[:88]:
    #     if c!='Month':
    #         df_1[c].replace(['-',' -','#DIV/0!'],0,inplace=True)
    #         df_1[c]=df_1[c].astype(float)
    #         df_1[c]=df_1[c].apply(lambda x: round(x,1))
    # date=dt.today().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
    date=dt.strptime(date_value, '%Y-%m-%d') - timedelta(days=1)

    df_1.fillna(0, inplace=True)
    df_1=df_1.loc[df_1['Month']<= date, :]
    fig=None
    df_1.rename(columns={'CO 3.2':'breakdown3','CO 4.2':'breakdown4', 'CO 5.2':'breakdown5','CO 3.3':'shutdown3','CO 4.3':'shutdown4', 'CO 5.3':'shutdown5',
                        '3 Pushings.1':'3pushings_target', '4 Pushings.1':'4pushings_target', '5 Pushings.1':'5pushings_target',
                        '3 Yield.1':'3yield_target', '4 Yield.1':'4yield_target', '5 Yield.1':'5yield_target',
                        'CDQ POWER GEN.1':'cdq_power_target'
                        }, inplace=True)

    if graph_type==1:
        if graph_area==1:
            fig = make_subplots(rows=2, cols=2,
                        vertical_spacing=0.2,
                        horizontal_spacing=0.1,
                        column_widths=[0.2, 0.8],
                        row_heights=[0.4,0.6],
                        specs=[[{}, {}],
                       [{"colspan": 2}, None]],
                    )

            df1=df_1.loc[df_1['Month'].between((date-timedelta(days=15)), date)]
            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['Total Prod Actual'],
                # hover_data=df1['breakdown4'],
                # mode='lines',
                name='Actual',
                # fill='tozeroy',
                mode='lines+markers',
                # text=df1['Total Prod Actual'],
                # textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                    color='#0F52BA',
                    width=2
                )
                ),
                line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )

            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['MP Total'],
                # mode='lines',
                name='Planned',
                mode='lines+markers',
                marker=dict(color='white',
                line=dict(
                    color='red',
                    width=2
                )
                ),
                # text=df1['MP Total'],
                # textposition='bottom center',
                # fill='tozeroy',
                line={'color':'red','shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )

            df2=df_1
            df2.index=df2.Month

            df2['MP Total']=df2['MP Total'].apply(lambda x: round(x))
            df2['Total Prod Actual']=df2['Total Prod Actual'].apply(lambda x: round(x))
            #grouping by month
            df2 = df2.groupby(pd.Grouper(freq="M")).sum()
            df2=df2.tail(12)
            df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]
            fig.add_trace(go.Bar(
                x=df2.index.astype(str),
                y=df2['MP Total'],
                name='Planned'
                ),row=1,col=2
                )
            fig.add_trace(go.Bar(
                x=df2.index.astype(str),
                y=df2['Total Prod Actual'],
                # textposition='outside',
                # text=df2['Total Prod Actual'],
                name='Actual'
                ),row=1,col=2
                )

            df3=df_1
            df3.index=range(df_1.shape[0])
            #Retriving year from dates
            df3.Month=df3.Month.apply(lambda x: x.year)
            #grouping by year
            df3=df3.groupby('Month').sum()
            a=df3.index.values.tolist()
            index=["FY-{}".format(str(x)[-2:]) for x in a]
            df3.index=index
            #Making subplots
            fig.add_trace(go.Bar(
                x=df3.index.astype(str),
                y=df3['MP Total'],
                # mode='lines',
                name='Planned'
                ),row=1,col=1
                )
            fig.add_trace(go.Bar(
                x=df3.index.astype(str),
                y=df3['Total Prod Actual'],
                # mode='lines',
                name='Actual'
                ),row=1,col=1
                )
            max_value = df1['MP Total'].max()
            min_value = df1['MP Total'].min()
            max_monthly_value = df2['MP Total'].max()
            min_monthly_value = df2['MP Total'].min()
            max_yearly_value = df3['MP Total'].max()
            min_yearly_value = df3['MP Total'].min()
            fig.update_yaxes(row=2, col=1, range=[min_value -1000,max_value + 1000], showgrid=False)
            fig.update_yaxes(row=1, col=2, range=[min_monthly_value -10000, max_monthly_value + 10000],  showgrid=False)
            fig.update_yaxes(row=1, col=1, range=[0,max_yearly_value + 200000],  showgrid=False)
        elif graph_area==2:
            fig = make_subplots(rows=2, cols=2,
                        vertical_spacing=0.2,
                        horizontal_spacing=0.1,
                        column_widths=[0.2, 0.8],
                        row_heights=[0.4,0.6],
                        specs=[[{}, {}],
                       [{"colspan": 2}, None]],
                    # subplot_titles=("Pusher side[{}]".format(oven), "Coke side[{}]".format(oven),
                    # "Pusher side[{}]".format(ovenplus),"Coke side[{}]".format(ovenplus)),
                    )
            df1=df_1.loc[df_1['Month'].between((date-timedelta(days=15)), date)]
            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['3 Prod Actual'],
                name='Actual',
                # fill='tozeroy',
                mode='lines+markers',
                # text=df1['Total Prod Actual'],
                # textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                    color='#0F52BA',
                    width=2
                )
                ),
                line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )
            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['3 MP'],
                name='Planned',
                mode='lines+markers',
                marker=dict(color='white',
                line=dict(
                    color='red',
                    width=2
                )
                ),
                # text=df1['MP Total'],
                # textposition='bottom center',
                # fill='tozeroy',
                line={'color':'red','shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )
            df2=df_1
            df2.index=df2.Month
            #grouping by month
            df2 = df2.groupby(pd.Grouper(freq="M")).sum()
            df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]
            df2=df2.tail(12)
            fig.add_trace(go.Bar(
                x=df2.index.astype(str),
                y=df2['3 MP'],
                # mode='lines',
                name='Planned'
                ),row=1,col=2
                )
            fig.add_trace(go.Bar(
                x=df2.index.astype(str),
                y=df2['3 Prod Actual'],
                # mode='lines',
                name='Actual'
                ),row=1,col=2
                )
            df3=df_1
            df3.index=range(df_1.shape[0])
            #Retriving year from dates
            df3.Month=df3.Month.apply(lambda x: x.year)
            #grouping by year
            df3=df3.groupby('Month').sum()
            a=df3.index.values.tolist()
            index=["FY-{}".format(str(x)[-2:]) for x in a]
            df3.index=index
            #Making subplots
            fig.add_trace(go.Bar(
                x=df3.index.astype(str),
                y=df3['3 MP'],
                # mode='lines',
                name='Planned'
                ),row=1,col=1
                )
            fig.add_trace(go.Bar(
                x=df3.index.astype(str),
                y=df3['3 Prod Actual'],
                # mode='lines',
                name='Actual'
                ),row=1,col=1
                )
            max_value = df1['3 MP'].max()
            min_value = df1['3 MP'].min()
            max_monthly_value = df2['3 MP'].max()
            min_monthly_value = df2['3 MP'].min()
            max_yearly_value = df3['3 MP'].max()
            min_yearly_value = df3['3 MP'].min()
            fig.update_yaxes(row=2, col=1, range=[min_value -1000,max_value + 1000], showgrid=False)
            fig.update_yaxes(row=1, col=2, range=[min_monthly_value -10000, max_monthly_value + 10000],  showgrid=False)
            fig.update_yaxes(row=1, col=1, range=[0,max_yearly_value + 200000],  showgrid=False)
        elif graph_area==3:
            fig = make_subplots(rows=2, cols=2,
                        vertical_spacing=0.2,
                        horizontal_spacing=0.1,
                        column_widths=[0.2, 0.8],
                        row_heights=[0.4,0.6],
                        specs=[[{}, {}],
                       [{"colspan": 2}, None]],
                    # subplot_titles=("Pusher side[{}]".format(oven), "Coke side[{}]".format(oven),
                    # "Pusher side[{}]".format(ovenplus),"Coke side[{}]".format(ovenplus)),
                    )
            df1=df_1.loc[df_1['Month'].between((date-timedelta(days=15)), date)]
            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['4 Prod Actual'],
                name='Actual',
                # fill='tozeroy',
                mode='lines+markers',
                # text=df1['Total Prod Actual'],
                # textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                    color='#0F52BA',
                    width=2
                )
                ),
                line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )
            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['4 MP'],
                name='Planned',
                mode='lines+markers',
                marker=dict(color='white',
                line=dict(
                    color='red',
                    width=2
                )
                ),
                # text=df1['MP Total'],
                # textposition='bottom center',
                # fill='tozeroy',
                line={'color':'red','shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )

            df2=df_1
            df2.index=df2.Month
            #grouping by month
            df2 = df2.groupby(pd.Grouper(freq="M")).sum()
            df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]
            df2=df2.tail(12)
            fig.add_trace(go.Bar(
                x=df2.index.astype(str),
                y=df2['4 MP'],
                name='Planned'
                ),row=1,col=2
                )
            fig.add_trace(go.Bar(
                x=df2.index.astype(str),
                y=df2['4 Prod Actual'],
                name='Actual'
                ),row=1,col=2
                )
            df3=df_1
            df3.index=range(df_1.shape[0])
            #Retriving year from dates
            df3.Month=df3.Month.apply(lambda x: x.year)
            #grouping by year
            df3=df3.groupby('Month').sum()
            a=df3.index.values.tolist()
            index=["FY-{}".format(str(x)[-2:]) for x in a]
            df3.index=index
            #Making subplots

            fig.add_trace(go.Bar(
                x=df3.index.astype(str),
                y=df3['4 MP'],
                name='Planned'
                ),row=1,col=1
                )
            fig.add_trace(go.Bar(
                x=df3.index.astype(str),
                y=df3['4 Prod Actual'],
                name='Actual'
                ),row=1,col=1
                )
            max_value = df1['4 MP'].max()
            min_value = df1['4 MP'].min()
            max_monthly_value = df2['4 MP'].max()
            min_monthly_value = df2['4 MP'].min()
            max_yearly_value = df3['4 MP'].max()
            min_yearly_value = df3['4 MP'].min()
            fig.update_yaxes(row=2, col=1, range=[min_value -1000,max_value + 1000], showgrid=False)
            fig.update_yaxes(row=1, col=2, range=[min_monthly_value -10000, max_monthly_value + 10000],  showgrid=False)
            fig.update_yaxes(row=1, col=1, range=[0,max_yearly_value + 200000],  showgrid=False)
        #Coke5  
        elif graph_area==4:
            fig = make_subplots(rows=2, cols=2,
                        vertical_spacing=0.2,
                        horizontal_spacing=0.1,
                        column_widths=[0.2, 0.8],
                        row_heights=[0.4,0.6],
                        specs=[[{}, {}],
                       [{"colspan": 2}, None]],
                    # subplot_titles=("Pusher side[{}]".format(oven), "Coke side[{}]".format(oven),
                    # "Pusher side[{}]".format(ovenplus),"Coke side[{}]".format(ovenplus)),
                    )
            df1=df_1.loc[df_1['Month'].between((date-timedelta(days=15)), date)]
            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['5 Prod Actual'],
                name='Actual',
                # fill='tozeroy',
                mode='lines+markers',
                # text=df1['Total Prod Actual'],
                # textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                    color='#0F52BA',
                    width=2
                )
                ),
                line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )
            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['5 MP'],
                name='Planned',
                mode='lines+markers',
                marker=dict(color='white',
                line=dict(
                    color='red',
                    width=2
                )
                ),
                # text=df1['MP Total'],
                # textposition='bottom center',
                # fill='tozeroy',
                line={'color':'red','shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )

            df2=df_1
            df2.index=df2.Month
            #grouping by month
            df2 = df2.groupby(pd.Grouper(freq="M")).sum()
            df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]
            df2=df2.tail(12)
            fig.add_trace(go.Bar(
                x=df2.index.astype(str),
                y=df2['5 MP'],
                name='Planned'
                ),row=1,col=2
                )
            fig.add_trace(go.Bar(
                x=df2.index.astype(str),
                y=df2['5 Prod Actual'],
                name='Actual'
                ),row=1,col=2
                )
            df3=df_1
            df3.index=range(df_1.shape[0])
            #Retriving year from dates
            df3.Month=df3.Month.apply(lambda x: x.year)
            #grouping by year
            df3=df3.groupby('Month').sum()
            a=df3.index.values.tolist()
            index=["FY-{}".format(str(x)[-2:]) for x in a]
            df3.index=index
            #Making subplots

            fig.add_trace(go.Bar(
                x=df3.index.astype(str),
                y=df3['5 MP'],
                name='Planned'
                ),row=1,col=1
                )
            fig.add_trace(go.Bar(
                x=df3.index.astype(str),
                y=df3['5 Prod Actual'],
                name='Actual'
                ),row=1,col=1
                )
            max_value = df1['5 MP'].max()
            min_value = df1['5 MP'].min()
            max_monthly_value = df2['5 MP'].max()
            min_monthly_value = df2['5 MP'].min()
            max_yearly_value = df3['5 MP'].max()
            min_yearly_value = df3['5 MP'].min()
            fig.update_yaxes(row=2, col=1, range=[min_value -1000,max_value + 1000], showgrid=False)
            fig.update_yaxes(row=1, col=2, range=[min_monthly_value -10000, max_monthly_value + 10000],  showgrid=False)
            fig.update_yaxes(row=1, col=1, range=[0,max_yearly_value + 200000],  showgrid=False)      
    elif graph_type==2:
        if graph_area==1:
            fig = make_subplots(rows=2, cols=2,
                        vertical_spacing=0.2,
                        horizontal_spacing=0.1,
                        column_widths=[0.2, 0.8],
                        row_heights=[0.5,0.5],
                        specs=[[{}, {}],
                       [{"colspan": 2}, None]],
                    # subplot_titles=("Pusher side[{}]".format(oven), "Coke side[{}]".format(oven),
                    # "Pusher side[{}]".format(ovenplus),"Coke side[{}]".format(ovenplus)),
                    )
            df1=df_1.loc[df_1['Month'].between((date-timedelta(days=15)), date)]

            df1['3 Pushings']=df1['3 Pushings'].apply(lambda x: int(x))
            df1['3pushings_target']=df1['3pushings_target'].apply(lambda x: int(x))

            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['3pushings_target'],
                name='Target pushing',
                mode='lines+markers',
                text=df1['3pushings_target'],
                # textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                    color='red',
                    width=2
                )
                ),
                # fill='tozeroy',
                line={'color':'red','shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )

            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['3 Pushings'],
                name='Actual pushing',
                mode='lines+markers+text',
                text=df1['3 Pushings'],
                textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                    color='#0F52BA',
                    width=2
                )
                ),
                # fill='tozeroy',
                line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )

            df2=df_1
            df2.index=df2.Month
            #grouping by month
            df2 = df2.groupby(pd.Grouper(freq="M")).mean().round(2)
            df2=df2.tail(12)
            df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]
            df2=df2.tail(12)
            fig.add_trace(go.Bar(
                x=df2.index.astype(str),
                y=df2['3 Pushings'],
                name = 'Monthly Mean Pushings',
                text=df2['3 Pushings'].round(0).astype(int),
                textposition='outside',
                # mode='lines',
                ),row=1,col=2
                )
            df3=df_1
            df3.index=range(df_1.shape[0])
            #Retriving year from dates
            df3.Month=df3.Month.apply(lambda x: x.year)
            #grouping by year
            df3=df3.groupby('Month').mean().round(2)
            a=df3.index.values.tolist()
            index=["FY-{}".format(str(x)[-2:]) for x in a]
            df3.index=index
            #Making subplots
            fig.add_trace(go.Bar(
                x=df3.index.astype(str),
                y=df3['3 Pushings'],
                name = 'Annual Mean Pushings',
                text=df3['3 Pushings'].round(0).astype(int),
                textposition='outside',
                # mode='lines',
                ),row=1,col=1
                )
            max_value = df1['3 Pushings'].max()
            min_value = df1['3 Pushings'].min()
            max_monthly_value = df2['3 Pushings'].max()
            min_monthly_value = df2['3 Pushings'].min()
            fig.update_yaxes(row=2, col=1, range=[min_value -20,max_value + 20], showgrid=False)
            fig.update_yaxes(row=1, col=2, range=[min_monthly_value -20,max_monthly_value + 20],  showgrid=False)
            fig.update_yaxes(row=1, col=1,range=[min_monthly_value -20,max_monthly_value + 20],  showgrid=False)

        elif graph_area==2:
            fig = make_subplots(rows=2, cols=2,
                        vertical_spacing=0.2,
                        horizontal_spacing=0.1,
                        column_widths=[0.2, 0.8],
                        row_heights=[0.5,0.5],
                        specs=[[{}, {}],
                       [{"colspan": 2}, None]],
                    # subplot_titles=("Pusher side[{}]".format(oven), "Coke side[{}]".format(oven),
                    # "Pusher side[{}]".format(ovenplus),"Coke side[{}]".format(ovenplus)),
                    )
            df1=df_1.loc[df_1['Month'].between((date-timedelta(days=15)), date)]
            df1['4 Pushings']=df1['4 Pushings'].apply(lambda x: int(x))
            df1['4pushings_target']=df1['4pushings_target'].apply(lambda x: int(x))

            fig.add_trace(go.Scatter(
                                x=df1.Month.astype(str),
                                y=df1['4pushings_target'],
                                name='Target pushing',
                                mode='lines+markers',
                                text=df1['4pushings_target'],
                                # textposition='bottom center',
                                marker=dict(color='white',
                                line=dict(
                                    color='red',
                                    width=2
                                )
                                ),
                                # fill='tozeroy',
                                line={'color':'red','shape': 'spline', 'smoothing': 1}
                                ),row=2,col=1
                                )


            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['4 Pushings'],
                name='Actual pushing',
                mode='lines+markers+text',
                text=df1['4 Pushings'],
                textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                    color='#0F52BA',
                    width=2
                )
                ),
                # fill='tozeroy',
                line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )
            df2=df_1
            df2.index=df2.Month
            #grouping by month
            df2 = df2.groupby(pd.Grouper(freq="M")).mean().round(2)
            df2=df2.tail(12)
            df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]
            df2=df2.tail(12)
            fig.add_trace(go.Bar(
                x=df2.index.astype(str),
                y=df2['4 Pushings'],
                name = 'Monthly Mean Pushings',
                text=df2['4 Pushings'].round(0).astype(int),
                textposition='outside',
                # mode='lines',
                ),row=1,col=2
                )
            df3=df_1
            df3.index=range(df_1.shape[0])
            #Retriving year from dates
            df3.Month=df3.Month.apply(lambda x: x.year)
            #grouping by year
            df3=df3.groupby('Month').mean().round(2)
            a=df3.index.values.tolist()
            index=["FY-{}".format(str(x)[-2:]) for x in a]
            df3.index=index
            #Making subplots
            fig.add_trace(go.Bar(
                x=df3.index.astype(str),
                y=df3['4 Pushings'],
                name = 'Annual Mean Pushings',
                text=df3['4 Pushings'].round(0).astype(int),
                textposition='outside',
                # mode='lines',
                ),row=1,col=1
                )
            max_value = df1['4 Pushings'].max()
            min_value = df1['4 Pushings'].min()
            max_monthly_value = df2['4 Pushings'].max()
            min_monthly_value = df2['4 Pushings'].min()
            fig.update_yaxes(row=2, col=1, range=[min_value -20,max_value + 20], showgrid=False)
            fig.update_yaxes(row=1, col=2, range=[min_monthly_value -20,max_monthly_value + 20],  showgrid=False)
            fig.update_yaxes(row=1, col=1,range=[min_monthly_value -20,max_monthly_value + 20],  showgrid=False)

            # fig.update_yaxes(row=2, col=1, showgrid=False)
            # fig.update_yaxes(row=1, col=2, showgrid=False)
            # fig.update_yaxes(row=1, col=1, showgrid=False)
        #coke5
        elif graph_area==3:
            fig = make_subplots(rows=2, cols=2,
                        vertical_spacing=0.2,
                        horizontal_spacing=0.1,
                        column_widths=[0.2, 0.8],
                        row_heights=[0.5,0.5],
                        specs=[[{}, {}],
                       [{"colspan": 2}, None]],
                    # subplot_titles=("Pusher side[{}]".format(oven), "Coke side[{}]".format(oven),
                    # "Pusher side[{}]".format(ovenplus),"Coke side[{}]".format(ovenplus)),
                    )
            df1=df_1.loc[df_1['Month'].between((date-timedelta(days=15)), date)]
            df1['5 Pushings']=df1['5 Pushings'].apply(lambda x: int(x))
            df1['5pushings_target']=df1['5pushings_target'].apply(lambda x: int(x))

            fig.add_trace(go.Scatter(
                                x=df1.Month.astype(str),
                                y=df1['5pushings_target'],
                                name='Target pushing',
                                mode='lines+markers',
                                text=df1['5pushings_target'],
                                # textposition='bottom center',
                                marker=dict(color='white',
                                line=dict(
                                    color='red',
                                    width=2
                                )
                                ),
                                # fill='tozeroy',
                                line={'color':'red','shape': 'spline', 'smoothing': 1}
                                ),row=2,col=1
                                )


            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['5 Pushings'],
                name='Actual pushing',
                mode='lines+markers+text',
                text=df1['5 Pushings'],
                textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                    color='#0F52BA',
                    width=2
                )
                ),
                # fill='tozeroy',
                line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )
            df2=df_1
            df2.index=df2.Month
            #grouping by month
            df2 = df2.groupby(pd.Grouper(freq="M")).mean().round(2)
            df2=df2.tail(12)
            df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]
            df2=df2.tail(12)
            fig.add_trace(go.Bar(
                x=df2.index.astype(str),
                y=df2['5 Pushings'],
                name = 'Monthly Mean Pushings',
                text=df2['5 Pushings'].round(0).astype(int),
                textposition='outside',
                # mode='lines',
                ),row=1,col=2
                )
            df3=df_1
            df3.index=range(df_1.shape[0])
            #Retriving year from dates
            df3.Month=df3.Month.apply(lambda x: x.year)
            #grouping by year
            df3=df3.groupby('Month').mean().round(2)
            a=df3.index.values.tolist()
            index=["FY-{}".format(str(x)[-2:]) for x in a]
            df3.index=index
            #Making subplots
            fig.add_trace(go.Bar(
                x=df3.index.astype(str),
                y=df3['5 Pushings'],
                name = 'Annual Mean Pushings',
                text=df3['5 Pushings'].round(0).astype(int),
                textposition='outside',
                # mode='lines',
                ),row=1,col=1
                )
            max_value = df1['5 Pushings'].max()
            min_value = df1['5 Pushings'].min()
            max_monthly_value = df2['5 Pushings'].max()
            min_monthly_value = df2['5 Pushings'].min()
            fig.update_yaxes(row=2, col=1, range=[min_value -20,max_value + 20], showgrid=False)
            fig.update_yaxes(row=1, col=2, range=[min_monthly_value -20,max_monthly_value + 20],  showgrid=False)
            fig.update_yaxes(row=1, col=1,range=[min_monthly_value -20,max_monthly_value + 20],  showgrid=False)         
    if graph_type==3:
        if graph_area==1:
            fig = make_subplots(rows=2, cols=2,
                        vertical_spacing=0.2,
                        horizontal_spacing=0.1,
                        column_widths=[0.2, 0.8],
                        row_heights=[0.5,0.5],
                        specs=[[{}, {}],
                       [{"colspan": 2}, None]],
                    # subplot_titles=("Pusher side[{}]".format(oven), "Coke side[{}]".format(oven),
                    # "Pusher side[{}]".format(ovenplus),"Coke side[{}]".format(ovenplus)),
                    )
            df1=df_1.loc[df_1['Month'].between((date-timedelta(days=15)), date)]
            df1['3 Yield']=df1['3 Yield'].apply(lambda x: round(x,1))
            df1['3yield_target']=df1['3yield_target'].apply(lambda x: round(x,1))

            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['3yield_target'],
                name='Target pushing',
                mode='lines+markers',
                text=df1['3yield_target'],
                # textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                    color='red',
                    width=2
                )
                ),
                # fill='tozeroy',
                line={'color':'red','shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )

            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['3 Yield'],
                name='Yield',
                mode='lines+markers+text',
                text=df1['3 Yield'],
                textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                    color='#0F52BA',
                    width=2
                )
                ),
                # fill='tozeroy',
                line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
                # fill='tozeroy',
                # line={'shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )
            df2=df_1
            df2.index=df2.Month
            #grouping by month
            df2 = df2.groupby(pd.Grouper(freq="M")).mean().round(2)
            df2=df2.tail(12)
            df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]
            df2=df2.tail(12)
            fig.add_trace(go.Bar(
                x=df2.index.astype(str),
                y=df2['3 Yield'],
                name='Monthly yield',
                text=df2['3 Yield'],
                textposition='outside',
                # mode='lines',
                ),row=1,col=2
                )
            df3=df_1
            df3.index=range(df_1.shape[0])
            #Retriving year from dates
            df3.Month=df3.Month.apply(lambda x: x.year)
            #grouping by year
            df3=df3.groupby('Month').mean().round(2)
            a=df3.index.values.tolist()
            index=["FY-{}".format(str(x)[-2:]) for x in a]
            df3.index=index
            #Making subplots
            fig.add_trace(go.Bar(
                x=df3.index.astype(str),
                y=df3['3 Yield'],
                text=df3['3 Yield'],
                name='Annual yield',
                textposition='outside',
                # mode='lines',
                ),row=1,col=1
                )
            max_value = df1['3 Yield'].max()
            min_value = df1['3 Yield'].min()
            max_monthly_value = df2['3 Yield'].max()
            min_monthly_value = df2['3 Yield'].min()
            fig.update_yaxes(row=2, col=1, range=[min_value -5,max_value + 5], showgrid=False)
            fig.update_yaxes(row=1, col=2, range=[min_monthly_value -10,max_monthly_value + 10],  showgrid=False)
            fig.update_yaxes(row=1, col=1,range=[min_monthly_value -10,max_monthly_value + 10],  showgrid=False)

            # fig.update_yaxes(row=2, col=1,  showgrid=False)
            # fig.update_yaxes(row=1, col=2,  showgrid=False)
            # fig.update_yaxes(row=1, col=1,  showgrid=False)
        elif graph_area==2:
            fig = make_subplots(rows=2, cols=2,
                        vertical_spacing=0.2,
                        horizontal_spacing=0.1,
                        column_widths=[0.2, 0.8],
                        row_heights=[0.5,0.5],
                        specs=[[{}, {}],
                       [{"colspan": 2}, None]],
                    # subplot_titles=("Pusher side[{}]".format(oven), "Coke side[{}]".format(oven),
                    # "Pusher side[{}]".format(ovenplus),"Coke side[{}]".format(ovenplus)),
                    )
            df1=df_1.loc[df_1['Month'].between((date-timedelta(days=15)), date)]
            df1['4 Yield']=df1['4 Yield'].apply(lambda x: round(x,1))
            df1['4yield_target']=df1['4yield_target'].apply(lambda x: round(x,1))

            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['4yield_target'],
                name='Target pushing',
                mode='lines+markers',
                text=df1['4yield_target'],
                # textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                    color='red',
                    width=2
                )
                ),
                # fill='tozeroy',
                line={'color':'red','shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )


            max_value = df1['4 Yield'].max()
            min_value = df1['4 Yield'].min()

            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['4 Yield'],
                name='Yield',
                mode='lines+markers+text',
                text=df1['4 Yield'],
                textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                    color='#0F52BA',
                    width=2
                )
                ),
                # fill='tozeroy',
                line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
                # fill='tozeroy',
                # line={'shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )
            df2=df_1
            df2.index=df2.Month
            #grouping by month
            df2 = df2.groupby(pd.Grouper(freq="M")).mean().round(2)
            df2=df2.tail(12)
            df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]

            max_monthly_value = df2['4 Yield'].max()
            min_monthly_value = df2['4 Yield'].min()

            fig.add_trace(go.Bar(
                x=df2.index.astype(str),
                y=df2['4 Yield'],
                text=df2['4 Yield'],
                textposition='outside',
                name = 'Monthly Yield',
                # mode='lines',
                ),row=1,col=2
                )
            df3=df_1
            df3.index=range(df_1.shape[0])
            #Retriving year from dates
            df3.Month=df3.Month.apply(lambda x: x.year)
            #grouping by year
            df3=df3.groupby('Month').mean().round(2)
            a=df3.index.values.tolist()
            index=["FY-{}".format(str(x)[-2:]) for x in a]
            df3.index=index
            #Making subplots
            fig.add_trace(go.Bar(
                x=df3.index.astype(str),
                y=df3['4 Yield'],
                name = 'Annual Yield',
                text=df2['4 Yield'],
                textposition='outside',
                # mode='lines',
                ),row=1,col=1
                )

            # fig.update_yaxes(row=2, col=1,showgrid=False)
            # fig.update_yaxes(row=1, col=2,showgrid=False)
            # fig.update_yaxes(row=1, col=1,showgrid=False)
            fig.update_yaxes(row=2, col=1, range=[min_value -10,max_value + 10], showgrid=False)
            fig.update_yaxes(row=1, col=2, range=[min_monthly_value -10,max_monthly_value + 10],  showgrid=False)
            fig.update_yaxes(row=1, col=1,range=[min_monthly_value -10,max_monthly_value + 10],  showgrid=False)
        #coke5
        elif graph_area==3:
            fig = make_subplots(rows=2, cols=2,
                        vertical_spacing=0.2,
                        horizontal_spacing=0.1,
                        column_widths=[0.2, 0.8],
                        row_heights=[0.5,0.5],
                        specs=[[{}, {}],
                       [{"colspan": 2}, None]],
                    # subplot_titles=("Pusher side[{}]".format(oven), "Coke side[{}]".format(oven),
                    # "Pusher side[{}]".format(ovenplus),"Coke side[{}]".format(ovenplus)),
                    )
            df1=df_1.loc[df_1['Month'].between((date-timedelta(days=15)), date)]
            df1['5 Yield']=df1['5 Yield'].apply(lambda x: round(x,1))
            df1['5yield_target']=df1['5yield_target'].apply(lambda x: round(x,1))

            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['5yield_target'],
                name='Target pushing',
                mode='lines+markers',
                text=df1['5yield_target'],
                # textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                    color='red',
                    width=2
                )
                ),
                # fill='tozeroy',
                line={'color':'red','shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )


            max_value = df1['5 Yield'].max()
            min_value = df1['5 Yield'].min()

            fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['5 Yield'],
                name='Yield',
                mode='lines+markers+text',
                text=df1['5 Yield'],
                textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                    color='#0F52BA',
                    width=2
                )
                ),
                # fill='tozeroy',
                line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
                # fill='tozeroy',
                # line={'shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )
            df2=df_1
            df2.index=df2.Month
            #grouping by month
            df2 = df2.groupby(pd.Grouper(freq="M")).mean().round(2)
            df2=df2.tail(12)
            df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]

            max_monthly_value = df2['5 Yield'].max()
            min_monthly_value = df2['5 Yield'].min()

            fig.add_trace(go.Bar(
                x=df2.index.astype(str),
                y=df2['5 Yield'],
                text=df2['5 Yield'],
                textposition='outside',
                name = 'Monthly Yield',
                # mode='lines',
                ),row=1,col=2
                )
            df3=df_1
            df3.index=range(df_1.shape[0])
            #Retriving year from dates
            df3.Month=df3.Month.apply(lambda x: x.year)
            #grouping by year
            df3=df3.groupby('Month').mean().round(2)
            a=df3.index.values.tolist()
            index=["FY-{}".format(str(x)[-2:]) for x in a]
            df3.index=index
            #Making subplots
            fig.add_trace(go.Bar(
                x=df3.index.astype(str),
                y=df3['5 Yield'],
                name = 'Annual Yield',
                text=df2['5 Yield'],
                textposition='outside',
                # mode='lines',
                ),row=1,col=1
                )

            # fig.update_yaxes(row=2, col=1,showgrid=False)
            # fig.update_yaxes(row=1, col=2,showgrid=False)
            # fig.update_yaxes(row=1, col=1,showgrid=False)
            fig.update_yaxes(row=2, col=1, range=[min_value -10,max_value + 10], showgrid=False)
            fig.update_yaxes(row=1, col=2, range=[min_monthly_value -10,max_monthly_value + 10],  showgrid=False)
            fig.update_yaxes(row=1, col=1,range=[min_monthly_value -10,max_monthly_value + 10],  showgrid=False)        
    if graph_type==4:
        fig = make_subplots(rows=2, cols=2,
                    vertical_spacing=0.2,
                    horizontal_spacing=0.1,
                    column_widths=[0.2, 0.8],
                    row_heights=[0.5,0.5],
                    specs=[[{}, {}],
                   [{"colspan": 2}, None]],
                # subplot_titles=("Pusher side[{}]".format(oven), "Coke side[{}]".format(oven),
                # "Pusher side[{}]".format(ovenplus),"Coke side[{}]".format(ovenplus)),
                )
        df1=df_1.loc[df_1['Month'].between((date-timedelta(days=15)), date)]
        df1['CDQ POWER GEN']=df1['CDQ POWER GEN'].apply(lambda x: round(x,1))
        df1['cdq_power_target']=df1['cdq_power_target'].apply(lambda x: round(x,1))


        max_value = df1['CDQ POWER GEN'].max()
        min_value = df1['CDQ POWER GEN'].min()

        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['cdq_power_target'],
            name='Target pushing',
            mode='lines+markers',
            text=df1['cdq_power_target'],
            # textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='red',
                width=2
            )
            ),
            # fill='tozeroy',
            line={'color':'red','shape': 'spline', 'smoothing': 1}
            ),row=2,col=1
            )


        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['CDQ POWER GEN'],
            name='CDQ POWER GEN',
            mode='lines+markers+text',
            text=df1['CDQ POWER GEN'],
            textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            # fill='tozeroy',
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            # fill='tozeroy',
            # line={'shape': 'spline', 'smoothing': 1}
            ),row=2,col=1
            )
        df2=df_1
        df2.index=df2.Month
        #grouping by month
        df2 = df2.groupby(pd.Grouper(freq="M")).mean().round(2)
        df2=df2.tail(12)
        df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]

        max_monthly = df2['CDQ POWER GEN'].max()
        min_monthly = df2['CDQ POWER GEN'].min()

        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['CDQ POWER GEN'],
            name = 'Monthly Mean Power Gen',
            text=df2['CDQ POWER GEN'],
            textposition='outside',
            # mode='lines',
            ),row=1,col=2
            )
        df3=df_1
        df3.index=range(df_1.shape[0])
        #Retriving year from dates
        df3.Month=df3.Month.apply(lambda x: x.year)
        #grouping by year
        df3=df3.groupby('Month').mean().round(2)
        a=df3.index.values.tolist()
        index=["FY-{}".format(str(x)[-2:]) for x in a]
        df3.index=index
        #Making subplots
        fig.add_trace(go.Bar(
            x=df3.index.astype(str),
            y=df3['CDQ POWER GEN'],
            text=df3['CDQ POWER GEN'],
            name = 'Annual Mean Power Gen',
            textposition='outside',
            # mode='lines',
            ),row=1,col=1
            )
        # fig.update_yaxes(row=2, col=1, showgrid=False)
        # fig.update_yaxes(row=1, col=2, visible=False, showgrid=False)
        # fig.update_yaxes(row=1, col=1, visible=False, showgrid=False)

        fig.update_yaxes(row=2, col=1, range=[min_value - 50,max_value + 100], showgrid=False)
        fig.update_yaxes(row=1, col=2,range=[min_monthly - 10,max_monthly +10],visible=False, showgrid=False)
        fig.update_yaxes(row=1, col=1,range=[min_monthly - 10,max_monthly +10],visible=False, showgrid=False)

    # fig.update_layout(yaxis_range=[8700,9500],legend=dict(yanchor='top', y=0.99,  xanchor='left', x=0.01) )

    fig.update_layout(
                    plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                    margin={'t': 0,'l':0,'r':0,'b':0},
                    xaxis=dict(linecolor='#000',showgrid=False),
                    yaxis=dict(linecolor='#000',showgrid=False),
                    font=dict(size=15)
                )
    fig['layout'].update(
            annotations=[
            dict(
                xref='x3 domain',
                yref='y3 domain',
                x=0.95,y=0.87,
                # text='dict Text',
                showarrow=True,
                # align="center",
                arrowhead=2,
                arrowsize=1,
                arrowwidth=5,
                ay=-30,
                ax=0,
                arrowcolor="red",
                font=dict(
                size=15,
                color="#383838"
            )
            ),
            dict(
                xref='x3 domain',
                yref='y3 domain',
                x=0.91,y=0.99,
                # text='dict Text',
                showarrow=True,
                # align="center",
                arrowhead=2,
                arrowsize=1,
                arrowwidth=5,
                ay=30,
                ax=0,
                arrowcolor="green",
                font=dict(
                size=15,
                color="#383838"
            )
            ),

        ])

    fig.update_layout(hovermode="x unified")
    fig.update_layout( showlegend=False)
    fig.update_xaxes(row=1, col=1,linecolor='#000', showgrid=False,tickangle=-45)
    fig.update_xaxes(row=1, col=2,linecolor='#000', showgrid=False,tickangle=-45)
    fig.update_xaxes(row=2, col=1,linecolor='#000', showgrid=False)
    fig.update_yaxes(row=2, col=1,linecolor='#000',showgrid=False)
    fig.update_yaxes(row=1, col=1,linecolor='#000',visible=True,showgrid=False)
    fig.update_yaxes(row=1, col=2,linecolor='#000',visible=True, showgrid=False)


    return dcc.Graph( id='production',figure=fig,style=dict(width='auto', height='auto'),
    config={"displayModeBar": False, "showTips": False}
    )

@app.callback(Output('delay_div','children'),
              Input('production','clickData'))
def delay_ouput(n):
        if n == None:
                date= dt.today().replace(hour=0, minute=0, second=0, microsecond=0) -timedelta(days=1)
        else:
                date=dt.strptime(n['points'][0]['x'], '%Y-%m-%d')

        df_1=pd.read_csv('./datasets/CSV/TE Data/DM Data.csv',parse_dates=['Month'])
        df_1.rename(columns={'CO 3.2':'breakdown3','CO 4.2':'breakdown4','CO 5.2':'breakdown5','CO 3.3':'shutdown3','CO 4.3':'shutdown4','CO 5.3':'shutdown5'}, inplace=True)
        df_delay=df_1.loc[df_1['Month']==date, ['Month', 'breakdown3', 'breakdown4','breakdown5', 'shutdown3', 'shutdown4','shutdown5']].reset_index(drop=True)
        df_delay['Month']=df_delay['Month'].apply(lambda x: dt.strftime(x, '%d-%b-%Y'))
        df_delay.rename(columns={'Month':'Date'}, inplace=True)
        df_delay['breakdown3']=df_delay['breakdown3'].apply(lambda x: 'No Delay' if x in ['0', 0] else x)
        df_delay['breakdown4']=df_delay['breakdown4'].apply(lambda x: 'No Delay' if x in ['0', 0] else x)
        df_delay['breakdown5']=df_delay['breakdown5'].apply(lambda x: 'No Delay' if x in ['0', 0] else x)
        df_delay['shutdown3']=df_delay['shutdown3'].apply(lambda x: 'No Delay' if x in ['0', 0] else x)
        df_delay['shutdown4']=df_delay['shutdown4'].apply(lambda x: 'No Delay' if x in ['0', 0] else x)
        df_delay['shutdown5']=df_delay['shutdown5'].apply(lambda x: 'No Delay' if x in ['0', 0] else x)

        delay_table=[dash_table.DataTable(
        id='delay_dataframe',
        columns=[
        {"name": ["", "Date"], "id": "Date"},
        {"name": ["Breakdown", "Coke Oven 3"], "id": "breakdown3"},
        {"name": ["Breakdown", "Coke Oven 4"], "id": "breakdown4"},
        {"name": ["Breakdown", "Coke Oven 5"], "id": "breakdown5"},
        {"name": ["Shutdown", "Coke Oven 3"], "id": "shutdown3"},
        {"name": ["Shutdown", "Coke Oven 4"], "id": "shutdown4"},
        {"name": ["Shutdown", "Coke Oven 5"], "id": "shutdown5"},
        ],
        merge_duplicate_headers=True,
        data=df_delay.to_dict('records'),
        style_data={
            'whiteSpace': 'normal',
            'height': 'auto',
        },
        style_cell={'textAlign': 'center', 'width': '150px','backgroundColor': 'white','color': 'black',
        'border':'1px solid black','fontSize':20, 'font-family':'sans-serif'
        },
        style_cell_conditional=[
            {'if': {'column_id': 'Date'},
             'width': '7%', 'textAlign': 'center',},
        ]
        )]
        return delay_table

#coal_blend_3
@app.callback(Output('coal_blend_3','children'),
              Input('blend_details3','value'),
              Input('production','clickData'))
def coalblend_pie3(tab, n):

    if n == None:
            date= dt.today().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
    else:
            date=dt.strptime(n['points'][0]['x'], '%Y-%m-%d')

    df=pd.read_csv('./datasets/CSV/TE Data/DM Data_Blend.csv')

    df_blend=df[['Month', 'Blend', 'Blend.1', 'Blend.2']]
    df_blend.rename(columns={'Month':'date', 'Blend':'co3', 'Blend.1':'co4', 'Blend.2':'co5'}, inplace=True)

    df_blend.dropna(inplace=True)
    df_blend['date']=df_blend['date'].apply(lambda x: dt.strptime(x, '%Y-%m-%d'))
    #filtering by date
    df_blend=df_blend.loc[df_blend['date']==date, :].reset_index(drop=True)
    if not(df_blend.empty):
        pattern = r'([a-zA-Z]+\s*[a-zA-Z]*\s*[a-zA-Z]*\s*[a-zA-Z]*)\-*\s*(\d+\.*\d*)'

        a = df_blend.co3.str.extractall(pattern).reset_index()
        a['label'] = a[0] + '-' + a[1] +'%'

        # blend_value=[]
        # for i in range(len(df_blend.co3[0].split(','))):
        #     blend_percentage=df_blend.co3[0].split(',')[i].split('-')
        #     if len(blend_percentage)==2:
        #         blend_percentage=df_blend.co3[0].split(',')[i].split('-')[-1][:-1]
        #     elif len(blend_percentage)==3:
        #         blend_percentage=df_blend.co3[0].split(',')[i].split('-')[1][:-1]
        #     try:
        #         blend_value.append(int(blend_percentage))
        #     except:
        #         pass
        # blend_label=df_blend.co3[0].split(',')
    else:
        blend_value=None
        blend_label=None

    # labels=['Gooneyella-18%','Tech Standard-16%','Contura-12%','Lake Vermont-10%','Kestral-20%','Tech Venture-8%','Maules Creek-10%','PCI-6%']
    # values=[18,16,12,10,20,8,10,6]
    data=go.Pie(labels=a['label'],values=a[1],hole=0.5)
    fig6=go.Figure(data=data,
                   layout=go.Layout(plot_bgcolor='#fff',
                                   paper_bgcolor='#fff',
                                   font_color='black',
                                   margin={'t':0.3,'l':0,'r':0,'b':0})
                                   )

    df_1=pd.read_csv('./datasets/CSV/TE Data/DM Data.csv',parse_dates=['Month'])
    df_1=df_1.loc[df_1['Month']==date, ['Month','CO 3.1','Fluidity.1', 'Ash.1','VM.1', 'Sulphur.1', 'CSN.1', '-3.15.1', '-0.5.1']].reset_index(drop=True)

    if tab == 1:

        return [dcc.Loading(children=[dcc.Graph( id='coal_blend_pie_3',figure=fig6,style=dict(width='auto',height='170px'),
        config={"displayModeBar": False, "showTips": False}
        )],
        type='cube',color='red',fullscreen=False),
        # html.H5(children='Coal/Coke: 1.0 ',
        # style={
        # 'display': 'inline',
        # 'color':'#FF3F00',
        #
        # },
        # className='cards-md',
        # ),
        # html.H5(children='Blend Cost: {} (INR)'.format(df_1.loc[0, 'CO 3.1'].round().astype(int)),
        # style={
        # 'display': 'inline',
        # 'color':'#FF3F00',
        # 'margin-left':'0'
        # },
        # className='cards-md',
        # )
        ]
    else:
        Fluidity = df_1['Fluidity.1'].round(2)
        VM = df_1['VM.1']
        Sulphur = df_1['Sulphur.1']
        CSN = df_1['CSN.1']
        minus_35 = df_1['-3.15.1']
        minus_5 = df_1['-0.5.1']
        df=pd.DataFrame({'Properties':['Fluidity','VM','Sulphur','CSN','-0.35mm','-0.5mm'],
                        'Value':[Fluidity, VM, Sulphur, CSN, minus_35, minus_5]})
        return [dash_table.DataTable(
            id='coal_details_3',
            columns=[{'name':c,'id':c} for c in df.columns],
            data=df.to_dict('records'),
            style_cell={
            # 'backgroundColor': '#261C2C',
            # 'color': 'white',
            # 'border':'1px solid #ec0c85',
            'textAlign': 'center', 'minWidth': '10px', 'width': '50pxpx', 'maxWidth': '100px',
            },
            style_header = {'display': 'none'}
        )]
#coal_blend_4

@app.callback(Output('coal_blend_4','children'),
              Input('blend_details4','value'),
              Input('production','clickData'))
def coalblend_pie3(tab, n):

    '''-------------------blend------------'''
    if n == None:
            date= dt.today().replace(hour=0, minute=0, second=0, microsecond=0) -timedelta(days=1)
    else:
            date=dt.strptime(n['points'][0]['x'], '%Y-%m-%d')

    df=pd.read_csv('./datasets/CSV/TE Data/DM Data_Blend.csv')
    df_blend=df[['Month', 'Blend', 'Blend.1', 'Blend.2']]
    df_blend.rename(columns={'Month':'date', 'Blend':'co3', 'Blend.1':'co4', 'Blend.2':'co5'}, inplace=True)
    df_blend.dropna(inplace=True)
    df_blend['date']=df_blend['date'].apply(lambda x: dt.strptime(x, '%Y-%m-%d'))
    #filtering by date
    df_blend=df_blend.loc[df_blend['date']==date, :].reset_index(drop=True)
    if not(df_blend.empty):
        pattern = r'([a-zA-Z]+\s*[a-zA-Z]*\s*[a-zA-Z]*\s*[a-zA-Z]*)\-*\s*(\d+\.*\d*)'

        a = df_blend.co3.str.extractall(pattern).reset_index()
        a['label'] = a[0] + '-' + a[1] +'%'

    else:
        blend_value=None
        blend_label=None

    # labels=['Gooneyella-18%','Tech Standard-16%','Contura-12%','Lake Vermont-10%','Kestral-20%','Tech Venture-8%','Maules Creek-10%','PCI-6%']
    # values=[18,16,12,10,20,8,10,6]
    data=go.Pie(labels=a['label'],values=a[1],hole=0.5)
    fig6=go.Figure(data=data,
                   layout=go.Layout(plot_bgcolor='#fff',
                                   paper_bgcolor='#fff',
                                   font_color='black',
                                   margin={'t':0.3,'l':0,'r':0,'b':0})
                                   )
    df_1=pd.read_csv('./datasets/CSV/TE Data/DM Data.csv',parse_dates=['Month'])
    df_1=df_1.loc[df_1['Month']==date, ['Month','CO 4.1','Fluidity.3', 'Ash.3','VM.3', 'Sulphur.3', 'CSN.3', '-3.15.3', '-0.5.3']].reset_index(drop=True)
    if tab == 1:

        return [dcc.Loading(children=[dcc.Graph( id='coal_blend_pie_3',figure=fig6,style=dict(width='auto',height='170px'),
        config={"displayModeBar": False, "showTips": False}
        )],
        type='cube',color='red',fullscreen=False),
        # html.H5(children='Coal/Coke: 1.0 ',
        # style={
        # 'display': 'inline',
        # 'color':'#FF3F00',
        # },
        # className='cards-md',
        # ),
        # html.H5(children='Blend Cost: {} (INR)'.format(df_1.loc[0, 'CO 4.1'].round().astype(int)),
        # style={
        # 'display': 'inline',
        # 'color':'#FF3F00',
        # 'margin-left':'0'
        # },
        # className='cards-md',
        # )
        ]
    else:
        Fluidity = df_1['Fluidity.3'].round(2)
        VM = df_1['VM.3']
        Sulphur = df_1['Sulphur.3']
        CSN = df_1['CSN.3']
        minus_35 = df_1['-3.15.3']
        minus_5 = df_1['-0.5.3']
        df=pd.DataFrame({'Properties':['Fluidity','VM','Sulphur','CSN','-0.35mm','-0.5mm'],
                        'Value':[Fluidity, VM, Sulphur, CSN, minus_35, minus_5]})
        return [dash_table.DataTable(
            id='coal_details_3',
            columns=[{'name':c,'id':c} for c in df.columns],
            data=df.to_dict('records'),
            style_cell={
            # 'backgroundColor': '#261C2C',
            # 'color': 'white',
            # 'border':'1px solid #000',
            'textAlign': 'center', 'minWidth': '10px', 'width': '50pxpx', 'maxWidth': '100px',
            },
            style_header = {'display': 'none'}
        )]
#coal_blend_5
@app.callback(Output('coal_blend_5','children'),
              Input('blend_details5','value'),
              Input('production','clickData'))
def coalblend_pie3(tab, n):

    '''-------------------blend------------'''
    if n == None:
            date= dt.today().replace(hour=0, minute=0, second=0, microsecond=0) -timedelta(days=1)
    else:
            date=dt.strptime(n['points'][0]['x'], '%Y-%m-%d')

    df=pd.read_csv('./datasets/CSV/TE Data/DM Data_Blend.csv')
    df_blend=df[['Month', 'Blend', 'Blend.1', 'Blend.2']]
    df_blend.rename(columns={'Month':'date', 'Blend':'co3', 'Blend.1':'co4', 'Blend.2':'co5'}, inplace=True)
    df_blend.dropna(inplace=True)
    df_blend['date']=df_blend['date'].apply(lambda x: dt.strptime(x, '%Y-%m-%d'))
    #filtering by date
    df_blend=df_blend.loc[df_blend['date']==date, :].reset_index(drop=True)
    if not(df_blend.empty):
        pattern = r'([a-zA-Z]+\s*[a-zA-Z]*\s*[a-zA-Z]*\s*[a-zA-Z]*)\-*\s*(\d+\.*\d*)'

        a = df_blend.co3.str.extractall(pattern).reset_index()
        a['label'] = a[0] + '-' + a[1] +'%'

    else:
        blend_value=None
        blend_label=None

    # labels=['Gooneyella-18%','Tech Standard-16%','Contura-12%','Lake Vermont-10%','Kestral-20%','Tech Venture-8%','Maules Creek-10%','PCI-6%']
    # values=[18,16,12,10,20,8,10,6]
    data=go.Pie(labels=a['label'],values=a[1],hole=0.5)
    fig6=go.Figure(data=data,
                   layout=go.Layout(plot_bgcolor='#fff',
                                   paper_bgcolor='#fff',
                                   font_color='black',
                                   margin={'t':0.3,'l':0,'r':0,'b':0})
                                   )
    df_1=pd.read_csv('./datasets/CSV/TE Data/DM Data.csv',parse_dates=['Month'])
    df_1=df_1.loc[df_1['Month']==date, ['Month','CO 5.1','Fluidity.5', 'Ash.9','VM.5', 'Sulphur.5', 'CSN.5', '-3.15.5', '-0.5.5']].reset_index(drop=True)
    if tab == 1:

        return [dcc.Loading(children=[dcc.Graph( id='coal_blend_pie_3',figure=fig6,style=dict(width='auto',height='170px'),
        config={"displayModeBar": False, "showTips": False}
        )],
        type='cube',color='red',fullscreen=False),
        # html.H5(children='Coal/Coke: 1.0 ',
        # style={
        # 'display': 'inline',
        # 'color':'#FF3F00',
        # },
        # className='cards-md',
        # ),
        # html.H5(children='Blend Cost: {} (INR)'.format(df_1.loc[0, 'CO 4.1'].round().astype(int)),
        # style={
        # 'display': 'inline',
        # 'color':'#FF3F00',
        # 'margin-left':'0'
        # },
        # className='cards-md',
        # )
        ]
    else:
        Fluidity = df_1['Fluidity.5'].round(2)
        VM = df_1['VM.5']
        Sulphur = df_1['Sulphur.5']
        CSN = df_1['CSN.5']
        minus_35 = df_1['-3.15.5']
        minus_5 = df_1['-0.5.5']
        df=pd.DataFrame({'Properties':['Fluidity','VM','Sulphur','CSN','-0.35mm','-0.5mm'],
                        'Value':[Fluidity, VM, Sulphur, CSN, minus_35, minus_5]})
        return [dash_table.DataTable(
            id='coal_details_3',
            columns=[{'name':c,'id':c} for c in df.columns],
            data=df.to_dict('records'),
            style_cell={
            # 'backgroundColor': '#261C2C',
            # 'color': 'white',
            # 'border':'1px solid #000',
            'textAlign': 'center', 'minWidth': '10px', 'width': '50pxpx', 'maxWidth': '100px',
            },
            style_header = {'display': 'none'}
        )]


@app.callback(Output('safety_output','children'),
              Input('safety_input','value'),
              Input('production','clickData'))
def coalblend_pie3(tab, n):

    if n == None:
        date= dt.today().replace(hour=0, minute=0, second=0, microsecond=0) -timedelta(days=1)
    else:
        date=dt.strptime(n['points'][0]['x'], '%Y-%m-%d')

    df_1=pd.read_csv('./datasets/CSV/TE Data/DM Data.csv',parse_dates=['Month'])
    df_1.fillna(0, inplace=True)
    df_1=df_1.loc[df_1['Month']<= date, :]

    df_filter=df_1.loc[df_1['Month'] == date, ['FAC', 'RWC', 'MTC', 'LTI', 'F', 'Total ', 'LTI FR', 'NDW LTI']].reset_index( drop=True)

    if not(df_filter.empty):
        fac=df_filter.loc[0, 'FAC']
        rwc=df_filter.loc[0, 'RWC']
        mtc=df_filter.loc[0, 'MTC']
        lti=df_filter.loc[0, 'LTI']
        f=df_filter.loc[0, 'F']
        total=df_filter.loc[0, 'Total ']
        lti_fr=df_filter.loc[0, 'LTI FR']
        lti_days=df_filter.loc[0, 'NDW LTI']
    else:
        fac=0
        rwc=0
        mtc=0
        lti=0
        f=0
        total=0
        lti_fr=0
        lti_days=0

    df=pd.DataFrame({'Parameter':['FAC/MTC','RWC','LTI','Total Incident','LTI-FR Moving Avg.'],
                    'Value':['{}/{}'.format(fac, mtc), rwc, lti, total, lti_fr]})

    if tab == 1:

        return [html.Div([
           html.H1(children=lti_days,
           className='cards-big-safety',
           style={'display': 'inline'}),
           html.H5(children='Days',
           style={
           'display': 'inline',
           },
           className='cards-small-safety mr-1')
        ]),
       html.H5(children='No. of days without LTI',
       style={
       'display': 'inline',
       'color':'#FF3F00',
       },
       className='cards-small-safety',
       )
        ]
    else:


        return [dash_table.DataTable(
            id='safety_table',
            columns=[{'name':c,'id':c} for c in df.columns],
            data=df.to_dict('records'),
            style_cell={
            # 'backgroundColor': '#261C2C',
            # 'color': 'white',
            # 'border':'1px solid #ec0c85',
            'textAlign': 'center', 'minWidth': '10px', 'width': '50pxpx', 'maxWidth': '100px',
            },
            style_header = {'display': 'none'}
        )]


@app.callback(
    Output('quality_parameter_div', 'children'),
    Input('quality_trends_graph','clickData'),
)
def qulaity_parameter_table(n):

    if n == None:
        date= dt.today().replace(hour=0, minute=0, second=0, microsecond=0) -timedelta(days=1)
    else:
        date=dt.strptime(n['points'][0]['x'], '%Y-%m-%d')

    df_1=pd.read_csv('./datasets/CSV/TE Data/DM Data.csv',parse_dates=['Month'])
    df_1.fillna(0, inplace=True)
    df_1=df_1.loc[df_1['Month']<= date, :]
    df_1.replace(['-',' -','#DIV/0!'],0,inplace=True)
    df1=df_1.loc[df_1['Month'] == date,:].reset_index( drop=True).copy()
    df1 = df1[['Month','MO.1','MPS.1','CSR.1','CRI.1','Ash.5','S.1','M10.1','M40.1','MO.3','MPS.3','CSR.3','CRI.3','Ash.7','S.3','M10.3','M40.3','MO.5','MPS.5','CSR.5','CRI.5','Ash.11','S.5','M10.5','M40.5']]
    df1['MPS.1'] = df1['MPS.1'].apply(lambda x: float(x))
    df1['MPS.3'] = df1['MPS.3'].apply(lambda x: float(x))
    df1['MPS.5'] = df1['MPS.5'].apply(lambda x: float(x))

    df_quality = pd.DataFrame({
        'Area':['Coke Oven 3', 'Coke Oven 4', 'Coke Oven 5'],
        'MO': [df1['MO.1'].values[0], df1['MO.3'].values[0], df1['MO.5'].values[0]],
        'MPS': [df1['MPS.1'].round(2).values[0], df1['MPS.3'].round(2).values[0], df1['MPS.5'].round(2).values[0]],
        'CSR':[df1['CSR.1'].values[0], df1['CSR.3'].values[0], df1['CSR.5'].values[0]],
        'CRI':[df1['CRI.1'].values[0], df1['CRI.3'].values[0],  df1['CRI.5'].values[0]],
        'Sulphur':[df1['S.1'].values[0], df1['S.3'].values[0],  df1['S.5'].values[0]],
        'Ash':[df1['Ash.5'].values[0], df1['Ash.7'].values[0], df1['Ash.11'].values[0]],
        'M10':[df1['M10.1'].values[0], df1['M10.3'].values[0],df1['M10.5'].values[0]],
        'M40':[df1['M40.1'].values[0], df1['M40.3'].values[0], df1['M40.5'].values[0]],
    })
    output_table = [
    html.H1(
        'Quality Parameters : ',
        style={"margin-bottom": "30px", 'color': '#000', 'fontSize': 30, 'display' : 'flex'},
    ),
    dash_table.DataTable(
    id='delay_dataframe',
    columns=[
    {"name": c, "id": c} for c in df_quality.columns
    ],
    merge_duplicate_headers=True,
    data=df_quality.to_dict('records'),
    style_cell={'textAlign': 'center',
    'backgroundColor': 'white','color': 'black',
    'border':'2px solid black','fontSize':20, 'font-family':'sans-serif'
    },
    )]
    time.sleep(1)
    return output_table


@app.callback(
    Output('tab_selection_div', 'children'),
    Input('tab_selection', 'value'),
    Input('production','clickData')
)
def tab_selection(tab, n):

    if n == None:
        date= dt.today().replace(hour=0, minute=0, second=0, microsecond=0) -timedelta(days=1)
    else:
        date=dt.strptime(n['points'][0]['x'], '%Y-%m-%d')

    df_1=pd.read_csv('./datasets/CSV/TE Data/DM Data.csv',parse_dates=['Month'])
    df_1.fillna(0, inplace=True)
    df_1=df_1.loc[df_1['Month']<= date, :]
    df_1.replace(['-',' -','#DIV/0!'],0,inplace=True)

    if tab == '2':

        df_1['3 CSR'] = df_1['3 CSR'].apply(lambda x: float(x))
        df_1['4 CSR'] = df_1['4 CSR'].apply(lambda x: float(x))
        df_1['5 CSR'] = df_1['5 CSR'].apply(lambda x: float(x))
        #daily trend
        df1=df_1.loc[df_1['Month'].between(date-timedelta(days=10), date), ['Month', '3 CSR', '4 CSR', '5 CSR','CSR', 'CRI', 'CSR.2', 'CRI.2', 'CSR.4', 'CRI.4' ]].reset_index( drop=True).copy()

        #monthly
        df2=df_1.copy()
        df2=df2[['Month', '3 CSR', '4 CSR', '5 CSR']].copy()

        df2.index=df2.Month
        df2 = df2.groupby(pd.Grouper(freq="M")).mean()
        df2=df2.tail(12)
        df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]


        fig = make_subplots(rows=2, cols=3,
                    vertical_spacing=0.2,
                    horizontal_spacing=0.1,
                    column_widths=[0.5, 0.5, 0.5],
                    row_heights=[0.4,0.6],
                    # subplot_titles=('Coke Oven 3', 'Coke Oven 4')
                    # specs=[[{}, {}],
                   # [{"colspan": 2}, None]],
                )
        df1['CSR']=df1['CSR'].apply(lambda x: float(x))
        df1['CSR.2']=df1['CSR.2'].apply(lambda x: float(x))
        df1['CSR.4']=df1['CSR.4'].apply(lambda x: float(x))

        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['CSR'],
        name='Target',
        mode='lines+markers',
        text=df1['CSR'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=1
        )

        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['CSR.2'],
        name='Target',
        mode='lines+markers',
        text=df1['CSR.2'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=2
        )
#coke5
        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['CSR.4'],
        name='Target',
        mode='lines+markers',
        text=df1['CSR.4'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=3
        )

        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['3 CSR'].round(2),
            name='Actual',
            # fill='tozeroy',
            mode='lines+markers+text',
            text=df1['3 CSR'].round(2),
            textposition='top center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=1
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['3 CSR'].round(2),
            text=df2['3 CSR'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=1
            )

        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['4 CSR'].round(2),
            name='Actual',
            # fill='tozeroy',
            mode='lines+markers+text',
            text=df1['4 CSR'].round(2),
            textposition='top center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=2
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['4 CSR'].round(2),
            text=df2['4 CSR'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=2
            )
        #coke5
        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['5 CSR'].round(2),
            name='Actual',
            # fill='tozeroy',
            mode='lines+markers+text',
            text=df1['5 CSR'].round(2),
            textposition='top center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=3
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['5 CSR'].round(2),
            text=df2['5 CSR'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=3
            )

        max_value3 = df1['3 CSR'].round(2).max()
        min_value3 = df1['3 CSR'].round(2).min()
        max_monthly_value3 = df2['3 CSR'].round(2).max()
        min_monthly_value3 = df2['3 CSR'].round(2).min()
        max_value4 = df1['4 CSR'].round(2).max()
        min_value4 = df1['4 CSR'].round(2).min()
        max_monthly_value4 = df2['4 CSR'].round(2).max()
        min_monthly_value4 = df2['4 CSR'].round(2).min()
        #coke5
        max_value5 = df1['5 CSR'].round(2).max()
        min_value5 = df1['5 CSR'].round(2).min()
        max_monthly_value5 = df2['5 CSR'].round(2).max()
        min_monthly_value5 = df2['5 CSR'].round(2).min()

        fig.update_yaxes(row=2, col=1, linecolor='#000', range = [0, max_value3+ 30],  showgrid=False)
        fig.update_yaxes(row=1, col=1, visible=False, linecolor='#000', range = [min_monthly_value3- 10, min_monthly_value3+ 10],  showgrid=False)
        fig.update_yaxes(row=2, col=2, linecolor='#000', range = [0, max_value4+ 30], showgrid=False)
        fig.update_yaxes(row=1, col=2, visible=False, linecolor='#000', range = [min_monthly_value4- 10, max_monthly_value4+ 10],  showgrid=False)
        fig.update_yaxes(row=2, col=3, linecolor='#000', range = [0, max_value5+ 30], showgrid=False)
        fig.update_yaxes(row=1, col=3, visible=False, linecolor='#000', range = [min_monthly_value5- 10, max_monthly_value5+ 10],  showgrid=False)
        fig.update_layout(
                        plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                        margin={'t': 20,'l':0,'r':0,'b':0},
                        font=dict(size=15),
                        showlegend=False,
                        hovermode="x unified"
                    )
        fig.update_xaxes(row=1, col=1, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=1, linecolor='#000', showgrid=False)
        fig.update_xaxes(row=1, col=2, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=2, linecolor='#000', showgrid=False)
        fig.update_xaxes(row=1, col=3, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=3, linecolor='#000', showgrid=False)
        
        fig['layout'].update(
                annotations=[
                dict(
                    xref='x3 domain',
                    yref='y3 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x3 domain',
                    yref='y3 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x4 domain',
                    yref='y4 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x4 domain',
                    yref='y4 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x5 domain',
                    yref='y5 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x5 domain',
                    yref='y5 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),

            ])




    elif tab == '1':

        df_1['3 Quality Index'] = df_1['3 Quality Index'].apply(lambda x: float(x))
        df_1['4 Quality Index'] = df_1['4 Quality Index'].apply(lambda x: float(x))
        df_1['5 Quality Index'] = df_1['5 Quality Index'].apply(lambda x: float(x))
        #daily trend
        df1=df_1.loc[df_1['Month'].between(date-timedelta(days=15), date), ['Month', '3 Quality Index', '4 Quality Index', '5 Quality Index','3 Quality Index.1', '4 Quality Index.1' ,'5 Quality Index.1']].reset_index( drop=True).copy()
        #monthly
        df2=df_1.copy()
        df2=df2[['Month', '3 Quality Index', '4 Quality Index', '5 Quality Index']].copy()

        df2.index=df2.Month
        df2 = df2.groupby(pd.Grouper(freq="M")).mean()
        df2=df2.tail(12)
        df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]


        fig = make_subplots(rows=2, cols=3,
                    vertical_spacing=0.2,
                    horizontal_spacing=0.1,
                    column_widths=[0.5, 0.5, 0.5],
                    row_heights=[0.4,0.6],
                    # subplot_titles=('Coke Oven 3', 'Coke Oven 4')
                    # specs=[[{}, {}],
                   # [{"colspan": 2}, None]],
                )

        df1['3 Quality Index.1']=df1['3 Quality Index.1'].apply(lambda x: float(x))
        df1['4 Quality Index.1']=df1['4 Quality Index.1'].apply(lambda x: float(x))
        df1['5 Quality Index.1']=df1['5 Quality Index.1'].apply(lambda x: float(x))

        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['3 Quality Index.1'],
        name='Target',
        mode='lines+markers',
        text=df1['3 Quality Index.1'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=1
        )

        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['4 Quality Index.1'],
        name='Target',
        mode='lines+markers',
        text=df1['4 Quality Index.1'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=2
        )
        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['5 Quality Index.1'],
        name='Target',
        mode='lines+markers',
        text=df1['5 Quality Index.1'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=3
        )

        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['3 Quality Index'].round(2),
            # fill='tozeroy',
            name='Actual',
            mode='lines+markers+text',
            text=df1['3 Quality Index'].round(2),
            textposition='top center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=1
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['3 Quality Index'].round(2),
            text=df2['3 Quality Index'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=1
            )

        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['4 Quality Index'].round(2),
            # fill='tozeroy',
            name='Actual',
            mode='lines+markers+text',
            text=df1['4 Quality Index'].round(2),
            textposition='top center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=2
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['4 Quality Index'].round(2),
            text=df2['4 Quality Index'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=2
            )
        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['5 Quality Index'].round(2),
            # fill='tozeroy',
            name='Actual',
            mode='lines+markers+text',
            text=df1['5 Quality Index'].round(2),
            textposition='top center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=3
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['5 Quality Index'].round(2),
            text=df2['5 Quality Index'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=3
            )

        fig['layout'].update(
                annotations=[
                dict(
                    xref='x3 domain',
                    yref='y3 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x3 domain',
                    yref='y3 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x4 domain',
                    yref='y4 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x4 domain',
                    yref='y4 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                #coke5
                dict(
                    xref='x5 domain',
                    yref='y5 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x5 domain',
                    yref='y5 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),

            ])
        fig.update_yaxes(row=2, col=1, linecolor='#000', range=[0,1.5],  showgrid=False)
        fig.update_yaxes(row=1, col=1, visible=False, linecolor='#000', range=[0,1.5],  showgrid=False)
        fig.update_yaxes(row=2, col=2, linecolor='#000', range=[0,1.5],  showgrid=False)
        fig.update_yaxes(row=1, col=2, visible=False, linecolor='#000', range=[0,1.5],  showgrid=False)
        fig.update_yaxes(row=2, col=3, linecolor='#000', range=[0,1.5],  showgrid=False)
        fig.update_yaxes(row=1, col=3, visible=False, linecolor='#000', range=[0,1.5],  showgrid=False)
        fig.update_layout(
                        plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                        margin={'t': 20,'l':0,'r':0,'b':0},
                        font=dict(size=15),
                        showlegend=False,
                        hovermode="x unified"
                    )
        fig.update_xaxes(row=1, col=1, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=1, linecolor='#000', showgrid=False)
        fig.update_xaxes(row=1, col=2, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=2, linecolor='#000', showgrid=False)
        fig.update_xaxes(row=1, col=3, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=3, linecolor='#000', showgrid=False)



    elif tab == '3':

                df_1['3 FINES'] = df_1['3 FINES'].apply(lambda x: float(x))
                df_1['4 FINES'] = df_1['4 FINES'].apply(lambda x: float(x))
                df_1['5 FINES'] = df_1['5 FINES'].apply(lambda x: float(x))
                #daily trend
                df1=df_1.loc[df_1['Month'].between(date-timedelta(days=15), date), ['Month', '3 FINES', '4 FINES', '5 FINES','3 FINES.1', '4 FINES.1', '5 FINES.1']].reset_index( drop=True).copy()
                #monthly
                df2=df_1.copy()
                df2=df2[['Month', '3 FINES', '4 FINES', '5 FINES']].copy()

                df2.index=df2.Month
                df2 = df2.groupby(pd.Grouper(freq="M")).mean()
                df2=df2.tail(12)
                df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]


                fig = make_subplots(rows=2, cols=3,
                            vertical_spacing=0.2,
                            horizontal_spacing=0.1,
                            column_widths=[0.5, 0.5, 0.5],
                            row_heights=[0.4,0.6],
                            # subplot_titles=('Coke Oven 3', 'Coke Oven 4')
                            # specs=[[{}, {}],
                           # [{"colspan": 2}, None]],
                        )
                df1['3 FINES.1']=df1['3 FINES.1'].apply(lambda x: float(x))
                df1['4 FINES.1']=df1['4 FINES.1'].apply(lambda x: float(x))
                df1['5 FINES.1']=df1['5 FINES.1'].apply(lambda x: float(x))

                fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['3 FINES.1'],
                name='Target',
                mode='lines+markers',
                text=df1['3 FINES.1'],
                # textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                color='red',
                width=2
                )
                ),
                line={'color':'red','shape': 'spline', 'smoothing': 1}
                ),row=2,col=1
                )

                fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['4 FINES.1'],
                name='Target',
                mode='lines+markers',
                text=df1['4 FINES.1'],
                # textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                color='red',
                width=2
                )
                ),
                line={'color':'red','shape': 'spline', 'smoothing': 1}
                ),row=2,col=2
                )

                fig.add_trace(go.Scatter(
                x=df1.Month.astype(str),
                y=df1['5 FINES.1'],
                name='Target',
                mode='lines+markers',
                text=df1['5 FINES.1'],
                # textposition='bottom center',
                marker=dict(color='white',
                line=dict(
                color='red',
                width=2
                )
                ),
                line={'color':'red','shape': 'spline', 'smoothing': 1}
                ),row=2,col=3
                )

                fig.add_trace(go.Scatter(
                    x=df1.Month.astype(str),
                    y=df1['3 FINES'].round(2),
                    # fill='tozeroy',
                    name='Actual',
                    mode='lines+markers+text',
                    text=df1['3 FINES'].round(2),
                    textposition='bottom center',
                    marker=dict(color='white',
                    line=dict(
                        color='#0F52BA',
                        width=2
                    )
                    ),
                    line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
                    ),row=2,col=1
                    )
                fig.add_trace(go.Bar(
                    x=df2.index.astype(str),
                    y=df2['3 FINES'].round(2),
                    text=df2['3 FINES'].round(2),
                    textposition='outside',
                    marker_color='#C63637'
                    ),row=1,col=1
                    )

                fig.add_trace(go.Scatter(
                    x=df1.Month.astype(str),
                    y=df1['4 FINES'].round(2),
                    # fill='tozeroy',
                    mode='lines+markers+text',
                    text=df1['4 FINES'].round(2),
                    textposition='bottom center',
                    marker=dict(color='white',
                    line=dict(
                        color='#0F52BA',
                        width=2
                    )
                    ),
                    line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
                    ),row=2,col=2
                    )
                fig.add_trace(go.Bar(
                    x=df2.index.astype(str),
                    y=df2['4 FINES'].round(2),
                    text=df2['4 FINES'].round(2),
                    textposition='outside',
                    marker_color='#C63637'
                    ),row=1,col=2
                    )
                
                fig.add_trace(go.Scatter(
                    x=df1.Month.astype(str),
                    y=df1['5 FINES'].round(2),
                    # fill='tozeroy',
                    name='Actual',
                    mode='lines+markers+text',
                    text=df1['5 FINES'].round(2),
                    textposition='bottom center',
                    marker=dict(color='white',
                    line=dict(
                        color='#0F52BA',
                        width=2
                    )
                    ),
                    line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
                    ),row=2,col=3
                    )
                fig.add_trace(go.Bar(
                    x=df2.index.astype(str),
                    y=df2['5 FINES'].round(2),
                    text=df2['5 FINES'].round(2),
                    textposition='outside',
                    marker_color='#C63637'
                    ),row=1,col=3
                    )

                max_value3 = df1['3 FINES'].round(2).max()
                min_value3 = df1['3 FINES'].round(2).min()
                max_monthly_value3 = df2['3 FINES'].round(2).max()
                min_monthly_value3 = df2['3 FINES'].round(2).min()
                max_value4 = df1['4 FINES'].round(2).max()
                min_value4 = df1['4 FINES'].round(2).min()
                max_monthly_value4 = df2['4 FINES'].round(2).max()
                min_monthly_value4 = df2['4 FINES'].round(2).min()
                #coke5
                max_value5 = df1['5 FINES'].round(2).max()
                min_value5 = df1['5 FINES'].round(2).min()
                max_monthly_value5 = df2['5 FINES'].round(2).max()
                min_monthly_value5 = df2['5 FINES'].round(2).min()

                fig.update_yaxes(row=2, col=1, linecolor='#000', range=[min_value3 - 1.5, max_value3 + 2],  showgrid=False)
                fig.update_yaxes(row=1, col=1, visible=False, linecolor='#000', range=[max_monthly_value3 - 1.5, max_monthly_value3 + 1.5],  showgrid=False)
                fig.update_yaxes(row=2, col=2, linecolor='#000', range=[min_value4 - 3, max_value4 + 3],  showgrid=False)
                fig.update_yaxes(row=1, col=2, visible=False, linecolor='#000', range=[min_monthly_value4 - 3, max_monthly_value4 + 3],  showgrid=False)
                fig.update_yaxes(row=2, col=3, linecolor='#000', range=[min_value5 - 4.5, max_value5 + 4],  showgrid=False)
                fig.update_yaxes(row=1, col=3, visible=False, linecolor='#000', range=[min_monthly_value5 - 4.5, max_monthly_value5 + 4.5],  showgrid=False)
                fig.update_layout(
                                plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                                margin={'t': 20,'l':0,'r':0,'b':0},
                                font=dict(size=15),
                                showlegend=False,
                                hovermode="x unified"
                            )
                fig.update_xaxes(row=1, col=1, linecolor='#000', showgrid=False,tickangle=-45)
                fig.update_xaxes(row=2, col=1, linecolor='#000', showgrid=False)
                fig.update_xaxes(row=1, col=2, linecolor='#000', showgrid=False,tickangle=-45)
                fig.update_xaxes(row=2, col=2, linecolor='#000', showgrid=False)
                fig.update_xaxes(row=1, col=3, linecolor='#000', showgrid=False,tickangle=-45)
                fig.update_xaxes(row=2, col=3, linecolor='#000', showgrid=False)

                fig['layout'].update(
                        annotations=[
                        dict(
                            xref='x3 domain',
                            yref='y3 domain',
                            x=0.95,y=0.87,
                            # text='dict Text',
                            showarrow=True,
                            # align="center",
                            arrowhead=2,
                            arrowsize=1,
                            arrowwidth=5,
                            ay=-30,
                            ax=0,
                            arrowcolor="red",
                            font=dict(
                            size=15,
                            color="#383838"
                        )
                        ),
                        dict(
                            xref='x3 domain',
                            yref='y3 domain',
                            x=0.91,y=0.99,
                            # text='dict Text',
                            showarrow=True,
                            # align="center",
                            arrowhead=2,
                            arrowsize=1,
                            arrowwidth=5,
                            ay=30,
                            ax=0,
                            arrowcolor="green",
                            font=dict(
                            size=15,
                            color="#383838"
                        )
                        ),
                        dict(
                            xref='x4 domain',
                            yref='y4 domain',
                            x=0.95,y=0.87,
                            # text='dict Text',
                            showarrow=True,
                            # align="center",
                            arrowhead=2,
                            arrowsize=1,
                            arrowwidth=5,
                            ay=-30,
                            ax=0,
                            arrowcolor="red",
                            font=dict(
                            size=15,
                            color="#383838"
                        )
                        ),
                        dict(
                            xref='x4 domain',
                            yref='y4 domain',
                            x=0.91,y=0.99,
                            # text='dict Text',
                            showarrow=True,
                            # align="center",
                            arrowhead=2,
                            arrowsize=1,
                            arrowwidth=5,
                            ay=30,
                            ax=0,
                            arrowcolor="green",
                            font=dict(
                            size=15,
                            color="#383838"
                        )
                        ),
                         dict(
                            xref='x5 domain',
                            yref='y5 domain',
                            x=0.95,y=0.87,
                            # text='dict Text',
                            showarrow=True,
                            # align="center",
                            arrowhead=2,
                            arrowsize=1,
                            arrowwidth=5,
                            ay=-30,
                            ax=0,
                            arrowcolor="red",
                            font=dict(
                            size=15,
                            color="#383838"
                        )
                        ),
                        dict(
                            xref='x5 domain',
                            yref='y5 domain',
                            x=0.91,y=0.99,
                            # text='dict Text',
                            showarrow=True,
                            # align="center",
                            arrowhead=2,
                            arrowsize=1,
                            arrowwidth=5,
                            ay=30,
                            ax=0,
                            arrowcolor="green",
                            font=dict(
                            size=15,
                            color="#383838"
                        )
                        ),

                    ])



    elif tab == '4':

        df_1['MPS.1'] = df_1['MPS.1'].apply(lambda x: float(x))
        df_1['MPS.3'] = df_1['MPS.3'].apply(lambda x: float(x))
        df_1['MPS.5'] = df_1['MPS.5'].apply(lambda x: float(x))

        #daily trend
        df1=df_1.loc[df_1['Month'].between(date-timedelta(days=10), date), ['Month', 'MPS', 'MPS.1', 'MPS.2', 'MPS.3', 'MPS.4', 'MPS.5']].reset_index( drop=True).copy()
        df1[['MPS3_L', 'MPS3_H']] = df1['MPS'].str.split('-', expand = True)
        df1[['MPS4_L', 'MPS4_H']] = df1['MPS.2'].str.split('-', expand = True)
        df1[['MPS5_L', 'MPS5_H']] = df1['MPS.4'].str.split('-', expand = True)
        
        

        df1['MPS3_L'] = df1['MPS3_L'].str.strip()
        df1['MPS3_H'] = df1['MPS3_H'].str.strip()
        df1['MPS4_L'] = df1['MPS4_L'].str.strip()
        df1['MPS4_H'] = df1['MPS4_H'].str.strip()
        df1['MPS5_L'] = df1['MPS5_L'].str.strip()
        df1['MPS5_H'] = df1['MPS5_H'].str.strip()

        df1['MPS3_L'] = df1['MPS3_L'].astype('float')
        df1['MPS3_H'] = df1['MPS3_H'].astype('float')
        df1['MPS4_L'] = df1['MPS4_L'].astype('float')
        df1['MPS4_H'] = df1['MPS4_H'].astype('float')
        df1['MPS5_L'] = df1['MPS5_L'].astype('float')
        df1['MPS5_H'] = df1['MPS5_H'].astype('float')
        #monthly
        df2=df_1.copy()
        df2=df2[['Month', 'MPS.1', 'MPS.3', 'MPS.5']].copy()

        df2.index=df2.Month
        df2 = df2.groupby(pd.Grouper(freq="M")).mean()
        df2=df2.tail(12)
        df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]

        fig = make_subplots(rows=2, cols=3,
                    vertical_spacing=0.2,
                    horizontal_spacing=0.1,
                    column_widths=[0.5, 0.5, 0.5],
                    row_heights=[0.4,0.6],
                    # subplot_titles=('Coke Oven 3', 'Coke Oven 4')
                    # specs=[[{}, {}],
                   # [{"colspan": 2}, None]],
                )
        # df1['MPS.1']=df1['MPS.1'].apply(lambda x: float(x))
        # df1['MPS.2']=df1['MPS.2'].apply(lambda x: float(x))

        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['MPS3_L'],
        name='Lower Limit',
        mode='lines',
        text=df1['MPS3_L'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=1
        )

        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['MPS3_H'],
        name='Upper Limit',
        mode='lines',
        text=df1['MPS3_H'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=1
        )

        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['MPS4_L'],
        name='Lower Limit',
        mode='lines',
        text=df1['MPS4_L'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=2
        )

        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['MPS4_H'],
        name='Upper Limit',
        mode='lines',
        text=df1['MPS4_H'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=2
        )
        #coke5
        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['MPS5_L'],
        name='Lower Limit',
        mode='lines',
        text=df1['MPS5_L'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=3
        )

        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['MPS5_H'],
        name='Upper Limit',
        mode='lines',
        text=df1['MPS5_H'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=3
        )
        #
        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['MPS.1'].round(2),
            name='Actual',
            # fill='tozeroy',
            mode='lines+markers+text',
            text=df1['MPS.1'].round(2),
            textposition='top center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=1
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['MPS.1'].round(2),
            text=df2['MPS.1'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=1
            )

        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['MPS.3'].round(2),
            name='Actual',
            # fill='tozeroy',
            mode='lines+markers+text',
            text=df1['MPS.3'].round(2),
            textposition='top center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=2
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['MPS.3'].round(2),
            text=df2['MPS.3'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=2
            )
        #coke5
        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['MPS.5'].round(2),
            name='Actual',
            # fill='tozeroy',
            mode='lines+markers+text',
            text=df1['MPS.5'].round(2),
            textposition='top center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=3
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['MPS.5'].round(2),
            text=df2['MPS.5'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=3
            )

        max_value3 = df1['MPS.1'].round(2).max()
        min_value3 = df1['MPS.1'].round(2).min()
        max_monthly_value3 = df2['MPS.1'].round(2).max()
        min_monthly_value3 = df2['MPS.1'].round(2).min()
        max_value4 = df1['MPS.3'].round(2).max()
        min_value4 = df1['MPS.3'].round(2).min()
        max_monthly_value4 = df2['MPS.3'].round(2).max()
        min_monthly_value4 = df2['MPS.3'].round(2).min()
        #coke5
        max_value5 = df1['MPS.5'].round(2).max()
        min_value5 = df1['MPS.5'].round(2).min()
        max_monthly_value5 = df2['MPS.5'].round(2).max()
        min_monthly_value5 = df2['MPS.5'].round(2).min()

        fig.update_yaxes(row=2, col=1, linecolor='#000', range = [min_value3 - 10, max_value3+ 10],  showgrid=False)
        fig.update_yaxes(row=1, col=1, visible=False, linecolor='#000', range = [min_monthly_value3- 10, min_monthly_value3+ 10],  showgrid=False)
        fig.update_yaxes(row=2, col=2, linecolor='#000', range = [min_value4 - 10, max_value4+ 10], showgrid=False)
        fig.update_yaxes(row=1, col=2, visible=False, linecolor='#000', range = [min_monthly_value4- 10, max_monthly_value4+ 10],  showgrid=False)
        fig.update_yaxes(row=2, col=3, linecolor='#000', range = [min_value5 - 10, max_value5+ 10], showgrid=False)
        fig.update_yaxes(row=1, col=3, visible=False, linecolor='#000', range = [min_monthly_value5- 10, max_monthly_value5+ 10],  showgrid=False)
        fig.update_layout(
                        plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                        margin={'t': 20,'l':0,'r':0,'b':0},
                        font=dict(size=15),
                        showlegend=False,
                        hovermode="x unified"
                    )
        fig.update_xaxes(row=1, col=1, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=1, linecolor='#000', showgrid=False)
        fig.update_xaxes(row=1, col=2, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=2, linecolor='#000', showgrid=False)
        fig.update_xaxes(row=1, col=3, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=3, linecolor='#000', showgrid=False)

        # fig['layout'].update(
        #         annotations=[
        #         dict(
        #             xref='x3 domain',
        #             yref='y3 domain',
        #             x=0.95,y=0.87,
        #             # text='dict Text',
        #             showarrow=True,
        #             # align="center",
        #             arrowhead=2,
        #             arrowsize=1,
        #             arrowwidth=5,
        #             ay=-30,
        #             ax=0,
        #             arrowcolor="red",
        #             font=dict(
        #             size=15,
        #             color="#383838"
        #         )
        #         ),
        #         dict(
        #             xref='x3 domain',
        #             yref='y3 domain',
        #             x=0.91,y=0.99,
        #             # text='dict Text',
        #             showarrow=True,
        #             # align="center",
        #             arrowhead=2,
        #             arrowsize=1,
        #             arrowwidth=5,
        #             ay=30,
        #             ax=0,
        #             arrowcolor="green",
        #             font=dict(
        #             size=15,
        #             color="#383838"
        #         )
        #         ),
        #         dict(
        #             xref='x4 domain',
        #             yref='y4 domain',
        #             x=0.95,y=0.87,
        #             # text='dict Text',
        #             showarrow=True,
        #             # align="center",
        #             arrowhead=2,
        #             arrowsize=1,
        #             arrowwidth=5,
        #             ay=-30,
        #             ax=0,
        #             arrowcolor="red",
        #             font=dict(
        #             size=15,
        #             color="#383838"
        #         )
        #         ),
        #         dict(
        #             xref='x4 domain',
        #             yref='y4 domain',
        #             x=0.91,y=0.99,
        #             # text='dict Text',
        #             showarrow=True,
        #             # align="center",
        #             arrowhead=2,
        #             arrowsize=1,
        #             arrowwidth=5,
        #             ay=30,
        #             ax=0,
        #             arrowcolor="green",
        #             font=dict(
        #             size=15,
        #             color="#383838"
        #         )
        #         ),
        #
        #     ])

    output_csr=[
        dbc.Row([
            dbc.Col([
                html.H1('Coke Oven 3',style={'margin-top':'3rem', 'color':'black', 'text-align': 'center',
                "font-family": "Cormorant ,sans-serif"}),
            ], width=4),
            dbc.Col([
                html.H1('Coke Oven 4',style={'margin-top':'3rem', 'color':'black', 'text-align': 'center', "font-family": "Cormorant ,sans-serif"}),
            ], width=4),
            dbc.Col([
                html.H1('Coke Oven 5',style={'margin-top':'3rem', 'color':'black', 'text-align': 'center', "font-family": "Cormorant ,sans-serif"}),
            ], width=4)
        ]),
        dbc.Row([
            dbc.Col([
            dcc.Graph( id='quality_trends_graph', figure=fig,style=dict(width='auto',height='auto'),
            config={"displayModeBar": False, "showTips": False}
            )
            ], width=12),
        ])
    ]
    return output_csr




@app.callback(
    Output('tab_selection_cost_div', 'children'),
    Input('tab_selection_cost', 'value'),
    Input('production','clickData')
)
def tab_selection(tab, n):

    if n == None:
        date= dt.today().replace(hour=0, minute=0, second=0, microsecond=0) -timedelta(days=1)
    else:
        date=dt.strptime(n['points'][0]['x'], '%Y-%m-%d')

    df_1=pd.read_csv('./datasets/CSV/TE Data/DM Data.csv',parse_dates=['Month'])
    df_1.fillna(0, inplace=True)
    df_1=df_1.loc[df_1['Month']<= date, :]
    df_1.replace(['-',' -','#DIV/0!'],0,inplace=True)
    df_1.rename(columns={'CO #3.5': 'sp_power3', 'CO #4.5': 'sp_power4', 'CO #5.5': 'sp_power5','CO #3.6': 'sp_steam3',  'CO #4.6': 'sp_steam4', 'CO #5.6': 'sp_steam5',
                         'CO 3': 'sp_gas3',  'CO 4': 'sp_gas4', 'CO 5': 'sp_gas5','CO 3.1':'blend_cost3','CO 4.1':'blend_cost4', 'CO 5.1':'blend_cost5',
                         'CO #3.9': 'sp_power_target3', 'CO #4.9': 'sp_power_target4', 'CO #5.9': 'sp_power_target5',
                         'CO #3.10': 'sp_steam_target3', 'CO #4.10': 'sp_steam_target4', 'CO #5.10': 'sp_steam_target5',
                         'CO #3.11':'sp_gas_target3', 'CO #4.11':'sp_gas_target4',  'CO #5.11':'sp_gas_target5'
                         }, inplace=True)
    if tab == '2':

        df_1['sp_steam3'] = df_1['sp_steam3'].apply(lambda x: float(x))
        df_1['sp_steam4'] = df_1['sp_steam4'].apply(lambda x: float(x))
        df_1['sp_steam5'] = df_1['sp_steam5'].apply(lambda x: float(x))
        #daily trend
        df1=df_1.loc[df_1['Month'].between(date-timedelta(days=10), date), ['Month', 'sp_steam3', 'sp_steam4', 'sp_steam5','sp_steam_target3', 'sp_steam_target4', 'sp_steam_target5']].reset_index( drop=True).copy()
        #monthly
        df2=df_1.copy()
        df2=df2[['Month', 'sp_steam3', 'sp_steam4', 'sp_steam5']].copy()

        df2.index=df2.Month
        df2 = df2.groupby(pd.Grouper(freq="M")).mean()
        df2=df2.tail(12)
        df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]


        fig = make_subplots(rows=2, cols=3,
                    vertical_spacing=0.2,
                    horizontal_spacing=0.1,
                    column_widths=[0.5, 0.5, 0.5],
                    row_heights=[0.4,0.6],
                    # subplot_titles=('Coke Oven 3', 'Coke Oven 4')
                    # specs=[[{}, {}],
                   # [{"colspan": 2}, None]],
                )

        df1['sp_steam_target3']=df1['sp_steam_target3'].apply(lambda x: float(x))
        df1['sp_steam_target4']=df1['sp_steam_target4'].apply(lambda x: float(x))
        df1['sp_steam_target5']=df1['sp_steam_target5'].apply(lambda x: float(x))


        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['sp_steam_target3'],
            name='Target',
            mode='lines+markers',
            text=df1['sp_steam_target3'],
            # textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='red',
                width=2
            )
            ),
            line={'color':'red','shape': 'spline', 'smoothing': 1}
            ),row=2,col=1
            )
        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['sp_steam_target4'],
            name='Target',
            mode='lines+markers',
            text=df1['sp_steam_target4'],
            # textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='red',
                width=2
            )
            ),
            line={'color':'red','shape': 'spline', 'smoothing': 1}
            ),row=2,col=2
            )
        #coke5
        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['sp_steam_target5'],
            name='Target',
            mode='lines+markers',
            text=df1['sp_steam_target5'],
            # textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='red',
                width=2
            )
            ),
            line={'color':'red','shape': 'spline', 'smoothing': 1}
            ),row=2,col=3
            )
        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['sp_steam3'].round(2),
            name='Actual',
            # fill='tozeroy',
            mode='lines+markers+text',
            text=df1['sp_steam3'].round(2),
            textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=1
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['sp_steam3'].round(2),
            text=df2['sp_steam3'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=1
            )

        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['sp_steam4'].round(2),
            name='Actual',
            # fill='tozeroy',
            mode='lines+markers+text',
            text=df1['sp_steam4'].round(2),
            textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=2
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['sp_steam4'].round(2),
            text=df2['sp_steam4'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=2
            )
        
        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['sp_steam5'].round(2),
            name='Actual',
            # fill='tozeroy',
            mode='lines+markers+text',
            text=df1['sp_steam5'].round(2),
            textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=3
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['sp_steam5'].round(2),
            text=df2['sp_steam5'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=3
            )

        fig.update_yaxes(row=2, col=1, linecolor='#000', range=[0, 0.4], showgrid=False)
        fig.update_yaxes(row=1, col=1, visible=False, linecolor='#000', range=[0, 0.4], showgrid=False)
        fig.update_yaxes(row=2, col=2, linecolor='#000', range=[0, 0.4], showgrid=False)
        fig.update_yaxes(row=1, col=2, visible=False, linecolor='#000', range=[0, 0.4], showgrid=False)
        fig.update_yaxes(row=2, col=3, linecolor='#000', range=[0, 0.4], showgrid=False)
        fig.update_yaxes(row=1, col=3, visible=False, linecolor='#000', range=[0, 0.4], showgrid=False)
        fig.update_layout(
                        plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                        margin={'t': 20,'l':0,'r':0,'b':0},
                        font=dict(size=15),
                        showlegend=False,
                        hovermode="x unified"
                    )
        fig.update_xaxes(row=1, col=1, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=1, linecolor='#000', showgrid=False)
        fig.update_xaxes(row=1, col=2, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=2, linecolor='#000', showgrid=False)
        fig.update_xaxes(row=1, col=3, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=3, linecolor='#000', showgrid=False)

        fig['layout'].update(
                annotations=[
                dict(
                    xref='x3 domain',
                    yref='y3 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x3 domain',
                    yref='y3 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x4 domain',
                    yref='y4 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x4 domain',
                    yref='y4 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x5 domain',
                    yref='y5 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x5 domain',
                    yref='y5 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),

            ])


        output_csr=[
            dbc.Row([
                dbc.Col([
                    html.H1('Coke Oven 3',style={'margin-top':'3rem', 'color':'black', 'text-align': 'center',
                    "font-family": "Cormorant ,sans-serif"}),
                ], width=4),
                dbc.Col([
                    html.H1('Coke Oven 4',style={'margin-top':'3rem', 'color':'black', 'text-align': 'center',
                     "font-family": "Cormorant ,sans-serif"}),
                ], width=4),
                dbc.Col([
                    html.H1('Coke Oven 5',style={'margin-top':'3rem', 'color':'black', 'text-align': 'center',
                     "font-family": "Cormorant ,sans-serif"}),
                ], width=4)
            ]),
            dbc.Row([
                dbc.Col([
                dcc.Graph( id='csr_trend_graph3', figure=fig,style=dict(width='auto',height='auto'),
                config={"displayModeBar": False, "showTips": False}
                )
                ], width=12),
            ])
        ]

    elif tab == '1':
        df_1['sp_power3'] = df_1['sp_power3'].apply(lambda x: float(x))
        df_1['sp_power4'] = df_1['sp_power4'].apply(lambda x: float(x))
        df_1['sp_power5'] = df_1['sp_power5'].apply(lambda x: float(x))
        #daily trend
        df1=df_1.loc[df_1['Month'].between(date-timedelta(days=10), date), ['Month', 'sp_power3', 'sp_power4', 'sp_power5','sp_power_target3', 'sp_power_target4', 'sp_power_target5']].reset_index( drop=True).copy()
        #monthly
        df2=df_1.copy()
        df2=df2[['Month', 'sp_power3', 'sp_power4','sp_power5']].copy()


        df2.index=df2.Month
        df2 = df2.groupby(pd.Grouper(freq="M")).mean()
        df2=df2.tail(12)
        df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]

        fig = make_subplots(rows=2, cols=3,
                    vertical_spacing=0.2,
                    horizontal_spacing=0.1,
                    column_widths=[0.5, 0.5, 0.5],
                    row_heights=[0.4,0.6],
                    # subplot_titles=('Coke Oven 3', 'Coke Oven 4')
                    # specs=[[{}, {}],
                   # [{"colspan": 2}, None]],
                )

        df1['sp_power_target3']=df1['sp_power_target3'].apply(lambda x: float(x))
        df1['sp_power_target4']=df1['sp_power_target4'].apply(lambda x: float(x))
        df1['sp_power_target5']=df1['sp_power_target5'].apply(lambda x: float(x))


        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['sp_power_target3'],
        name='Target',
        mode='lines+markers',
        text=df1['sp_power_target3'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=1
        )

        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['sp_power_target4'],
        name='Target',
        mode='lines+markers',
        text=df1['sp_power_target4'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=2
        )
        #coke5
        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['sp_power_target5'],
        name='Target',
        mode='lines+markers',
        text=df1['sp_power_target5'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=3
        )

        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['sp_power3'].round(2),
            name='Actual',
            # fill='tozeroy',
            mode='lines+markers+text',
            text=df1['sp_power3'].round(2),
            textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=1
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['sp_power3'].round(2),
            text=df2['sp_power3'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=1
            )

        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['sp_power4'].round(2),
            name='Actual',
            # fill='tozeroy',
            mode='lines+markers+text',
            text=df1['sp_power4'].round(2),
            textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=2
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['sp_power4'].round(2),
            text=df2['sp_power4'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=2
            )
        
        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['sp_power5'].round(2),
            name='Actual',
            # fill='tozeroy',
            mode='lines+markers+text',
            text=df1['sp_power5'].round(2),
            textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=3
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['sp_power5'].round(2),
            text=df2['sp_power5'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=3
            )

        fig.update_yaxes(row=2, col=1, linecolor='#000', range=[40,80],  showgrid=False)
        fig.update_yaxes(row=1, col=1, visible=False, linecolor='#000', range=[40,80],  showgrid=False)
        fig.update_yaxes(row=2, col=2, linecolor='#000', range=[40,70],  showgrid=False)
        fig.update_yaxes(row=1, col=2, visible=False, linecolor='#000', range=[40,80],  showgrid=False)
        fig.update_yaxes(row=2, col=3, linecolor='#000', range=[40,70],  showgrid=False)
        fig.update_yaxes(row=1, col=3, visible=False, linecolor='#000', range=[40,80],  showgrid=False)
        fig.update_layout(
                        plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                        margin={'t': 20,'l':0,'r':0,'b':0},
                        font=dict(size=15),
                        showlegend=False,
                        hovermode="x unified"
                    )
        fig.update_xaxes(row=1, col=1, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=1, linecolor='#000', showgrid=False)
        fig.update_xaxes(row=1, col=2, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=2, linecolor='#000', showgrid=False)
        fig.update_xaxes(row=1, col=3, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=3, linecolor='#000', showgrid=False)

        fig['layout'].update(
                annotations=[
                dict(
                    xref='x3 domain',
                    yref='y3 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x3 domain',
                    yref='y3 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x4 domain',
                    yref='y4 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x4 domain',
                    yref='y4 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                 dict(
                    xref='x5 domain',
                    yref='y5 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x5 domain',
                    yref='y5 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),

            ])


        output_csr=[
            dbc.Row([
                dbc.Col([
                    html.H1('Coke Oven 3',style={'margin-top':'3rem', 'color':'black', 'text-align': 'center',
                    "font-family": "Cormorant ,sans-serif"}),
                ], width=4),
                dbc.Col([
                    html.H1('Coke Oven 4',style={'margin-top':'3rem', 'color':'black', 'text-align': 'center',
                     "font-family": "Cormorant ,sans-serif"}),
                ], width=4),
                dbc.Col([
                    html.H1('Coke Oven 5',style={'margin-top':'3rem', 'color':'black', 'text-align': 'center',
                     "font-family": "Cormorant ,sans-serif"}),
                ], width=4)
            ]),
            dbc.Row([
                dbc.Col([
                dcc.Graph( id='csr_trend_graph3', figure=fig,style=dict(width='auto',height='auto'),
                config={"displayModeBar": False, "showTips": False}
                )
                ], width=12),
            ])
        ]
    elif tab == '3':

        df_1['sp_gas3'] = df_1['sp_gas3'].apply(lambda x: float(x))
        df_1['sp_gas4'] = df_1['sp_gas4'].apply(lambda x: float(x))
        df_1['sp_gas5'] = df_1['sp_gas5'].apply(lambda x: float(x))
        date_minus2  = date -timedelta(days = 1)

        #daily trend
        df1=df_1.loc[df_1['Month'].between(date_minus2-timedelta(days=10), date_minus2), ['Month', 'sp_gas3', 'sp_gas4', 'sp_gas5','sp_gas_target3', 'sp_gas_target4', 'sp_gas_target5']].reset_index( drop=True).copy()
        #monthly
        df2=df_1.copy()
        df2=df2[['Month', 'sp_gas3', 'sp_gas4', 'sp_gas5']].copy()

        df2.index=df2.Month
        df2 = df2.groupby(pd.Grouper(freq="M")).mean()
        df2=df2.tail(12)
        df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]

        fig = make_subplots(rows=2, cols=3,
                    vertical_spacing=0.2,
                    horizontal_spacing=0.1,
                    column_widths=[0.5, 0.5, 0.5],
                    row_heights=[0.4,0.6],
                    # subplot_titles=('Coke Oven 3', 'Coke Oven 4')
                    # specs=[[{}, {}],
                   # [{"colspan": 2}, None]],
                )

        df1['sp_gas_target3']=df1['sp_gas_target3'].apply(lambda x: float(x))
        df1['sp_gas_target4']=df1['sp_gas_target4'].apply(lambda x: float(x))
        df1['sp_gas_target5']=df1['sp_gas_target5'].apply(lambda x: float(x))


        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['sp_gas_target3'],
        name='Target',
        mode='lines+markers',
        text=df1['sp_gas_target3'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=1
        )

        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['sp_gas_target4'],
        name='Target',
        mode='lines+markers',
        text=df1['sp_gas_target4'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=2
        )
        fig.add_trace(go.Scatter(
        x=df1.Month.astype(str),
        y=df1['sp_gas_target5'],
        name='Target',
        mode='lines+markers',
        text=df1['sp_gas_target5'],
        # textposition='bottom center',
        marker=dict(color='white',
        line=dict(
        color='red',
        width=2
        )
        ),
        line={'color':'red','shape': 'spline', 'smoothing': 1}
        ),row=2,col=3
        )

        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['sp_gas3'].round(2),
            name='Actual',
            # fill='tozeroy',
            mode='lines+markers+text',
            text=df1['sp_gas3'].round(2),
            textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=1
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['sp_gas3'].round(2),
            text=df2['sp_gas3'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=1
            )

        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['sp_gas4'].round(2),
            name='Actual',
            # fill='tozeroy',
            mode='lines+markers+text',
            text=df1['sp_gas4'].round(2),
            textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=2
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['sp_gas4'].round(2),
            text=df2['sp_gas4'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=2
            )
        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['sp_gas5'].round(2),
            name='Actual',
            # fill='tozeroy',
            mode='lines+markers+text',
            text=df1['sp_gas5'].round(2),
            textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=3
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['sp_gas5'].round(2),
            text=df2['sp_gas5'].round(2),
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=3
            )

        fig.update_yaxes(row=2, col=1, linecolor='#000', range=[0, 1.5], showgrid=False)
        fig.update_yaxes(row=1, col=1, visible=False, linecolor='#000', range=[0, 1], showgrid=False)
        fig.update_yaxes(row=2, col=2, linecolor='#000', range=[0, 1.5], showgrid=False)
        fig.update_yaxes(row=1, col=2, visible=False, linecolor='#000', range=[0, 1], showgrid=False)
        fig.update_yaxes(row=2, col=3, linecolor='#000', range=[0, 1.5], showgrid=False)
        fig.update_yaxes(row=1, col=3, visible=False, linecolor='#000', range=[0, 1], showgrid=False)
        fig.update_layout(
                        plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                        margin={'t': 20,'l':0,'r':0,'b':0},
                        font=dict(size=15),
                        showlegend=False,
                        hovermode="x unified"
                    )
        fig.update_xaxes(row=1, col=1, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=1, linecolor='#000', showgrid=False)
        fig.update_xaxes(row=1, col=2, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=2, linecolor='#000', showgrid=False)
        fig.update_xaxes(row=1, col=3, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=3, linecolor='#000', showgrid=False)

        fig['layout'].update(
                annotations=[
                dict(
                    xref='x3 domain',
                    yref='y3 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x3 domain',
                    yref='y3 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x4 domain',
                    yref='y4 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x4 domain',
                    yref='y4 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x5 domain',
                    yref='y5 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x5 domain',
                    yref='y5 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),

            ])


        output_csr=[
            dbc.Row([
                dbc.Col([
                    html.H1('Coke Oven 3',style={'margin-top':'3rem', 'color':'black', 'text-align': 'center',
                    "font-family": "Cormorant ,sans-serif"}),
                ], width=4),
                dbc.Col([
                    html.H1('Coke Oven 4',style={'margin-top':'3rem', 'color':'black', 'text-align': 'center',
                     "font-family": "Cormorant ,sans-serif"}),
                ], width=4),
                dbc.Col([
                    html.H1('Coke Oven 5',style={'margin-top':'3rem', 'color':'black', 'text-align': 'center',
                     "font-family": "Cormorant ,sans-serif"}),
                ], width=4)
            ]),
            dbc.Row([
                dbc.Col([
                dcc.Graph( id='csr_trend_graph3', figure=fig,style=dict(width='auto',height='auto'),
                config={"displayModeBar": False, "showTips": False}
                )
                ], width=12),
            ])
        ]

    if tab == '4':

        df_1['blend_cost3'] = df_1['blend_cost3'].apply(lambda x: int(float(x)))
        df_1['blend_cost4'] = df_1['blend_cost4'].apply(lambda x: int(float(x)))
        df_1['blend_cost5'] = df_1['blend_cost5'].apply(lambda x: int(float(x)))
        #daily trend
        df1=df_1.loc[df_1['Month'].between(date-timedelta(days=15), date), ['Month', 'blend_cost3', 'blend_cost4', 'blend_cost5']].reset_index( drop=True).copy()


        #monthly
        df2=df_1.copy()
        df2=df2[['Month', 'blend_cost3', 'blend_cost4', 'blend_cost5']].copy()
        df2.index=df2.Month
        df2 = df2.groupby(pd.Grouper(freq="M")).mean()
        df2=df2.tail(12)
        df2.index=[x.strftime('%b-%y') for x in df2.index.tolist()]
        df2['blend_cost3'] = df2['blend_cost3'].apply(lambda x: int(x))
        df2['blend_cost4'] = df2['blend_cost4'].apply(lambda x: int(x))
        df2['blend_cost5'] = df2['blend_cost5'].apply(lambda x: int(x))
        df2['blend_cost3_text'] = df2['blend_cost3'].apply(lambda x: '₹ '+str(x))
        df2['blend_cost4_text'] = df2['blend_cost4'].apply(lambda x: '₹ '+str(x))
        df2['blend_cost5_text'] = df2['blend_cost5'].apply(lambda x: '₹ '+str(x))

        fig = make_subplots(rows=2, cols=3,
                    vertical_spacing=0.1,
                    horizontal_spacing=0.1,
                    column_widths=[0.4, 0.4, 0.4],
                    row_heights=[0.4,0.6],
                )

        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['blend_cost3'],
            name='Blend Cost',
            mode='lines+markers',
            text=df1['blend_cost3'],
            textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=1
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['blend_cost3'],
            text=df2['blend_cost3_text'],
            name='Blend Cost',
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=1
            )

        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['blend_cost4'],
            name='Blend Cost',
            # fill='tozeroy',
            mode='lines+markers',
            text=df1['blend_cost4'],
            textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=2
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['blend_cost4'],
            name='Blend Cost',
            text=df2['blend_cost4_text'],
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=2
            )
        fig.add_trace(go.Scatter(
            x=df1.Month.astype(str),
            y=df1['blend_cost5'],
            name='Blend Cost',
            mode='lines+markers',
            text=df1['blend_cost5'],
            textposition='bottom center',
            marker=dict(color='white',
            line=dict(
                color='#0F52BA',
                width=2
            )
            ),
            line={'color':'#0F52BA','shape': 'spline', 'smoothing': 1}
            ),row=2,col=3
            )
        fig.add_trace(go.Bar(
            x=df2.index.astype(str),
            y=df2['blend_cost5'],
            text=df2['blend_cost5_text'],
            name='Blend Cost',
            textposition='outside',
            marker_color='#C63637'
            ),row=1,col=3
            )

        max_value3 = df1['blend_cost3'].max()
        min_value3 = df1['blend_cost3'].min()
        max_value4 = df1['blend_cost4'].max()
        min_value4 = df1['blend_cost4'].min()
        max_value5 = df1['blend_cost5'].max()
        min_value5 = df1['blend_cost5'].min()

        fig.update_yaxes(row=2, col=1, linecolor='#000', range=[min_value3 - 1500, max_value3+10000], showgrid=False)
        fig.update_yaxes(row=1, col=1, visible=False, linecolor='#000', range=[0, max_value3+5000], showgrid=False)
        fig.update_yaxes(row=2, col=2, linecolor='#000', range=[min_value4 - 1500, max_value4+10000], showgrid=False)
        fig.update_yaxes(row=1, col=2, visible=False, linecolor='#000', range=[0, max_value4+5000], showgrid=False)
        fig.update_yaxes(row=2, col=3, linecolor='#000', range=[min_value5 - 1500, max_value5+10000], showgrid=False)
        fig.update_yaxes(row=1, col=3, visible=False, linecolor='#000', range=[0, max_value5+5000], showgrid=False)
        fig.update_layout(
                        plot_bgcolor='#fff',paper_bgcolor='#fff',font_color='black',
                        margin={'t': 20,'l':0,'r':0,'b':0},
                        font=dict(size=15),
                        showlegend=False,
                        hovermode="x unified"
                    )
        fig.update_xaxes(row=1, col=1, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=1, linecolor='#000', showgrid=False)
        fig.update_xaxes(row=1, col=2, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=2, linecolor='#000', showgrid=False)
        fig.update_xaxes(row=1, col=3, linecolor='#000', showgrid=False,tickangle=-45)
        fig.update_xaxes(row=2, col=3, linecolor='#000', showgrid=False)
        fig.update_layout(uniformtext_minsize=5, uniformtext_mode='hide')

        fig['layout'].update(
                annotations=[
                dict(
                    xref='x3 domain',
                    yref='y3 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x3 domain',
                    yref='y3 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x4 domain',
                    yref='y4 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x4 domain',
                    yref='y4 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x5 domain',
                    yref='y5 domain',
                    x=0.95,y=0.87,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=-30,
                    ax=0,
                    arrowcolor="red",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),
                dict(
                    xref='x5 domain',
                    yref='y5 domain',
                    x=0.91,y=0.99,
                    # text='dict Text',
                    showarrow=True,
                    # align="center",
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=5,
                    ay=30,
                    ax=0,
                    arrowcolor="green",
                    font=dict(
                    size=15,
                    color="#383838"
                )
                ),

            ])

        output_csr=[
            dbc.Row([
                dbc.Col([
                    html.H1('Coke Oven 3',style={'margin-top':'3rem', 'color':'black', 'text-align': 'center',
                    "font-family": "Cormorant ,sans-serif"}),
                ], width=4),
                dbc.Col([
                    html.H1('Coke Oven 4',style={'margin-top':'3rem', 'color':'black', 'text-align': 'center', "font-family": "Cormorant ,sans-serif"}),
                ], width=4),
                dbc.Col([
                    html.H1('Coke Oven 5',style={'margin-top':'3rem', 'color':'black', 'text-align': 'center', "font-family": "Cormorant ,sans-serif"}),
                ], width=4)
            ]),
            dbc.Row([
                dbc.Col([
                dcc.Graph( id='csr_trend_graph3', figure=fig,style=dict(width='auto',height='auto'),
                config={"displayModeBar": False, "showTips": False}
                )
                ], width=12),
            ])
        ]

    return output_csr



# #test.py wala
# df_blend=pd.read_excel('./datasets/CSV/TE Data/DM Data.xlsx', sheet_name='DM Data_Blend', skiprows=2)

# df=pd.read_excel('./datasets/CSV/TE Data/DM Data.xlsx', sheet_name='DM Data', skiprows=2)
# def te_Data():
#     try:
#         df=pd.read_excel('./datasets/CSV/TE Data/DM Data.xlsx', sheet_name='DM Data', skiprows=2)
#         df_blend=pd.read_excel('./datasets/CSV/TE Data/DM Data.xlsx', sheet_name='DM Data_Blend', skiprows=2)

#         df.to_csv('./datasets/CSV/TE Data/DM Data.csv')
#         df_blend.to_csv('./datasets/CSV/TE Data/DM Data_Blend.csv')

#     except:
#         pass
def te_Data():
    try:
        df = pd.read_excel(r'//10.10.78.108/Users/process.coke5/process_data/TE Data/DM Data.xlsx', sheet_name='DM Data', skiprows=2)
        df_blend = pd.read_excel(r'//10.10.78.108/Users/process.coke5/process_data/TE Data/DM Data.xlsx', sheet_name='DM Data_Blend', skiprows=2)

        df.to_csv('./datasets/CSV/TE Data/DM Data.csv')
        df_blend.to_csv('./datasets/CSV/TE Data/DM Data_Blend.csv')

    except Exception as e:
        print("Error occurred while updating data:", e)

# Function to run the scheduler loop
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)  # Sleep for 1 second to avoid high CPU usage

# Schedule data update every hour
#schedule.every().hour.do(te_Data)
schedule.every(1).minutes.do(te_Data)       

# Create and start a thread for the scheduler loop
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()





if __name__ == '__main__':
    te_Data()
    app.run_server(debug=False, host='0.0.0.0', port=8055)    
    while True:
        run_scheduler()