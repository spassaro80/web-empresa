from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contactform=ContactForm()
    if request.method == "POST":
        contactform=ContactForm(data=request.POST) 
        if contactform.is_valid:
            name = request.POST.get('name','')
            email = request.POST.get('email', '')
            content = request.POST.get('content','')
            
            #Send e-mail

            email=EmailMessage(
                "Nuevo mensaje de la Caffetiera",
                "{} ha enviado un nuevo mensaje \n \n  {}".format(name, content),
                "nocontestar@inbox.mailtrap.io",
                ["stefano.passaro@gmail.com"],
                reply_to=[email]

            )
            try:
                email.send()
                return redirect(reverse('contact') + "?ok")
            except:
                return redirect(reverse('contact') + "?FAIL")

            
            return redirect(reverse('contact') + "?ok")
    return render(request, "contact/contact.html", {'form':contactform})
