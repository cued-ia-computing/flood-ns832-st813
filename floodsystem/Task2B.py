from floodsystem import stationdata
from stationdata import relative_water_level
from stationdata import update_water_levels

def run():
    stations = stationdata.build_station_list()
    update_water_levels(stations)
    rel_level = relative_water_level(stations)
    print(rel_level)


if __name__ == "__main__":
    run()


