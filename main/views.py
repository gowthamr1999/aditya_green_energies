# Django views.py example for the solar website

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    """Main homepage view"""
    
    # Sample data for services (you can move this to models)
    services = [
        {
            'icon': 'home',
            'title': 'Residential Solar',
            'description': 'Complete solar solutions for your home. From consultation to installation and maintenance, we handle everything.',
            'features': ['Custom system design', 'Professional installation', '30-year warranty', 'Monitoring system']
        },
        {
            'icon': 'building-2',
            'title': 'Commercial Solar',
            'description': 'Scale your business with commercial solar installations. Reduce operational costs and enhance your sustainability profile.',
            'features': ['Large-scale systems', 'Tax incentives', 'Energy storage', 'Fleet electrification']
        },
        {
            'icon': 'wrench',
            'title': 'Maintenance & Repair',
            'description': 'Keep your solar system running at peak performance with our comprehensive maintenance and repair services.',
            'features': ['Regular inspections', 'Performance optimization', 'Component replacement', 'Emergency repairs']
        },
        {
            'icon': 'bar-chart-3',
            'title': 'Energy Consulting',
            'description': 'Expert analysis and recommendations to maximize your energy efficiency and solar investment returns.',
            'features': ['Energy audits', 'ROI analysis', 'System optimization', 'Financing options']
        }
    ]
    
    # Sample data for benefits
    benefits = [
        {
            'icon': 'dollar-sign',
            'title': 'Reduce Energy Bills',
            'description': 'Cut your electricity costs by up to 90% with solar energy. Many customers see complete elimination of their electric bills.'
        },
        {
            'icon': 'leaf',
            'title': 'Environmental Impact',
            'description': 'Reduce your carbon footprint and contribute to a cleaner planet. Solar energy produces zero emissions during operation.'
        },
        {
            'icon': 'trending-up',
            'title': 'Increase Property Value',
            'description': 'Solar installations can increase your home value by 3-4% on average, providing excellent return on investment.'
        },
        {
            'icon': 'zap',
            'title': 'Energy Independence',
            'description': 'Generate your own clean energy and reduce dependence on the grid. Battery storage options available for 24/7 power.'
        },
        {
            'icon': 'shield',
            'title': 'Long-term Reliability',
            'description': 'Solar panels are built to last 30+ years with minimal maintenance. Most systems pay for themselves within 6-8 years.'
        },
        {
            'icon': 'home',
            'title': 'Low Maintenance',
            'description': 'Solar systems require minimal upkeep. Rain naturally cleans panels, and our monitoring ensures optimal performance.'
        }
    ]
    
    context = {
        'services': services,
        'benefits': benefits,
        'hero_image': '/static/images/solar-hero.jpg',  # Add your hero image to static files
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