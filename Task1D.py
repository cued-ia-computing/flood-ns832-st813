from floodsystem import geo
from floodsystem import stationdata


def run():
    """Requirement for Task 1D"""
    rivers = geo.rivers_with_station(stationdata.build_station_list())
    print(len(rivers))
    print(sorted(rivers)[:10])

    print(geo.stations_by_river(stationdata.build_station_list())["River Aire"].name)
    print(geo.stations_by_river(stationdata.build_station_list())["River Cam"].name)
    print(geo.stations_by_river(stationdata.build_station_list())["River Thames"].name)


if __name__ == "__main__":
    run()
