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