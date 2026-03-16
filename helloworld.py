from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hlo world"

app.run(host="0.0.0.0", port=5000)

print("hello this is my first python program")
