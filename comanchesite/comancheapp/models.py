from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Lipid(models.Model):
    lmid = models.IntegerField(default=-1)
    common_name = models.CharField(max_length=200)
    systematic_name = models.CharField(max_length=200)
    formula = models.CharField(max_length=50)
    mass = models.FloatField()
    charge = models.IntegerField()
    category = models.ForeignKey("LipidCategory", on_delete=models.PROTECT)
    main_class = models.ForeignKey("LipidClass", on_delete=models.PROTECT)
    sub_class = models.ForeignKey("LipidSubclass", on_delete=models.PROTECT)
    synomyms = models.CharField(max_length=200)
    keggid = models.CharField(max_length=50)
    hmdbid = models.CharField(max_length=50)
    ymdbid = models.CharField(max_length=50)
    chebiid = models.CharField(max_length=50)
    metabolomicsid = models.CharField(max_length=50)
    pubchemcid = models.CharField(max_length=50)
    lipidbankid = models.CharField(max_length=50)
    lipidatid = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    refs = models.CharField(max_length=200)
    lipidmapsurl = models.URLField()

class LipidCategory(models.Model):
    name = models.CharField(max_length=200)

class LipidClass(models.Model):
    name = models.CharField(max_length=200)

class LipidSubClass(models.Model):
    name = models.CharField(max_length=200)

class Forcefield(models.Model):
    forcefield = models.CharField(max_length=50)
    lmid = models.CharField(max_length=50)
    common = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    reverse = models.BooleanField()
    status = models.CharField(max_length=50)
    refs = models.CharField(max_length=200)

class Membrane(models.Model):
    membrane = models.CharField(max_length=50)
    forcefield = models.ForeignKey("Forcefield")
    temperature = models.FloatField()
    nblipids = models.IntegerField()

class MembraneLipid(models.Model):
    UNKNOWN=0
    UPPER=1
    LOWER=2
    POSITION_CHOICES = (
        (UNKNOWN, "Unknown"),
        (UPPER, "Upper"),
        (LOWER, "Lower")
    )
    membrane = models.ForeignKey("Membrane")
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    position = models.IntegerField(choices=POSITION_CHOICES, default=UNKNOWN)
    nblipids = models.IntegerField()
