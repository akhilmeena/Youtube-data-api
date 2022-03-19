from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
  path = "static/Data/Data.json"
  data = get_static_json(path)
  return data

def get_static_json(path):
  with open(path, 'r') as f:
    data = json.load(f)
  pretty_json = json.dumps(data, indent=4) 
  print(pretty_json)
  return pretty_json



if __name__ == '__main__':
    app.run(debug=True)
