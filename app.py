from flask import Flask
from flask import *
from flask import request, jsonify
from py_youtube import Data 
app = Flask(__name__)


@app.route('/')
def home():
    return f"<h1>Get YouTube Video Data</h1>"

@app.route('/user/<uname>')  
def message(uname):  
  return render_template('Home.html',name=uname)

@app.route('/api/<link>')
def show_Link(link):
  text = f"<h1>Get YouTube Video Data \n {{link}} </h1>".format(link=link)
  return text
#@app.route('/api')
def api_id():
    if "link" in request.args:
        id = request.args['link']
    else:
        return "Error: No link field provided"
    yt = Data(id).data()
    return jsonify(yt)
        
if __name__ == "__main__":
    app.run( debug=True)
