from floodsystem import station
from floodsystem import stationdata
from stationdata import relative_water_level
from stationdata import update_water_levels


def run():
    stations = stationdata.build_station_list()
    update_water_levels(stations)
    rivers = flood(stations, 0.8)
    print(rivers)

def flood(stations, tol):
    rivers = []
    stations = relative_water_level(stations)
    "Filter out data with no relative level"
    stations = [i for i in stations if None not in i]
    "Checks ratio against tolerance"
    for station in stations:
        if station[1] > tol:
            rivers += [station[0], station[1]]
    return rivers


if __name__ == "__main__":
    run()
