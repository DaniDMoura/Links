from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "assunto", "data_msg")
    search_fields = ("nome", "email", "assunto")
    list_filter = ("data_msg",)