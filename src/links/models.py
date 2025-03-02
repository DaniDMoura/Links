from django.db import models


class Message(models.Model):
  nome = models.CharField(max_length=255)
  email = models.EmailField()
  assunto = models.CharField(max_length=50)
  mensagem = models.TextField()
  data_msg = models.DateTimeField(auto_now_add=True)

