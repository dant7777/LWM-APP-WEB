from django.contrib import admin
from .models import Continent, Zone, Country, District, Assembly

admin.site.register(Continent)
admin.site.register(Zone)
admin.site.register(Country)
admin.site.register(District)
admin.site.register(Assembly)
