import json

SERIES=[
  'Hollywood',
  'Noite Adentro',
  'Billions',
  'Supermães',
  'The Eddy',
  'Disque Amiga Para Matar',
  'Restaurantes em Risco',
  'Valéria',
  'Bordertown',
  'Outlander',
  'Gotham',
  'White Lines',
  'Mágica Para a Humanidade',
  'Índia Catalina',
  'Batalha das Flores',
  'Doces Magnólias',
  'Control Z',
  '13 Reasons Why'
]


def save_to_file(data):
  json_file = json.dumps(data)
  f = open("data.json","w")
  f.write(json_file)
  f.close()
