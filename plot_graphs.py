import datetime
import json

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output

from analysis import Analysis
from lib.tools import save_to_file
from lib.tools import load_from_file

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

streamer = None

# Init files
save_to_file({ 'count': 0 }, filename="number_tweets.json")
save_to_file({}, filename="most_retweeted.json")
save_to_file({}, filename="sources.json")
save_to_file({}, filename="countries.json")

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
      html.H1(children='Tweet-Analysis'),

      html.Div([
          dcc.Input(id='input-on-submit', type='text'),
          html.Button('Submit', id='submit-val', n_clicks=0),
      ]),
      html.Div(id='container-button-basic', children='Enter a value and press submit'),
      html.H3(id='number_tweets', children=''),

      html.Hr(),

      html.H4(children='Análise de frequência de substantivos'),
      dcc.Graph(id='live-graph', animate=False),

      html.Hr(),

      html.H4(children='Análise de frequência de fontes'),
      dcc.Graph(id='live-graph-sources', animate=False),

      dcc.Interval(
        id='graph-update',
        interval=1*1000, # in milliseconds
        n_intervals=0
      ),

      html.Hr(),

      html.H4(children='Análise de Localização dos usuários'),
      html.P(children='Análise das localizações que os usuários colocam em seus perfis'),
      dcc.Graph(id='live-graph-countries', animate=False),


    ]
)

# Callback do botão de enviar keyword
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

# Callback da label que mostra a qtd de tweets analisados
@app.callback(
  Output('number_tweets', 'children'),
  [Input('graph-update', 'n_intervals')]
)
def show_num_tweets(n):
  data = load_from_file(filename="number_tweets.json")
  return f'{data["count"]} tweets analisados'

# Callback do gráfico de frequência de termos (substantivos)
@app.callback(
  Output('live-graph', 'figure'),
  [Input('graph-update', 'n_intervals')]
)
def update_graph_tweets(n):
  data = load_from_file()
  data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

  data =  {'x': list(data.keys())[:15], 'y': list(data.values())[:15], 'type': 'bar', 'name': 'SF'}

  return { 'data': [data] }

# Callback do gráfico de frequência de países
@app.callback(
  Output('live-graph-countries', 'figure'),
  [Input('graph-update', 'n_intervals')]
  )
def update_graph_countries(n):
  data = load_from_file('countries.json')
  data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

  data =  {'x': list(data.keys())[:15], 'y': list(data.values())[:15], 'type': 'bar', 'name': 'SF'}

  return { 'data': [data] }

# Callback do gráfico de frequência de fontes
@app.callback(
  Output('live-graph-sources', 'figure'),
  [Input('graph-update', 'n_intervals')]
  )
def update_graph_sources(n):
  data = load_from_file('sources.json')
  data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

  data =  {'x': list(data.keys())[:15], 'y': list(data.values())[:15], 'type': 'bar', 'name': 'SF'}

  return { 'data': [data] }

############################3
# RUN SERVER
if __name__ == '__main__':
  app.run_server(debug=True)

