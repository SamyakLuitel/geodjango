from django.contrib import admin
from .models import ShpNepal
from leaflet.admin import LeafletGeoAdmin

# Register your models here.


admin.site.register(ShpNepal,LeafletGeoAdmin)
