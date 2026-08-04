from django.db import models
from django.contrib.auth.models import User

class LoginLog(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logins')
    data_hora = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-data_hora']  # mais recente primeiro
        verbose_name = "Login registrado"
        verbose_name_plural = "Logins registrados"

    def __str__(self):
        return f"{self.usuario.username} - {self.data_hora.strftime('%d/%m/%Y %H:%M')}"
# Create your models here.
