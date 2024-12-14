from flask import Flask , render_template, request
import db

app = Flask(__name__)
app.secret_key = "rookie"

@app.route("/")
def Home():
    return rener_template("index.html")

app.run(debug=True, port=5000)