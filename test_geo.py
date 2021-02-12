from floodsystem import geo
from floodsystem import station
from floodsystem import stationdata
from haversine import haversine

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
    return [s1, s2]

def test_stations_by_distance():
    result = geo.stations_by_distance(test_data(), (0, 0))
    assert result[0][1] == 1


def test_stations_within_radius():
    result = geo.stations_within_radius(test_data(), (0, 0), 1)
    assert len(result) == 1
    assert result.__contains__(test_data()[1])


def test_rivers_with_station():
    result = geo.rivers_with_station(test_data)
    assert result.__sizeof__() == 1


def test_stations_by_river():
    result = geo.stations_by_river(test_data)
    assert result["River X"].label == "cambridge station"


def test_rivers_by_station_number():
    s_id = "test-s-2"
    m_id = "test-m-2"
    label = "cambridge station 2"
    coord = (0, 2)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "cambridge"
    s3 = station.MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    stations = [test_data()[0], test_data()[1], s3]
    result = geo.rivers_by_station_number(stations, 2)
    assert len(result) == 1

def test_relative_water_level():
    return(stationdata.relative_water_level(test_data()))

print(test_relative_water_level())