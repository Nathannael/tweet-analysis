import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output
import json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.H1(children='Tweet-Analysis'),
        html.Div(children='''
          Gráfico informando o impacto de séries recém-adicionadas à Netflix nas redes Sociais
        '''),
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*1000, # in milliseconds
            n_intervals=0
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])
def update_graph_tweets(n):
  data = json.load(open("data.json"))
  data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

  data =  {'x': list(data.keys()), 'y': list(data.values()), 'type': 'bar', 'name': 'SF'}

  return {'data': [data] }

if __name__ == '__main__':
    app.run_server(debug=True)
