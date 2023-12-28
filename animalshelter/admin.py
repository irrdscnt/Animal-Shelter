from django.contrib import admin
from . import models

admin.site.register(models.Animal)
admin.site.register(models.News)
admin.site.register(models.Review)
admin.site.register(models.AdoptionForm)

