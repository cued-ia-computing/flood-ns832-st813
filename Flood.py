from floodsystem import station
from floodsystem import stationdata
from floodsystem.stationdata import relative_water_level
from floodsystem.stationdata import update_water_levels



def stations_level_over_threshold(stations, tol):
    rivers = []
    stations = relative_water_level(stations)
    "Filter out data with no relative level"
    stations = [i for i in stations if None not in i]
    "Checks ratio against tolerance"
    for station in stations:
        if station[1] > tol:
            rivers += [(station[0], station[1])]
    return rivers


def stations_highest_rel_level(stations, N):
    "Returns a list of the N stations where the relative water level is highest"
    stations = relative_water_level(stations)
    stations = [i for i in stations if None not in i]
    rivers = sorted(stations, key=lambda x: x[1], reverse=True)
    return rivers[:N]
