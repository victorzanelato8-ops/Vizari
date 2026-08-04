from django.contrib import admin
from .models import LoginLog

@admin.register(LoginLog)
class LoginLogAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'data_hora', 'ip']
    list_filter = ['usuario', 'data_hora']
    readonly_fields = ['usuario', 'data_hora', 'ip']  # ninguém edita, só visualiza

    def has_add_permission(self, request):
        return False  # ninguém cria manualmente, só via login real