# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20141013_2201'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Art',
            new_name='Gallary',
        ),
    ]
