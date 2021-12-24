from django.contrib import admin
from django.db.models.aggregates import Count

from db.models import City, District, Person,States,Country

# Register your models here.
admin.site.register(Country)
admin.site.register(States)
admin.site.register(District)
admin.site.register(City)
admin.site.register(Person)
# admin.site.register(States)
# admin.site.register(District)



