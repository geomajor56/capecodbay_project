# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonitorStation',
            fields=[
                ('station_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('station_name', models.CharField(max_length=50)),
                ('station_alt_name', models.CharField(max_length=50, null=True)),
                ('station_type', models.CharField(max_length=20, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'ordering': ['station_name'],
                'verbose_name': 'Monitor Station',
                'verbose_name_plural': 'Monitor Stations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SampleParameters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cruise', models.CharField(max_length=20, null=True)),
                ('cruise_date', models.DateField(verbose_name=b'Cruise Date')),
                ('depth_class', models.IntegerField()),
                ('temp', models.FloatField(verbose_name=b'Temperature', validators=[django.core.validators.MaxValueValidator(40)])),
                ('salinity', models.FloatField(verbose_name=b'Salinity', validators=[django.core.validators.MaxValueValidator(200)])),
                ('dissolved_o', models.FloatField(verbose_name=b'Dissolved Oxygen', validators=[django.core.validators.MaxValueValidator(200)])),
                ('ph', models.FloatField(verbose_name=b'pH', validators=[django.core.validators.MaxValueValidator(200)])),
                ('chl', models.FloatField(verbose_name=b'Chlorophyll', validators=[django.core.validators.MaxValueValidator(200)])),
                ('pheo', models.FloatField(verbose_name=b'Pheophytin', validators=[django.core.validators.MaxValueValidator(200)])),
                ('turb', models.FloatField(verbose_name=b'Turbidity', validators=[django.core.validators.MaxValueValidator(200)])),
                ('no', models.FloatField(verbose_name=b'Nitrates', validators=[django.core.validators.MaxValueValidator(200)])),
                ('nh', models.FloatField(verbose_name=b'Ammonium', validators=[django.core.validators.MaxValueValidator(200)])),
                ('po', models.FloatField(verbose_name=b'Ortho-Phosphates', validators=[django.core.validators.MaxValueValidator(200)])),
                ('si', models.FloatField(verbose_name=b'Silicates', validators=[django.core.validators.MaxValueValidator(200)])),
                ('tn', models.FloatField(verbose_name=b'Total Nitrogen)', validators=[django.core.validators.MaxValueValidator(200)])),
                ('tp', models.FloatField(verbose_name=b'Total Phosphates', validators=[django.core.validators.MaxValueValidator(200)])),
                ('station', models.ForeignKey(to='monitor.MonitorStation')),
            ],
            options={
                'verbose_name': 'Parameter',
                'verbose_name_plural': 'Sample Results',
            },
            bases=(models.Model,),
        ),
    ]
