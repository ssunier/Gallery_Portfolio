# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20141014_0343'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Collections',
            new_name='Collection',
        ),
    ]
