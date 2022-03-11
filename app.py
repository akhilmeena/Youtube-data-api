from flask import Flask
from flask import request, jsonify
from py_youtube import Data 
app = Flask(__name__)


@app.route('/<text>')
def home():
    return f"<h1>Get YouTube Video Data {{text}} akhil</h1>"


#@app.route('/<link>')
def show_Link():
  return f"<h1>Get YouTube Video Data \n {link} </h1>"

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
