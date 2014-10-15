# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20141014_0313'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gallary',
            new_name='Art',
        ),
    ]
