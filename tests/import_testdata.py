import pandas as pd
import numpy as np
import os

from src.controller.settings import Settings

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

from src.model.dc_contact import Contact as dcContact
from src.model.contact import Contact

from src.model.dc_location import Location as dcLocation
from src.model.location import Location


Settings.load()

xlsx = pd.ExcelFile(os.path.join(Settings.ROOT_DIR, 'tests', 'Testdata.xlsx'))
seasons = pd.read_excel(xlsx, 'Season')
leagues = pd.read_excel(xlsx, 'League')
competitions = pd.read_excel(xlsx, 'Competition')
series = pd.read_excel(xlsx, 'Series')
matchdays = pd.read_excel(xlsx, 'Matchday')
players = pd.read_excel(xlsx, 'Player')
clubs = pd.read_excel(xlsx, 'Club')
teams = pd.read_excel(xlsx, 'Team')
matches = pd.read_excel(xlsx, 'Match')
contact = pd.read_excel(xlsx, 'Contact')
location = pd.read_excel(xlsx, 'Location')
# Drop table and Recreate database

for index, row in clubs.iterrows():
    dc = dcClub(*row.tolist())
    c = Club(dc)
    c.db_execute(open(os.path.join(Settings.ROOT_DIR, 'src', 'database', 'create_db.sql'), 'r').read(), ['dummy'])
    break

for index, row in seasons.iterrows():
    row = row.replace({np.nan: None})
    dc = dcSeason(*row.tolist())
    c = Season(dc)
    c.insert()

for index, row in clubs.iterrows():
    row = row.replace({np.nan: None})
    dc = dcClub(*row.tolist())
    c = Club(dc)
    c.insert()

for index, row in leagues.iterrows():
    row = row.replace({np.nan: None})
    dc = dcLeague(*row.tolist())
    c = League(dc)
    c.insert()

for index, row in competitions.iterrows():
    row = row.replace({np.nan: None})
    dc = dcCompetition(*row.tolist())
    c = Competition(dc)
    c.insert()

for index, row in series.iterrows():
    row = row.replace({np.nan: None})
    dc = dcSeries(*row.tolist())
    c = Series(dc)
    c.insert()

for index, row in matchdays.iterrows():
    row = row.replace({np.nan: None})
    dc = dcMatchday(*row.tolist())
    c = Matchday(dc)
    c.insert()

for index, row in players.iterrows():
    row = row.replace({np.nan: None})
    dc = dcPlayer(*row.tolist())
    c = Player(dc)
    c.insert()

for index, row in location.iterrows():
    row = row.replace({np.nan: None})
    dc = dcLocation(*row.tolist())
    c = Location(dc)
    c.insert()

for index, row in teams.iterrows():
    row = row.replace({np.nan: None})
    dc = dcTeam(*row.tolist())
    c = Team(dc)
    c.insert()

for index, row in matches.iterrows():
    row = row.replace({np.nan: None})
    dc = dcMatch(*row.tolist())
    c = Match(dc)
    c.insert()

for index, row in contact.iterrows():
    row = row.replace({np.nan: None})
    dc = dcContact(*row.tolist())
    c = Contact(dc)
    c.insert()



