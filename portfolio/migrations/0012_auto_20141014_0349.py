# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20141014_0346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='collection',
            new_name='collections_id',
        ),
    ]
