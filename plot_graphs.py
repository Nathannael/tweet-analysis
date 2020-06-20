import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output
import json
from analysis import Analysis

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

streamer = None

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
      html.H1(children='Tweet-Analysis'),

      html.Div(dcc.Input(id='input-on-submit', type='text')),
      html.Button('Submit', id='submit-val', n_clicks=0),
      html.Div(id='container-button-basic',
              children='Enter a value and press submit'),
      html.H3(id='number_tweets',
              children='Enter a value and press submit'),

      dcc.Graph(id='live-graph', animate=True),
      dcc.Interval(
        id='graph-update',
        interval=1*1000, # in milliseconds
        n_intervals=0
      ),
    ]
)

@app.callback(
  dash.dependencies.Output('container-button-basic', 'children'),
  [dash.dependencies.Input('submit-val', 'n_clicks')],
  [dash.dependencies.State('input-on-submit', 'value')]
)
def update_output_div(n_clicks, input_value):
  global streamer

  if streamer is not None:
    Analysis.stop(streamer)

  streamer = Analysis.perform(input_value)
  return 'Iniciado'

@app.callback(
  Output('live-graph', 'figure'),
  [Input('graph-update', 'n_intervals')]
)
def update_graph_tweets(n):
  data = json.load(open("data.json"))
  data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

  data =  {'x': list(data.keys())[:15], 'y': list(data.values())[:15], 'type': 'bar', 'name': 'SF'}

  return {'data': [data] }


@app.callback(
  Output('number_tweets', 'children'),
  [Input('graph-update', 'n_intervals')]
)
def show_num_tweets(n):
  data = json.load(open("number_tweets.json"))
  return f'{data["count"]} tweets analisados'


if __name__ == '__main__':
  app.run_server(debug=True)

