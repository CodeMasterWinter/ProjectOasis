from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
# Create your views here.

def home(request):

    context = {
        'page_title': 'Home',
        'branches': ['Daveyton - Main', 'Carletonville',
                     'Etwatwa', 'Katlehong', 'Tembisa',
                     'Wattville', 'Braamfischerville',
                     'Umlazi', 'Vosloorus']
    }

    return render(request, 'oasis/home.html', context)


def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_first = request.POST['first_name']
            sender_last = request.POST['last_name']
            sender_email = request.POST['email']
            subject = request.POST['subject']
            sender_message = request.POST['message']

            try:
                send_mail(
                    f'{subject} inquiry by {sender_first} {sender_last}',
                    sender_message,
                    sender_email,
                    ['rhulanimogotsi@gmail.com']
                )

                messages.success(request, 'Message sent! Expect to hear from us soon!')
                return redirect('home')
            except BadHeaderError:
                return HttpResponse('Invalid Header')
    else:
        form = ContactForm()

    context = {
        'ContactForm': form,
        'branches': ['Daveyton - Main', 'Carletonville',
                     'Etwatwa', 'Katlehong', 'Tembisa',
                     'Wattville', 'Braamfischerville',
                     'Umlazi', 'Vosloorus'],
    }

    return render(request, 'oasis/contact.html', context)
