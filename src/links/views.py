from django.shortcuts import render

def links(request):
  return render(request,'links.html')

def contact(request):
  return render(request,'contact.html')