from flask import Flask, render_template
from src.data_object import DataObject
import os
import pathlib

app = Flask(__name__, static_url_path="/static", static_folder="templates/static")


@app.route("/")
def index_html():
    root_dir = os.getcwd()
    d_object = DataObject()
    d_object.db_execute(open(os.path.join(root_dir, 'src', 'database', 'get_clubs.sql'), 'r').read())
    resp = d_object.db_read()
    print(resp)
    return render_template("index.html", data=None)


if __name__ == "__main__":
    pass

