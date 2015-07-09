# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'Date de creation')),
                ('auteur', models.CharField(max_length=100)),
                ('closeby', models.CharField(max_length=100)),
                ('attributedto', models.CharField(max_length=100, null=True)),
                ('status', models.BooleanField(default=True)),
                ('categorie', models.ForeignKey(to='ticket.categorie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
