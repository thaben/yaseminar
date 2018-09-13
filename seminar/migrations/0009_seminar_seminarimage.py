# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0008_category_categoryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar',
            name='seminarimage',
            field=models.ImageField(default=b'avatarlogo.jpg', upload_to=b''),
        ),
    ]
