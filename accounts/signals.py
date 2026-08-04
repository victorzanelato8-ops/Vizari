from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import LoginLog

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')

@receiver(user_logged_in)
def registrar_login(sender, request, user, **kwargs):
    LoginLog.objects.create(
        usuario=user,
        ip=get_client_ip(request)
    )