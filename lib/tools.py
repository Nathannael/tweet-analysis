import json

def save_to_file(data, filename="data.json"):
  json_file = json.dumps(data)
  f = open(filename,"w")
  f.write(json_file)
  f.close()
