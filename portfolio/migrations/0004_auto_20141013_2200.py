# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20141013_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 13, 22, 0, 42, 499109, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='music',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 13, 22, 0, 42, 501196, tzinfo=utc)),
        ),
    ]
