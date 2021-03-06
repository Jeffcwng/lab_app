# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wanderful', '0002_auto_20140919_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.ImageField(null=True, upload_to=b'location_images', blank=True),
            preserve_default=True,
        ),
    ]
