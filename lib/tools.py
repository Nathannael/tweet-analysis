import json

def save_to_file(data, filename="data.json"):
  json_file = json.dumps(data)
  f = open("data/"+filename,"w")
  f.write(json_file)
  f.close()

def load_from_file(filename="data.json"):
  return json.load(open("data/"+filename))
