# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_auto_20141014_0428'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Collection',
            new_name='Collections',
        ),
    ]
