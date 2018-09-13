# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0007_category_seminarcounter'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='categoryimage',
            field=models.ImageField(default=b'avatarlogo.jpg', upload_to=b''),
        ),
    ]
