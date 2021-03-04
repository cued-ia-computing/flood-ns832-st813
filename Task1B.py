from floodsystem import geo
from floodsystem import stationdata


def run():
    """Requirement for Task 1B"""
    x = geo.stations_by_distance(stationdata.build_station_list(), (52.2053, 0.1218))
    print(x[:10])
    print(x[-10:])


if __name__ == "__main__":
    run()
