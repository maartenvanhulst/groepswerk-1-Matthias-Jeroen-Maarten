from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/api/v1/hello/")
@app.route("/api/v1/hello/<name>")
def hello_json(name="world"):
    msg = {"hello": name}

    return jsonify(msg)


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_html(name="world"):
    data = {
        "person": {
            "first_name": "Yves",
            "last_name": "Vindevogel"
        }
    }
    return render_template("hello.html", data=data)
