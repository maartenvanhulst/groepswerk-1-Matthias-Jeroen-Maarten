import pandas as pd
import numpy as np
import os
from src.controller.settings import Settings

Settings.load()

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

for index, row in clubs.iterrows():
     dc = dcClub(*row.tolist())
     c = Club(dc)
     c.db_execute(open(os.path.join(Settings.ROOT_DIR, 'src', 'database', 'create_db.sql'), 'r').read(), ['dummy'])
     break

# for index, row in seasons.iterrows():
#     row = row.replace({np.nan: None})
#     dc = dcSeason(*row.tolist())
#     c = Season(dc)
#     c.insert()
#
# for index, row in clubs.iterrows():
#     row = row.replace({np.nan: None})
#     dc = dcClub(*row.tolist())
#     c = Club(dc)
#     c.insert()
#
# for index, row in matches.iterrows():
#     row = row.replace({np.nan: None})
#     dc = dcMatch(*row.tolist())
#     c = Match(dc)
#     c.insert()
#
# for index, row in matchdays.iterrows():
#     row = row.replace({np.nan: None})
#     dc = dcMatchday(*row.tolist())
#     c = Matchday(dc)
#     c.insert()

