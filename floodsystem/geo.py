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

def rivers_by_station_number(stations, N):
    """Returns a tuple (river name, n.o. stations) with 'N' entries, sorted by n.o stations"""
    river_dict = stations_by_river(stations)
    #print(river_dict)
    """Creates two lists, one with the rivers and the other with the instances"""
    rivers = ['River']
    number = [5]
    """Takes dictionary of rivers and checks to see if the river is in rivers_sorted"""
    for i in river_dict:
        print(i)
        print((rivers[0]))
        """Raise exception if type doesn't match what's expected"""
        if type(i) != str:
            raise Exception

        if i in rivers:
            #error in the code here, if you replace it with "if 'test' in rivers" it will call the function but otherwise it doesn't call this if function (despite being a string)
            """if in list find position within the list and add '1' onto the corresponding count in the number list"""
            position = rivers.index(i)
            number[position] +=1
        else:
            """If not in the list add a new entry along with an entry in the number list"""
            rivers.append (i)
            number.append (1)

    """Zips the two lists together into a list and reverse sorts"""
    new = sorted(list(zip(rivers,number)), key=lambda x: x[1], reverse=True)

    """Slices and returns, checking if there are more stations with the same number"""
    nsort = sorted(number, reverse=True)
    while nsort[N-1] == nsort[N]:
        N +=1
        if N>50: #just to limit the list of data for troubleshooting
            break
        print ("ADDED")
    
    return new [:N]
    

def inconsistent_typical_range_stations(stations):
    "Takes list of stations and returns those with inconsistent typical values"
    inconsistent_stations = []
    for i in range(len(stations)):
        if typical_range_consistent(stations[i]) == False:
            inconsistent_stations.append (stations[i].name)
    return sorted(inconsistent_stations)