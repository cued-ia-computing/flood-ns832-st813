import matplotlib.pyplot as plt
import datetime
from floodsystem import datafetcher


def plot_water_levels(station, dates=None, levels=None):
    dates, levels = datafetcher.fetch_measure_levels(station.measure_id, datetime.timedelta(dates))
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, levels)
    plt.plot(dates, [station.typical_range[0] for i in range(len(dates))])
    plt.plot(dates, [station.typical_range[1] for i in range(len(dates))])
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(station.name)
    plt.tight_layout()
    fig.autofmt_xdate()
    plt.show()
