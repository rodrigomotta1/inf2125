from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Local
from django.contrib import admin
from core.models import Usuario, Local, Informacao, Aviso, Previsao


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'latitude', 'longitude')
    search_fields = ('nome',)
    list_filter = ('avisos',)

admin.site.register(Aviso)
admin.site.register(Previsao)
admin.site.register(Informacao)