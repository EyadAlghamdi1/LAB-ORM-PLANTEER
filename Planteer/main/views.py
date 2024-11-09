from django.shortcuts import render , redirect
from django.http import HttpRequest,HttpResponse
from .models import Contact
from plant.models import Plant

# Create your views here 
def home_view(request: HttpRequest):
    featured_plants = Plant.objects.all()[:3]
    return render(request, "main/home.html", {'featured_plants': featured_plants})

def contact_view(request: HttpRequest):
    if request.method == "POST":
        user_message = Contact(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            message=request.POST["message"],
        )
        user_message.save()
    return render(request, "main/contact.html")

def contact_message_view(request: HttpRequest):
    user_messages = Contact.objects.all()  
    return render(request, "main/contact_massege.html", {"user_messages": user_messages})
