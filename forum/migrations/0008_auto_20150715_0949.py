# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20150715_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='sscategorie',
            field=models.ForeignKey(to='forum.PostSsCategorie', null=True),
        ),
    ]
