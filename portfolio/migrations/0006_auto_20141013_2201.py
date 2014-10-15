# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20141013_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='post_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='music',
            name='post_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
