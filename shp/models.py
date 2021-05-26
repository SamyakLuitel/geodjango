# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models 




class ShpNepal(models.Model):
    object_id = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    descriptio = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=1, blank=True, null=True)
    objectid = models.IntegerField(blank=True, null=True)
    dist_code = models.IntegerField(blank=True, null=True)
    dist_name = models.CharField(max_length=14, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    shape_len = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    cartodb_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    updated_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shp_Nepal'

    def __str__(self):
        return self.dist_name


