from Flood import stations_highest_rel_level
from floodsystem import stationdata


def run():
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)
    rivers = stations_highest_rel_level(stations, 10)
    print(rivers)


if __name__ == "__main__":
    run()
