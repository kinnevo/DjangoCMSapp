# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='activity',
            name='image',
            field=models.URLField(default=''),
        ),
    ]
