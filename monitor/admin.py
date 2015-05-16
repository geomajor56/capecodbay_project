from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import MonitorStation, SampleParameters


class MonitorAdmin(LeafletGeoAdmin):
    fields = (('station_id', 'station_name'), 'geom')
    list_display = ('station_id', 'station_name')
    search_fields = ['station_id', 'station_name']

class SampleAdmin(admin.ModelAdmin):
    list_display = ('station', 'cruise_date', 'depth_class')
    list_filter = ['station']




admin.site.register(SampleParameters, SampleAdmin)
admin.site.register(MonitorStation, MonitorAdmin)
