from src.model.dc_series import Series as dcSeries
from src.model.series import Series

def table_all(c):
    return {"Column_names": list(c.model.__dataclass_fields__.keys()), "data": c.fetch_all()}

def table_ranking(data, details=True):
    header = ['position',
              'team_id',
              'team_name',
              'points',
              'matches',
              'wins',
              'draws',
              'losses',
              'goals_made',
              'goals_against',
              'goals_delta']

    new_data = data

    if details == False:
        header = header[2:5]
        new_data = []
        for row in data:
            new_data.append(row[2:5])

    return {"Column_names": header, "data": new_data}

if __name__ == "__main__":
    dc = dcSeries(1, "a", 1, 1)
    c = Series(dc)

    print(list(table_all(c)))