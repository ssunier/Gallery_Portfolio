# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('music_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('album', models.CharField(max_length=200)),
                ('post_type', models.CharField(default=b'S', max_length=1, choices=[(b'S', b'Song'), (b'V', b'Video')])),
                ('link', models.URLField(max_length=255)),
                ('post_desc', models.CharField(max_length=500)),
                ('post_date', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
