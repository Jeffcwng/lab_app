# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('continent', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('hotel', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75)),
                ('username', models.CharField(max_length=30)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('listname', models.CharField(max_length=30)),
                ('user', models.ForeignKey(related_name=b'userlists', to='wanderful.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='location',
            name='userlist',
            field=models.ManyToManyField(related_name=b'locations', to='wanderful.UserList'),
            preserve_default=True,
        ),
    ]
