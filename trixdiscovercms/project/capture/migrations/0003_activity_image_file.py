# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capture', '0002_auto_20160808_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='image_file',
            field=models.FileField(default='', upload_to='uploads/'),
        ),
    ]
