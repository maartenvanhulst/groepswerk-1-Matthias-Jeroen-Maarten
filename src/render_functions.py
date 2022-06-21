# Render tables requires a dict of 2 list:
# - Column names
# - Row data

def table_all(c):
    return {"Column_names": list(c.model.__dataclass_fields__.keys()), "data": c.fetch_all()}


def table_ranking(data, details=True):
    header = ['Plaats',
              'Team',
              'Punten',
              'Gespeelde Matchen',
              'Gewonnen',
              'Gelijk Gespeeld',
              'Verloren',
              'Goals gemaakt',
              'Tegen Goals',
              'Goals delta']
    new_data = []
    for row in data:
        row_lst = list(row)
        new_data.append(row_lst)

    if not details:
        header = header[0:4]
        new_data = []
        for row in data:
            new_data.append(row[0:4])

    return {"Column_names": header, "data": new_data}


def table_calender(data):
    header = ['Thuisploeg',
              'VS',
              'Bezoekers',
              'Locatie',
              'Datum',
              'Tijdstip'
              ]
    new_data = []
    for row in data:
        row_lst = list(row)

        new_data.append(row_lst)

    return {"Column_names": header, "data": new_data}


def table_results(data, recent_results=False):
    header = ['Thuisploeg',
              'VS',
              'Bezoekers',
              'Score'
              ]

    new_data = []
    for row in data:
        row_lst = list(row)
        new_data.append(row_lst)

    # Shows last 3 played matches, could be based on last week or matchday too

    if recent_results:
        new_data = []
        count = 3
        for row in data:

            if count > 0:
                new_data.append(row)

            count -= 1

    return {"Column_names": header, "data": new_data}


def table_scoring(data):
    header = ['Date',
              'Thuisploeg',
              'VS',
              'Bezoekers',
              'Punten Thuisploeg',
              'Punten Bezoekers',
              'Edit'
              ]
    new_data = []
    for row in data:
        row_lst = list(row)
        new_data.append(row_lst)

    return {"Column_names": header, "data": new_data}

def table_team(data, clubs):
    header = ['Id',
              'Team Name',
              'Display Name',
              'Home color 1',
              'Home color 2',
              'Home color 3',
              'Away color 1',
              'Away color 2',
              'Away color 3',
              'Alt color 1',
              'Alt color 2',
              'Alt color 3',
              'Club'
              ]

    new_data = []
    for row in data:
        row_lst = list(row)
        club_id = row_lst[12]

        row_lst[12] = clubs[club_id-1][1]
        new_data.append(row_lst)

    return {"Column_names": header, "data": new_data}


if __name__ == "__main__":
    pass
