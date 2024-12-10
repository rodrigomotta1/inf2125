from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Local
from django.contrib import admin
from core.models import Usuario

# @admin.register(Usuario)
# class UsuarioAdmin(UserAdmin):
#     # Personalize, se necessário
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('locais_favoritos',)}),
#     )

# admin.site.register(Local)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user',)
