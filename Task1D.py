from floodsystem import geo
from floodsystem import stationdata

rivers = geo.rivers_with_station(stationdata.build_station_list())
print(len(rivers))
print(sorted(rivers)[:10])

print(geo.stations_by_river(stationdata.build_station_list())["River Aire"])
print(geo.stations_by_river(stationdata.build_station_list())["River Cam"])
print(geo.stations_by_river(stationdata.build_station_list())["River Thames"])

