from floodsystem import plot
from floodsystem import stationdata
import Flood
from floodsystem import datafetcher
import datetime


def run():
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)
    highest_stations = [i for i in Flood.stations_highest_rel_level(stations, 5)]

    for i in highest_stations:
        dates, levels = datafetcher.fetch_measure_levels(i.measure_id, datetime.timedelta(2))
        plot.plot_water_level_with_fit(i, dates, levels, 4)


if __name__ == "__main__":
    run()
