# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampleparameters',
            name='chl',
            field=models.FloatField(null=True, verbose_name=b'Chlorophyll', validators=[django.core.validators.MaxValueValidator(200)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sampleparameters',
            name='dissolved_o',
            field=models.FloatField(null=True, verbose_name=b'Dissolved Oxygen', validators=[django.core.validators.MaxValueValidator(200)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sampleparameters',
            name='nh',
            field=models.FloatField(null=True, verbose_name=b'Ammonium', validators=[django.core.validators.MaxValueValidator(200)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sampleparameters',
            name='no',
            field=models.FloatField(null=True, verbose_name=b'Nitrates', validators=[django.core.validators.MaxValueValidator(200)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sampleparameters',
            name='ph',
            field=models.FloatField(null=True, validators=[django.core.validators.MaxValueValidator(200)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sampleparameters',
            name='pheo',
            field=models.FloatField(null=True, verbose_name=b'Pheophytin', validators=[django.core.validators.MaxValueValidator(200)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sampleparameters',
            name='po',
            field=models.FloatField(null=True, verbose_name=b'Ortho-Phosphates', validators=[django.core.validators.MaxValueValidator(200)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sampleparameters',
            name='salinity',
            field=models.FloatField(null=True, verbose_name=b'Salinity', validators=[django.core.validators.MaxValueValidator(200)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sampleparameters',
            name='si',
            field=models.FloatField(null=True, verbose_name=b'Silicates', validators=[django.core.validators.MaxValueValidator(200)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sampleparameters',
            name='temp',
            field=models.FloatField(null=True, verbose_name=b'Temperature', validators=[django.core.validators.MaxValueValidator(40)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sampleparameters',
            name='tn',
            field=models.FloatField(null=True, verbose_name=b'Total Nitrogen)', validators=[django.core.validators.MaxValueValidator(200)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sampleparameters',
            name='tp',
            field=models.FloatField(null=True, verbose_name=b'Total Phosphates', validators=[django.core.validators.MaxValueValidator(200)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sampleparameters',
            name='turb',
            field=models.FloatField(null=True, verbose_name=b'Turbidity', validators=[django.core.validators.MaxValueValidator(200)]),
            preserve_default=True,
        ),
    ]
