from flask import Flask, render_template

app = Flask(__name__)

def get_static_json(path):
    return json.load(open(get_static_file(path)))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
  path = "static/Data/Data.json"
  data = get_static_json(path)
  return data

if __name__ == '__main__':
    app.run(debug=True)
