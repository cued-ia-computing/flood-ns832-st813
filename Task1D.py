from floodsystem import geo
from floodsystem import stationdata


def run():
    """Requirement for Task 1D"""
    rivers = geo.rivers_with_station(stationdata.build_station_list())
    print(len(rivers), "stations. First 10 - ", sorted(rivers)[:10])
    RA = []
    print('River Aire')
    for i in geo.stations_by_river(stationdata.build_station_list())["River Aire"]:
        RA.append(i.name)
    print(sorted(RA))
    RC = []
    print('River Cam')
    for j in geo.stations_by_river(stationdata.build_station_list())["River Cam"]:
        RC.append(j.name)
    print(sorted(RC))
    RT = []
    print('River Thames')
    for k in geo.stations_by_river(stationdata.build_station_list())["River Thames"]:
        RT.append(k.name)
    print(sorted(RT))


if __name__ == "__main__":
    run()
