from Flood import stations_level_over_threshold
from floodsystem import stationdata


def run():
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)
    rivers = stations_level_over_threshold(stations, 0.8)
    print(len(rivers))
    print(rivers)


if __name__ == "__main__":
    run()
