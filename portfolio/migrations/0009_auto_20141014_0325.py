# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20141014_0315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('art_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('collection', models.CharField(default=b'Sketch Book', max_length=200)),
                ('link', models.URLField(max_length=255)),
                ('post_desc', models.CharField(max_length=500)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Art',
        ),
    ]
