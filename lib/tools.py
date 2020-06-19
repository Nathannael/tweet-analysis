import json

def save_to_file(data):
  json_file = json.dumps(data)
  f = open("data.json","w")
  f.write(json_file)
  f.close()
