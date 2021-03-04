from floodsystem import geo
from floodsystem import stationdata


def run():
    """Requirement for Task 1C"""
    station_list = geo.stations_within_radius(stationdata.build_station_list(), (52.2053, 0.1218), 10)
    for i in station_list:
        print(i.name)


if __name__ == "__main__":
    run()
