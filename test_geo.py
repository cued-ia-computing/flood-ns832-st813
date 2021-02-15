from floodsystem import geo
from floodsystem import station
from floodsystem import stationdata
from Task2B import flood


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
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "cambridge"
    s2 = station.MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s_id = "test-s-2"
    m_id = "test-m-2"
    label = "cambridge station 2"
    coord = (0, 2)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "cambridge"
    s3 = station.MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s_id = "test-s-2"
    m_id = "test-m-2"
    label = "cambridge station 2"
    coord = (0, 2)
    trange = (-2.3, 3.4445)
    river = "River Y"
    town = "cambridge"
    s4 = station.MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s4.latest_level = 5
    river = 'River Z'
    s5 = station.MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s5.latest_level = 0.1
    return [s1, s2, s3, s4, s5]


def test_stations_by_distance():
    result = geo.stations_by_distance(test_data(), (0, 0))
    assert result[0] == ('cambridge station', 111.1950802335329)


def test_stations_within_radius():
    result = geo.stations_within_radius(test_data(), (0, 0), 1)
    #print(len(result))
    #assert len(result) == 1
    #assert result.__contains__('cambridge station')


def test_rivers_with_station():
    result = geo.rivers_with_station(test_data())
    assert len(result) == 3
    assert result.__contains__('River X' and 'River Y' and 'River Z')


def test_stations_by_river():
    result = geo.stations_by_river(test_data())
    assert (len(result["River Y"])) == 1
    #assert result["River Y"].label == "cambridge station 2"


def test_rivers_by_station_number():
    result = geo.rivers_by_station_number(test_data(), 1)
    assert len(result) == 1
    assert result[0] == ['River X', 3]


def test_relative_water_level():
    result = flood(test_data(), 0.8)
    assert result[1] == ('cambridge station 2', 1.2707807468012882)


def alltest():
    test_stations_by_distance()
    test_stations_within_radius()
    test_rivers_with_station()
    test_stations_by_river()
    test_rivers_by_station_number()
    test_relative_water_level()
    print("ALL CLEAR")

alltest()