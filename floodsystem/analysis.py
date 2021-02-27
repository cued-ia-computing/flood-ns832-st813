import matplotlib.dates as mdates
import numpy as np


def polyfit(dates, levels, p):
    x = mdates.date2num(dates)
    p_coeff = np.polyfit(x-x[0], levels, p)
    poly = np.poly1d(p_coeff)
    return poly, x[0]
