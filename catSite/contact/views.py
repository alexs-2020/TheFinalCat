from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=f"Message: {message}\n\nFrom: {email}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['recipient_email@example.com'],  # Your email to receive messages
                fail_silently=False,
            )
            return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def contact_success(request):
    return render(request, 'contact_success.html')