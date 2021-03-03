"""if the level is beyond typical high: severe
if the level is above the average of typical high and low and is rising: high
if the level is above the average of typical high and low and is decreasing: moderate
if the level is below the average of typical high and low: low"""

from floodsystem import stationdata
from floodsystem import datafetcher
import datetime
import matplotlib.dates as mdates


def monotonocity(station, dates, levels):
    return (levels[-1]-levels[0])/(mdates.date2num(dates[-1])-mdates.date2num(dates[0]))


def run():
    stations = stationdata.build_station_list()
    stationdata.update_water_levels(stations)
    category = {'severe': [], 'high': [], 'moderate': [], 'low': []}
    for i in stations:
        dates, levels = datafetcher.fetch_measure_levels(i.measure_id, datetime.timedelta(1))
        if i.typical_range_consistent() and levels:
            if levels[-1] >= i.typical_range[1]:
                category['severe'].append(i.name)
            elif levels[-1] < i.typical_range[1]:
                if levels[-1] >= (i.typical_range[1]+i.typical_range[0])/2 and monotonocity(i, dates, levels) >= 0:
                    category['high'].append(i.name)
                elif levels[-1] >= (i.typical_range[1]+i.typical_range[0])/2 and monotonocity(i, dates, levels) < 0:
                    category['moderate'].append(i.name)
                else:
                    category['low'].append(i.name)
    print(category)


if __name__ == "__main__":
    run()
