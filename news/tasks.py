from celery import shared_task
from django.core.mail import send_mail


@shared_task
send_mail(
    'Новые новости на портале'
    'news/'
    'EMAIL_HOST_USER'
    ['subscribers'],
    fail_silently=False
)
