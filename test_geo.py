from floodsystem import geo
from floodsystem import station
from floodsystem import stationdata
from Flood import stations_level_over_threshold
from Flood import stations_highest_rel_level


def test_data():
    s_id = "test-s-1"
    m_id = "test-m-1"
    label = "oxford station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "oxford"
    s1 = station.MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s_id = "test-s-2"
    m_id = "test-m-2"
    label = "cambridge station"
    coord = (0, 1)
    town = "cambridge"
    s2 = station.MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s_id = "test-s-3"
    m_id = "test-m-3"
    label = "cambridge station 2"
    coord = (0, 2)
    s3 = station.MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s_id = "test-s-4"
    m_id = "test-m-4"
    label = "cambridge station 3"
    coord = (0, 2)
    river = "River Y"
    s4 = station.MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s4.latest_level = 5
    s4.typical_range = (-2.3, 3.4445)
    river = 'River Z'
    s5 = station.MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s5.latest_level = 0.1
    s5.typical_range = (-2.3, 3.4445)
    return [s1, s2, s3, s4, s5]


def test_stations_by_distance():
    result = geo.stations_by_distance(test_data(), (0, 0))
    assert result[0] == ('cambridge station', 111.1950802335329)


def test_stations_within_radius():
    result = geo.stations_within_radius(test_data(), (0, 0), 0)
    assert len(result) == 0
    assert type(result) == list


def test_rivers_with_station():
    result = geo.rivers_with_station(test_data())
    assert len(result) == 3
    assert result.__contains__('River X' and 'River Y' and 'River Z')


def test_stations_by_river():
    result = geo.stations_by_river(test_data())
    assert (len(result["River Y"])) == 1
    assert (type(result) == dict)


def test_rivers_by_station_number():
    result = geo.rivers_by_station_number(test_data(), 1)
    assert len(result) == 1
    assert result[0] == ['River X', 3]


def test_relative_water_level():
    result = stations_level_over_threshold(test_data(), 0.8)
    assert result == [('cambridge station 3', 1.2707807468012882)]


def alltest():
    test_stations_by_distance()
    test_stations_within_radius()
    test_rivers_with_station()
    test_stations_by_river()
    test_rivers_by_station_number()
    test_relative_water_level()
    print("ALL CLEAR")


alltest()
