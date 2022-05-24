import pandas as pd
import numpy as np
import os
from src.controller.settings import Settings

Settings.load()

from src.model.dc_club import Club as dcClub
from src.model.club import Club

from src.model.dc_match import Match as dcMatch
from src.model.match import Match

from src.model.dc_matchday import Matchday as dcMatchday
from src.model.matchday import Matchday


xlsx = pd.ExcelFile(os.path.join(os.getcwd(), 'tests', 'Testdata.xlsx'))
clubs = pd.read_excel(xlsx, 'Club')
matches = pd.read_excel(xlsx, 'Match')
matchdays = pd.read_excel(xlsx, 'Matchday')


for index, row in clubs.iterrows():
    dc = dcClub(*row.tolist())
    c = Club(dc)
    c.db_execute(open(os.path.join(Settings.ROOT_DIR, 'src', 'database', 'create_db.sql'), 'r').read(), ['dummy'])
    break

for index, row in clubs.iterrows():
    row = row.replace({np.nan: None})
    dc = dcClub(*row.tolist())
    c = Club(dc)
    c.insert()

# for index, row in matches.iterrows():
#     row = row.replace({np.nan: None})
#     dc = dcMatch(*row.tolist())
#     c = Match(dc)
#     c.insert()

for index, row in matchdays.iterrows():
    row = row.replace({np.nan: None})
    dc = dcMatchday(*row.tolist())
    c = Matchday(dc)
    c.insert()

