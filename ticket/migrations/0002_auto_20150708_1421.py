# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('auteur', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'Date de creation')),
                ('ticket', models.ForeignKey(to='ticket.Ticket')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='categorie',
            field=models.ForeignKey(to='ticket.Categorie'),
        ),
    ]
