# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_postsscategorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorie',
            field=models.ForeignKey(to='forum.PostSsCategorie'),
        ),
    ]
