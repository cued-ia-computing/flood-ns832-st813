from floodsystem import plot
from floodsystem import stationdata
import Flood


def run():
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)
    highest_stations = [i for i in Flood.stations_highest_rel_level(stations, 5)]
    for i in highest_stations:
        plot.plot_water_levels(i, 10)


if __name__ == "__main__":
    run()
