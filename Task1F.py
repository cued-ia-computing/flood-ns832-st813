from floodsystem import stationdata
from floodsystem.geo import inconsistent_typical_range_stations


def run():
    stat = inconsistent_typical_range_stations(stationdata.build_station_list())
    print(stat)


if __name__ == "__main__":
    run()
