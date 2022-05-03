from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static", static_folder="templates/static")


@app.route("/")
def index_html():
    return render_template("index.html", data=None)
