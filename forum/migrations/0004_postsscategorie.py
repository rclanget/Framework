# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20150702_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostSsCategorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('postcategorie', models.ForeignKey(to='forum.PostCategorie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
