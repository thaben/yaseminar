# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(max_length=200)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('read', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(related_name='users_notification_list', to='seminar.Seminar', null=True)),
                ('sender', models.ForeignKey(to='seminar.Seminar')),
            ],
        ),
    ]
