from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def seven(request):
    return render(request, 'seven.html', {})



def meetings(request):
    return render(request, 'meetings.html', {})

def meetingdetails(request):
    return render(request, 'meeting-details.html', {})




def about(request):
    return render(request, 'about.html', {})

def car(request):
    return render(request, 'car.html', {})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']  # Koristi email adresu posetioca kao pošiljaoca
        number = request.POST['number']
        message = request.POST['message']
        
        # Slanje maila
        send_mail(
            subject='Kontakt - AutoSeven | Poruka',
            message=f'Ime i prezime: {name}\n\nEmail: {email}\n\nBroj telefona: {number}\n\nPoruka: {message}',
            from_email=email,
            recipient_list=[settings.EMAIL_HOST_USER],
        )
        
        return render(request, 'message.html', {'name': name})
    else:
        return render(request, 'contact.html', {})

def detail(request):
    return render(request, 'detail.html', {})

def service(request):
    return render(request, 'service.html', {})


def contact2(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']  # Koristi email adresu posetioca kao pošiljaoca
        instagram = request.POST['instagram']
        message = request.POST['message']
        
        # Slanje maila
        send_mail(
            subject='Kontakt - ClubSeven | Poruka',
            message=f'Ime i prezime: {name}\n\nEmail: {email}\n\nInstagram: {instagram}\n\nPoruka: {message}',
            from_email=email,
            recipient_list=[settings.EMAIL_HOST_USER],
        )
        
        return render(request, 'message2.html', {'name': name})
    else:
        return render(request, 'index.html', {})

