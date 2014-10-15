# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_music'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='post_desc',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
