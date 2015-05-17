__author__ = 'michael'
import os
from django.contrib.gis.utils import LayerMapping
from monitor.models import MonitorStation

station_mapping = {
    'station_id': 'sta_num',
    'station_name': 'StationNam',
    'station_alt_name': 'StationID',
    'geom': 'POINT'
}

station_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'monitor/data/ccb_monitor_stations_5_12_2015.shp'))

def run(verbose=True):
    lm = LayerMapping(MonitorStation, station_shp, station_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
