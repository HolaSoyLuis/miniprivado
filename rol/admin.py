from django.contrib import admin
from .models import afiliado, empleado, registro
# Register your models here.
admin.site.register(afiliado)
admin.site.register(empleado)
admin.site.register(registro)