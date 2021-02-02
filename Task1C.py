from floodsystem import geo
from floodsystem import stationdata


def run():
    """Requirement for Task 1C"""
    print(geo.stations_within_radius(stationdata.build_station_list(), (52.2053, 0.1218), 10))


if __name__ == "__main__":
    run()

