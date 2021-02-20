from Flood import stations_highest_rel_level
from floodsystem import station
from floodsystem import stationdata


def run():
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)
    rivers = stations_highest_rel_level(stations, 10)
    riv = []
    for i in stations:
        if i.name in rivers:
            riv.append(i)
    rivers = station.MonitoringStation.relative_water_level(riv)[1:]
    for i in rivers:
        print(i)


if __name__ == "__main__":
    run()
