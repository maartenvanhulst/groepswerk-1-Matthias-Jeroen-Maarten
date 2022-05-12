from flask import Flask, render_template
from src.data_object import DataObject
import os
import pathlib

app = Flask(__name__, static_url_path="/static", static_folder="templates/static")

list1 = [3, 'xyz?!', 127, 3320, 'Hoegaarden', 'Belgium', '', '', '', '', '', '', '', '', '', True]

@app.route("/")
def index_html():
    root_dir = os.getcwd()
    d_object = DataObject()
    query = d_object.db_execute(open(os.path.join(root_dir, 'src', 'database', 'add_club.sql'), 'r').read(),data=list1)
    print(query)
    return render_template("index.html", data=None)


if __name__ == "__main__":
    pass

