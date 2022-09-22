from dash import Dash,html,dcc
import plotly.express as px
import pandas as pd

app=Dash(__name__)
data=pd.read_csv('./data/ouput.csv')
fig=px.bar(data,x='date',y='sale')
app.layout=html.Div(children=[html.H1(children='Sales V/S Date'),
                              dcc.Graph(id='example-graph',figure=fig)
                              ])

app.run_server()
