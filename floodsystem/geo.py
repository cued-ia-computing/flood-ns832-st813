# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from floodsystem import station
from haversine import haversine
from collections import Counter


def stations_by_distance(stations, p):
    """returns a list of station-distance tuples sorted by distance"""
    station_distance = []
    # Initiate the returned list
    for instances in stations:
        # Iterate the stations list
        station_distance.append((instances.name, haversine(instances.coord, p)))
        # Append the tuples of station name and distance to the list
    station_distance_sorted = sorted_by_key(station_distance, 1)
    # Sort the list by the second key, which is the distance
    return station_distance_sorted


def stations_within_radius(stations, centre, r):
    """returns a list of stations within a certain radius"""
    all_stations = []
    returned = []
    for i in stations:
        all_stations.append((i, haversine(i.coord, centre)))
    # Add all stations and its distance to the list
    all_stations = sorted(all_stations, key=lambda x: x[1])
    # Sort the list according to the second key
    for i in all_stations:
        if i[1] <= r:
            returned.append(i[0])
        else:
            break
    # Add all stations within the radius in the sorted list to returned
    return returned


def rivers_with_station(stations):
    """returns a set of rivers with at least one station"""
    rivers = set()
    for i in stations:
        if i.river != "":
            rivers.add(i.river)
    # adding rivers to a set that doesn't allow repeated elements
    return rivers


def stations_by_river(stations):
    """returns a dictionary that maps a river to its monitoring stations"""
    river_dict = {}
    for i in rivers_with_station(stations):
        river_dict[i] = []
    # creating the keys with all rivers
    for j in stations:
        river_dict[j.river].append(j)
    # adding all the stations to its river key
    return river_dict


def rivers_by_station_number(stations, N):
    """Returns a tuple (river name, n.o. stations) with 'N' entries, sorted by n.o stations"""
    rivers = []
    "Creates a list of rivers"
    for i in stations:
        rivers.append(i.river)
    "Counts number of instances and creates list of tuples, then sorts"
    counter = [[x, rivers.count(x)] for x in rivers]
    counter = sorted(counter, key=lambda x: x[1], reverse=True)
    "Removes repeats"
    norepeats = []
    for i in counter:
        if i not in norepeats:
            norepeats.append(i)
    "Slices and returns, checking if there are more stations with the same number"
    while norepeats[N - 1] == norepeats[N]:
        N += 1
    return norepeats[:N]


def inconsistent_typical_range_stations(stations):
    """Takes list of stations and returns those with inconsistent typical values"""
    inconsistent_stations = []
    for i in range(len(stations)):
        if not station.MonitoringStation.typical_range_consistent(stations[i]):
            inconsistent_stations.append(stations[i].name)
    return sorted(inconsistent_stations)
