from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.gis.db import models as gismodels
from django.core.validators import MaxValueValidator, MinValueValidator


class MonitorStation(gismodels.Model):
    station_id = models.CharField(max_length=20, primary_key=True)
    station_name = models.CharField(max_length=50)
    station_alt_name = models.CharField(max_length=50, null=True)
    station_type = models.CharField(max_length=20, null=True)

    geom = gismodels.PointField()

    objects = gismodels.GeoManager()

    class Meta:
        verbose_name = 'Monitor Station'
        verbose_name_plural = 'Monitor Stations'
        ordering = ['station_name']

    # @python_2_unicode_compatible
    def __str__(self):
        return self.station_name


class SampleParameters(models.Model):
    station = models.ForeignKey(MonitorStation)
    cruise = models.CharField(max_length=20, null=True)
    cruise_date = models.DateField('Cruise Date')
    depth_class = models.IntegerField()
    temp = models.FloatField(null=True, validators=[MaxValueValidator(40)], verbose_name='Temperature')
    salinity = models.FloatField(null=True, validators=[MaxValueValidator(200)], verbose_name='Salinity')
    dissolved_o = models.FloatField(null=True, validators=[MaxValueValidator(200)], verbose_name='Dissolved Oxygen')
    ph = models.FloatField(null=True, validators=[MaxValueValidator(200)])
    chl = models.FloatField(null=True, validators=[MaxValueValidator(200)], verbose_name='Chlorophyll')
    pheo = models.FloatField(null=True, validators=[MaxValueValidator(200)], verbose_name='Pheophytin')
    turb = models.FloatField(null=True, validators=[MaxValueValidator(200)], verbose_name='Turbidity')
    no = models.FloatField(null=True, validators=[MaxValueValidator(200)], verbose_name='Nitrates')
    nh = models.FloatField(null=True, validators=[MaxValueValidator(200)], verbose_name='Ammonium')
    po = models.FloatField(null=True, validators=[MaxValueValidator(200)], verbose_name='Ortho-Phosphates')
    si = models.FloatField(null=True, validators=[MaxValueValidator(200)], verbose_name='Silicates')
    tn = models.FloatField(null=True, validators=[MaxValueValidator(200)], verbose_name='Total Nitrogen)')
    tp = models.FloatField(null=True, validators=[MaxValueValidator(200)], verbose_name='Total Phosphates')

    class Meta:
        verbose_name = 'Parameter'
        verbose_name_plural = 'Sample Results'

    # @python_2_unicode_compatible
    def __str__(self):
        return self.station_id
