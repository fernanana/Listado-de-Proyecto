from django.contrib import admin
from principal.models import Comuna
from django.contrib import admin

class ComunaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
admin.site.register(Comuna, ComunaAdmin)