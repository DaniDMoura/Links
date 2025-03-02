from django.core.mail import send_mail
from django.conf import settings
from textwrap import dedent

def send_email(to_email, subject, message, nome, user_email):
    email_body = dedent(f"""
        Nome: {nome}
        Email: {user_email}
        Mensagem: {message}
    """)

    send_mail(
        subject=subject,
        message=email_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[to_email],
        fail_silently=False,
    )
