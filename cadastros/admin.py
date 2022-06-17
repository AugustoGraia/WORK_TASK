from django.contrib import admin

# Importar as classes

# admin.py: Arquivo responsável por definir os models a serem utilizados no módulo administrativo do Django.
from .models import Atividade, Campo

admin.site.register(Campo)
admin.site.register(Atividade)


