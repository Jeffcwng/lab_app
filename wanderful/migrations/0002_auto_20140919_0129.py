# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wanderful', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='traveler',
            field=models.ManyToManyField(related_name=b'locations', to='wanderful.Traveler'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='traveler',
            name='gender',
            field=models.CharField(max_length=6),
        ),
    ]
