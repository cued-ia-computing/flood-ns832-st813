from floodsystem import geo
from floodsystem import stationdata

def run():
    sorted_stations = geo.rivers_by_station_number(stationdata.build_station_list(),5)
    print (sorted_stations)

if __name__ == "__main__":
    run()