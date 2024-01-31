from .models import Notification


def notifications(request):
    if request.user.is_authenticated:
        notifications = request.user.notifications.filter(is_read=False)
        return {'notifications': notifications}
    return {'notifications': []}
