from django.shortcuts import render
from .models import LogEntry

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):
    ip = get_client_ip(request)
    user_id = request.user.id if request.user.is_authenticated else None

    LogEntry.objects.create(ip_address=ip, user_id=user_id)

    return render(request, 'home.html')


def log_list(request):
    logs = LogEntry.objects.order_by('-timestamp')[:100]
    return render(request, 'log_list.html', {'logs': logs})