# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from floodsystem import station
from haversine import haversine


def stations_by_distance(stations, p):
    """returns a list of station-distance tuples sorted by distance"""
    station_distance = []
    """Initiate the returned list"""
    for instances in stations:
        """Iterate the stations list"""
        station_distance.append((instances.name, haversine(instances.coord, p)))
        """Append the tuples of station name and distance to the list"""
    station_distance_sorted = sorted_by_key(station_distance, 1)
    """Sort the list by the second key, which is the distance"""
    return station_distance_sorted


def stations_within_radius(stations, centre, r):
    """returns a list of stations within a certain radius"""
    all_stations = []
    returned = []
    for i in stations:
        all_stations.append((i, haversine(i.coord, centre)))
    all_stations = sorted(all_stations, key=lambda x: x[1])
    for i in all_stations:
        if i[1] <= r:
            returned.append(i[0])
        else:
            break
    return returned


def rivers_with_station(stations):
    """returns a set of rivers with at least one station"""
    rivers = set()
    for i in stations:
        rivers.add(i.river)
    return rivers


def stations_by_river(stations):
    """returns a dictionary that maps a river to its monitoring stations"""
    river_dict = {}
    for i in rivers_with_station(stations):
        river_dict[i] = []
    for j in stations:
        river_dict[j.river].append(j)
    return river_dict
