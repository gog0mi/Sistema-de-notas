from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Admins)
admin.site.register(models.Profesores)
admin.site.register(models.Secciones)
admin.site.register(models.Cursos)
admin.site.register(models.Estudiantes)
admin.site.register(models.Notas)