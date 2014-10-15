# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_auto_20141014_0501'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Collections',
            new_name='Collection',
        ),
        migrations.RenameField(
            model_name='collection',
            old_name='col_id',
            new_name='collection_id',
        ),
        migrations.RenameField(
            model_name='gallery',
            old_name='collections',
            new_name='collection',
        ),
        migrations.AlterField(
            model_name='gallery',
            name='collection',
            field=models.ForeignKey(to='portfolio.Collection'),
        ),
    ]
