# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20141014_0325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('col_id', models.AutoField(serialize=False, primary_key=True)),
                ('collection', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='collection',
            field=models.ForeignKey(to='portfolio.Collections'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='post_desc',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
