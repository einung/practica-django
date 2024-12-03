from django.contrib import admin

from .models.prenda import Prenda
from .models.accesorios import Accesorio
# Register your models here.
admin.site.register(Prenda)
admin.site.register(Accesorio)
