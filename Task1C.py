from floodsystem import geo
from floodsystem import stationdata
print(geo.stations_within_radius(stationdata.build_station_list(), (52.2053, 0.1218), 10))