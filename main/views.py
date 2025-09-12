# Django views.py example for the solar website

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Benefit, About, ContactInfo

def index(request):
    services = Service.objects.all()
    benefits = Benefit.objects.all()
    about = About.objects.first()
    contact = ContactInfo.objects.first()
    context = {
        "about": about,
        'services': services,
        'benefits': benefits,
        "contact": contact,
        'hero_image': '/static/images/solar-hero.jpg',
    }
    return render(request, 'index.html', context)

def contact_form(request):
    """Handle contact form submissions"""
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone_number')
        address = request.POST.get('address')
        message = request.POST.get('message')
        
        # Save to database (create a ContactInquiry model)
        # ContactInquiry.objects.create(
        #     first_name=first_name,
        #     last_name=last_name,
        #     email=email,
        #     phone=phone,
        #     address=address,
        #     electric_bill=electric_bill,
        #     message=message
        # )
        
        # Send email notification
        subject = f'New Solar Quote Request from {name}'
        email_message = f"""
        New solar quote request received:
        
        Name: {name}
        Email: {email}
        Phone: {phone}
        Address: {address}
        Message: {message}
        """
        
        try:
            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                ['adityagreenenergies@gmail.com'],  # Replace with your email
                fail_silently=False,
            )
            messages.success(request, 'Thank you for your interest! We\'ll contact you within 24 hours.')
            return redirect("contact")
        except:
            messages.error(request, 'There was an error sending your message. Please try again.')
        
        return redirect("contact")  # reload with success message
    
    return render(request, "contact.html")