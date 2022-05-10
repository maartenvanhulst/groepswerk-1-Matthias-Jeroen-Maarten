from flask import Flask, render_template
from src.data_object import DataObject
import os
import pathlib

app = Flask(__name__, static_url_path="/static", static_folder="templates/static")


@app.route("/")
def index_html():
    return render_template("index.html", data=None)


if __name__ == "__main__":

    root_dir = pathlib.Path(os.getcwd())

    while not os.path.exists(os.path.join(root_dir, "connection.secret")):
        if os.path.exists(os.path.join(root_dir, "README.mb")):
            root_dir = os.path.join(root_dir, "./src")
        else:
            root_dir = pathlib.Path(root_dir.parent)
        os.chdir(root_dir)

    d_object = DataObject()

    root_dir = os.getcwd()
    print(root_dir)

    d_object.db_execute(open(os.path.join(root_dir, './database/create_db.sql'), 'r').read())
