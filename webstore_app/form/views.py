from django.shortcuts import render
from django.http import HttpResponse
from form.form import RegisterForm
from django.core.mail import EmailMessage

def index(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        asunto = "Este es  un mensaje d eprueba"
        mensaje = "Gracias cupon"
        mail = EmailMessage(asunto,mensaje,to =["danielbarroso1989@gmail.com"])
        mail.send()
    return render(request,"form/index.html",{"form":form})

# Create your views here.
