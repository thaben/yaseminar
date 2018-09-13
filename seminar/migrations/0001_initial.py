# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Seminar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200, null=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(max_length=30)),
                ('users_max', models.PositiveIntegerField(null=True)),
                ('user_counter', models.IntegerField(default=0, null=True)),
                ('author', models.ForeignKey(to='userprofile.AffiliateUser')),
                ('category', models.ForeignKey(related_name='seminar_category', to='seminar.Category', null=True)),
                ('usersbooked', models.ManyToManyField(to='userprofile.SimpleUser', blank=True)),
            ],
        ),
    ]
