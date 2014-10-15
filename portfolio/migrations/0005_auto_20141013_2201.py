# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20141013_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='post_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='music',
            name='post_date',
            field=models.DateTimeField(),
        ),
    ]
