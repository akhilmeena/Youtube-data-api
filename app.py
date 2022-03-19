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
  return JSON.stringify(data, undefined, 2)

def get_static_json(path):
  with open(path, 'r') as f:
    data = json.load(f)
  print(data)
  return data



if __name__ == '__main__':
    app.run(debug=True)
