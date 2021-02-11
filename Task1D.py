from floodsystem import geo
from floodsystem import stationdata


def run():
    """Requirement for Task 1D"""
    rivers = geo.rivers_with_station(stationdata.build_station_list())
    print(len(rivers))
    print(sorted(rivers)[:10])

    for i in geo.stations_by_river(stationdata.build_station_list())["River Aire"]:
        print(i.name)
    for j in geo.stations_by_river(stationdata.build_station_list())["River Cam"]:
        print(j.name)
    for k in geo.stations_by_river(stationdata.build_station_list())["River Thames"]:
        print(k.name)


if __name__ == "__main__":
    run()
