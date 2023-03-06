from flask import Flask,jsonify


app = Flask(__name__)



@app.route("/home")
def index():
  return("welcome to app")



if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 8000, debug=True)