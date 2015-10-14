# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bactname',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('num', models.TextField(db_column='NUM', blank=True)),
                ('genus', models.CharField(max_length=50, db_column='GENUS', blank=True)),
                ('species', models.CharField(max_length=50, db_column='SPECIES', blank=True)),
                ('subspecies', models.CharField(max_length=50, db_column='SUBSPECIES', blank=True)),
                ('reference', models.CharField(max_length=50, db_column='REFERENCE', blank=True)),
                ('status', models.CharField(max_length=50, db_column='STATUS', blank=True)),
                ('authors', models.CharField(max_length=50, db_column='AUTHORS', blank=True)),
                ('remarks', models.CharField(max_length=50, db_column='REMARKS', blank=True)),
                ('risk_grp', models.CharField(max_length=50, db_column='RISK_GRP', blank=True)),
                ('type_strains', models.CharField(max_length=50, db_column='TYPE_STRAINS', blank=True)),
                ('taxonid', models.CharField(max_length=50, db_column='taxonId', blank=True)),
                ('ncbitaxonid', models.CharField(max_length=50, db_column='ncbiTaxonId', blank=True)),
                ('mclid', models.CharField(max_length=50, db_column='mclId', blank=True)),
                ('sequence', models.TextField(db_column='SEQUENCE', blank=True)),
            ],
            options={
                'db_table': 'bactname',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaxonMapping',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('speciesname', models.CharField(max_length=100, db_column='speciesName', blank=True)),
                ('taxonid', models.CharField(max_length=50, db_column='taxonId', blank=True)),
                ('ncbitaxonid', models.CharField(max_length=50, db_column='ncbiTaxonId', blank=True)),
                ('mclid', models.CharField(max_length=50, db_column='mclId', blank=True)),
            ],
            options={
                'db_table': 'taxon_mapping',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=100, blank=True)),
                ('password', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
