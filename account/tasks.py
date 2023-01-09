from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_activasion_code(email, activation_code):
    activation_link = f'http://localhost:8000/account/activate/{activation_code}'
    message = f'Activate your account b*tch\n{activation_link}'
    send_mail('Activate account', message, 'aupmaan@gmail.com', [email])
    return 'Sent'