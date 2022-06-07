from flask import Flask, render_template, send_from_directory
import os
import pathlib
from src.controller.settings import Settings

import render_functions

from src.model.dc_season import Season as dcSeason
from src.model.season import Season

from src.model.dc_league import League as dcLeague
from src.model.league import League

from src.model.dc_competition import Competition as dcCompetition
from src.model.competition import Competition

from src.model.dc_series import Series as dcSeries
from src.model.series import Series

from src.model.dc_matchday import Matchday as dcMatchday
from src.model.matchday import Matchday

from src.model.dc_player import Player as dcPlayer
from src.model.player import Player

from src.model.dc_club import Club as dcClub
from src.model.club import Club

from src.model.dc_team import Team as dcTeam
from src.model.team import Team

from src.model.dc_match import Match as dcMatch
from src.model.match import Match

Settings.load()


app = Flask(__name__, static_url_path="/static", static_folder="../view/static", template_folder="../view")
app.config["UPLOAD_FOLDER"] = "src/view/static/downloads"


# Testdata for creating tables
# html tables are created by a dictionary with 2 keys: column names and row data

column_name_ls1 = ["Thuisploeg", "VS", "Bezoekers", "Details"]
data_lst1 = [
    ("Testerkes Baatsem", "VS", "Bianconeri Roma", ("BOUTERSEM", "31/8/2020", "20:00")),
    ("Magos Rojos", "VS", "La Pazz", ("BOUTERSEM", "31/8/2020", "21:00")),
    ("Magos Rojos", "VS", "La Pazz", ("BOUTERSEM", "31/8/2020", "21:00"))
]

data_dict1 = {"Column_names": column_name_ls1, "data": data_lst1}

column_name_lst2 = ["Thuisploeg", "VS", "Bezoekers", "Details"]
data_lst2 = [
    ("Scorcio Baatsem", "VS", "Bianconeri Roma", ("BOUTERSEM", "31/8/2020", "20:00")),
    ("Magos Rojos", "VS", "La Pazz", ("BOUTERSEM", "31/8/2020", "21:00")),
    ("Magos Rojos", "VS", "La Pazz", ("BOUTERSEM", "31/8/2020", "21:00")),
    ("Scorcio Baatsem", "VS", "Bianconeri Roma", ("BOUTERSEM", "31/8/2020", "20:00")),
    ("Magos Rojos", "VS", "La Pazz", ("BOUTERSEM", "31/8/2020", "21:00")),
    ("Magos Rojos", "VS", "La Pazz", ("BOUTERSEM", "31/8/2020", "21:00"))
]

data_dict2 = {"Column_names": column_name_lst2, "data": data_lst2}

# Testdata for creating contact information cards
contact_data = [
    {"role": "Voorzitter", "name": "Nico Vandevin", "email": "nico.vandevin@hzvb.be", "phone": "0497/05.71.51"},
    {"role": "Secretaris", "name": "John Kempeneers", "email": "john.kempeneers@hzvb.be", "phone": "0477/61.98.84"},
    {"role": "Financieel beheerder", "name": "Annemie Lefevre", "email": "annemie.lefevre@hzvb.be", "phone": "0497/13.76.23"},
    {"role": "Bestuurslid", "name": "Fanny Vandendael", "email": "nfanny.vandendael@hzvb.be", "phone": "0472/52.86.30"},
    {"role": "Bestuurslid", "name": "Fanny Vandendael", "email": "nfanny.vandendael@hzvb.be", "phone": "0472/52.86.30"},
    {"role": "Bestuurslid", "name": "Fanny Vandendael", "email": "nfanny.vandendael@hzvb.be", "phone": "0472/52.86.30"},
]


@app.route("/")
def index_html():
    # homepage contains 2 tables pass data for second table by adding a second data set
    # and assigning this data in html template (% set data = data2 %)
    dc = dcSeries(1, "a", 1, 1)
    obj = Series(dc)
    data_dict1 = render_functions.table_all(obj)
    return render_template("pages/home.html", data=data_dict1, data2=data_dict2)


@app.route("/kalender/")
def kalender_html():
    return render_template("pages/kalender.html", data=data_dict1)


@app.route("/resultaten/")
def resultaten_html():
    return render_template("pages/kalender.html", data=data_dict1)


@app.route("/rangschikking/")
def rangschikking_html():
    return render_template("pages/kalender.html", data=data_dict1)


@app.route("/contact/")
def contact():
    return render_template("pages/contact.html", data=contact_data)


@app.route("/downloads/")
def downloads():
    return render_template("pages/downloads.html", data=data_dict1)


@app.route('/downloads/<path:filename>', methods=['GET', 'POST'])
def download(filename):

    # locate downloads folder
    root_dir = os.getcwd()
    while not os.path.exists(os.path.join(root_dir, 'src', "view", "static", "downloads")):
        root_dir = pathlib.Path(root_dir.parent)
    uploads = os.path.join(root_dir, app.config["UPLOAD_FOLDER"])

    # Returning file from appended path
    return send_from_directory(directory=uploads, path=filename, as_attachment=True)


@app.route("/login/")
def login():

    return render_template("pages/login.html", data=data_dict1)


if __name__ == "__main__":
    pass
