from floodsystem import geo
from floodsystem import station


def test_stations_by_distance():
    # Create stations
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
    stations = [s1, s2]
    result = geo.stations_by_distance(stations, (0, 0))
    assert result[0][1] == 1


def test_stations_within_radius():
    # Create stations
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
    stations = [s1, s2]
    result = geo.stations_within_radius(stations, (0, 0), 1)
    assert len(result) == 1
    assert result.__contains__(s2)


def test_rivers_with_station():
    # Create stations
    s_id = "test-s-1"
    m_id = "test-m-1"
    label = "oxford station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = ""
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
    stations = [s1, s2]
    result = geo.rivers_with_station(stations)
    assert result.__sizeof__() == 1


def test_stations_by_river():
    # Create stations
    s_id = "test-s-1"
    m_id = "test-m-1"
    label = "oxford station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River Y"
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
    stations = [s1, s2]
    result = geo.stations_by_river(stations)
    assert result["River X"].label == "cambridge station"


def test_rivers_by_station_number():
    # Create stations
    s_id = "test-s-1"
    m_id = "test-m-1"
    label = "oxford station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River Y"
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
    # Create stations
    s_id = "test-s-1"
    m_id = "test-m-1"
    label = "oxford station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River Y"
    town = "oxford"
    s1 = station.MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s_id = "test-s-2"
    m_id = "test-m-2"
    label = "cambridge station 2"
    coord = (0, 2)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "cambridge"
    s3 = station.MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    stations = [s1, s2, s3]
    result = geo.rivers_by_station_number(stations, 2)
    assert len(result) == 1
