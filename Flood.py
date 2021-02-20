from floodsystem import station
from floodsystem.station import MonitoringStation


def stations_level_over_threshold(stations, tol):
    rivers = []
    stations = MonitoringStation.relative_water_level(stations)
    "Filter out data with no relative level"
    stations = [i for i in stations if None not in i]
    "Checks ratio against tolerance"
    for s in stations:
        if s[1] > tol:
            rivers += [(s[0], s[1])]
    return rivers


def stations_highest_rel_level(stations, N):
    "Returns a list of the N stations where the relative water level is highest"
    stations = station.MonitoringStation.relative_water_level(stations)
    stations = [i for i in stations if None not in i]
    rivers = sorted(stations, key=lambda x: x[1], reverse=True)
    s = []
    for key, value in rivers:
        s.append(key)
    return s[:N]
