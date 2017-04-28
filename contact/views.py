from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings


from django.core.mail import send_mail, mail_admins

from .models import Contact

from .forms import ContactForm
# from .models import Kind


def index(request):


    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            fname = form.cleaned_data['fname']
            surname = form.cleaned_data['surname']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            recipients = settings.SECRETS.get('e_recipients')

            message = "name: %s %s\nphone: %s\nemail: %s\nmessage: %s" % (fname, surname, phone, email, content )
            send_mail('spin the wheel contact form', message, settings.SECRETS.get('email_from'), recipients)

            contact = Contact(
                fname = fname,
                surname = surname,
                phone = phone,
                email = email,
                content = content,
            )

            contact.save()

            return HttpResponseRedirect('/')
    else:
        form = ContactForm()


    data = {
        'active_tab': 'contact',
        'form': form
    }

    return render(request, 'contact/index.html', data)