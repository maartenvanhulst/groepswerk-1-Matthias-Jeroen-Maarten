from src.model.dc_series import Series as dcSeries
from src.model.series import Series

def table_all(c):
    return {"Column_names": list(c.model.__dataclass_fields__.keys()), "data": c.fetch_all()}

if __name__ == "__main__":
    dc = dcSeries(1, "a", 1, 1)
    c = Series(dc)

    print(list(table_all(c)))