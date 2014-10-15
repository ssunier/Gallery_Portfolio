# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_auto_20141014_0349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='collections_id',
            new_name='collections',
        ),
    ]
