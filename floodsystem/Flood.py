from floodsystem import station
from floodsystem import stationdata
from stationdata import relative_water_level
from stationdata import update_water_levels


def run():
    stations = stationdata.build_station_list()
    update_water_levels(stations)
    rivers = flood(stations, 0.8)
    print(rivers)

def flood(stations, tol):
    rivers = []
    nstations = filter(None, relative_water_level(stations))
    for nstation in nstations:
        print(nstation)
        if nstation[1] > tol:
            rivers += [nstation[0], nstation[1]]
    return 0


if __name__ == "__main__":
    run()
