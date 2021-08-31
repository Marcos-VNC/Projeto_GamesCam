from django.contrib import admin
from .models import Empresa, Game

class detGame(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'Genero', 'Plataforma', 'dataLançamento', 'Desenvolvedora', 'mostrar')
    list_editable = ('mostrar',)
    list_display_links = ('nome',)
    search_fields = ('nome',)

admin.site.register(Empresa)
admin.site.register(Game, detGame)






