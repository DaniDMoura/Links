
from django.shortcuts import render,redirect
from .models import Message
from .email_service import send_email
from django.contrib import messages

def links(request):
  return render(request,'links.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('nome').strip()
        email = request.POST.get('email').strip()
        subject = request.POST.get('subject').strip()
        message = request.POST.get('message').strip()

        if not name or not email or not subject or not message:
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect("contact")

        send_message = Message.objects.create(
            nome=name, email=email, assunto=subject, mensagem=message
        )
        send_message.save()

        try:
            send_email(to_email='mouradanilo061@gmail.com',subject=subject, message=message, nome=name, user_email=email)
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")
            return redirect("contact")

        print("Mensagem enviada com sucesso!")
        return redirect('/')
    return render(request,'contact.html')