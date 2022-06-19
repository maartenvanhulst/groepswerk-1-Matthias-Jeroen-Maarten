from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import flask_login
import os
from src.controller.settings import Settings
import src.render_functions as render_functions

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

from src.data_object import DataObject

from src.model.dc_contact import Contact as dcContact
from src.model.contact import Contact


Settings.load()

app = Flask(__name__, static_url_path="/static", static_folder="../view/static", template_folder="../view")
app.secret_key = 'super secret string'  # Change this!
app.config["UPLOAD_FOLDER"] = "src/view/static/downloads"

# Create login manager

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

#  Define users and set up the system to manage these

users = {'admin': {'password': 'root'}, 'test': {'password': 'test'}}   # Test values, needs to migrate to DB


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(user_request):
    email = user_request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user


# MAIN PAGE


@app.route("/")
def index_html():

    # homepage contains 2 tables pass data for second table by adding a second data set
    # and assigning this data in html template (% set data = data2 %)

    data_object = DataObject(None)
    query = open(os.path.join(Settings.ROOT_DIR, 'src', 'database', 'ranking_by_series_id.sql'), 'r').read()
    ranking = data_object.db_execute(query, [1, 1])

    data_object = DataObject(None)
    query = open(os.path.join(Settings.ROOT_DIR, 'src', 'database', 'get_results.sql'), 'r').read()
    results = data_object.db_execute(query)

    return render_template("pages/home.html", data=render_functions.table_ranking(ranking, details=False), data2=render_functions.table_results(results, True))


@app.route("/kalender")
def kalender_html():

    data_object = DataObject(None)
    query = open(os.path.join(Settings.ROOT_DIR, 'src', 'database', 'get_calender.sql'), 'r').read()
    calender = data_object.db_execute(query)
    return render_template("pages/kalender.html", data=render_functions.table_calender(calender))


@app.route("/resultaten")
def resultaten_html():

    data_object = DataObject(None)
    query = open(os.path.join(Settings.ROOT_DIR, 'src', 'database', 'get_results.sql'), 'r').read()
    results = data_object.db_execute(query)
    return render_template("pages/kalender.html", data=render_functions.table_results(results))


@app.route("/rangschikking")
def rangschikking_html():

    data_object = DataObject(None)
    ranking = data_object.db_execute(
        open(os.path.join(Settings.ROOT_DIR, 'src', 'database', 'ranking_by_series_id.sql'), 'r').read(), [1, 1])
    return render_template("pages/kalender.html", data=render_functions.table_ranking(ranking))


@app.route("/contact")
def contact():

    get_dataclass_contact = dcContact()
    contact_obj = Contact(get_dataclass_contact)
    contacts = contact_obj.fetch_all()

    return render_template("pages/contact.html", data=contacts)


@app.route("/downloads")
def downloads():

    return render_template("pages/downloads.html")


# To download a file a route is created dynamically based on filename and root location


@app.route('/downloads/<path:filename>/', methods=['GET', 'POST'])
def download(filename):

    # locate downloads folder
    uploads = os.path.join(Settings.ROOT_DIR, app.config["UPLOAD_FOLDER"])

    # Returning file from appended path
    return send_from_directory(directory=uploads, path=filename, as_attachment=True)


# Login and admin page


@app.route('/login', methods=['GET', 'POST'])
def login():

    # Store user input data
    email = request.form.get('input_username')
    password = request.form.get('input_password')

    if request.method == 'GET':

        return render_template("pages/login.html", login="")

    # Check user and password
    if email in users and password == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('protected'))

    return render_template("pages/login.html", login="login failed")


@app.route('/protected', methods=['GET', 'POST'] )
@flask_login.login_required
def protected():
    user_info = 'Logged in as ' + flask_login.current_user.id
    data_object = DataObject(None)
    query = open(os.path.join(Settings.ROOT_DIR, 'src', 'database', 'get_scoring_table.sql'), 'r').read()
    scoring_table = data_object.db_execute(query)

    return render_template("pages/protected.html", user_info=user_info, data=render_functions.table_scoring(scoring_table))


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect("/")


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401


if __name__ == "__main__":
    pass
