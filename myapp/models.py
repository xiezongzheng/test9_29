# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Bactname(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    num = models.TextField(db_column='NUM', blank=True)  # Field name made lowercase.
    genus = models.CharField(db_column='GENUS', max_length=50, blank=True)  # Field name made lowercase.
    species = models.CharField(db_column='SPECIES', max_length=50, blank=True)  # Field name made lowercase.
    subspecies = models.CharField(db_column='SUBSPECIES', max_length=50, blank=True)  # Field name made lowercase.
    reference = models.CharField(db_column='REFERENCE', max_length=50, blank=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=50, blank=True)  # Field name made lowercase.
    authors = models.CharField(db_column='AUTHORS', max_length=50, blank=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='REMARKS', max_length=50, blank=True)  # Field name made lowercase.
    risk_grp = models.CharField(db_column='RISK_GRP', max_length=50, blank=True)  # Field name made lowercase.
    type_strains = models.CharField(db_column='TYPE_STRAINS', max_length=50, blank=True)  # Field name made lowercase.
    taxonid = models.CharField(db_column='taxonId', max_length=50, blank=True)  # Field name made lowercase.
    ncbitaxonid = models.CharField(db_column='ncbiTaxonId', max_length=50, blank=True)  # Field name made lowercase.
    mclid = models.CharField(db_column='mclId', max_length=50, blank=True)  # Field name made lowercase.
    sequence = models.TextField(db_column='SEQUENCE', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bactname'


class TaxonMapping(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    speciesname = models.CharField(db_column='speciesName', max_length=100, blank=True)  # Field name made lowercase.
    taxonid = models.CharField(db_column='taxonId', max_length=50, blank=True)  # Field name made lowercase.
    ncbitaxonid = models.CharField(db_column='ncbiTaxonId', max_length=50, blank=True)  # Field name made lowercase.
    mclid = models.CharField(db_column='mclId', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taxon_mapping'


class User(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    username = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'user'
