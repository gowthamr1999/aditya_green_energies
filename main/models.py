# Django models.py for the solar website

from django.db import models
from django.utils import timezone

class ContactInquiry(models.Model):
    """Model to store contact form submissions"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    electric_bill = models.CharField(max_length=20, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('quoted', 'Quoted'),
        ('closed', 'Closed'),
    ], default='new')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Inquiry'
        verbose_name_plural = 'Contact Inquiries'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

class Service(models.Model):
    """Model for solar services"""
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=50)  # Lucide icon name
    description = models.TextField()
    features = models.JSONField(default=list)  # List of features
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class Benefit(models.Model):
    """Model for solar benefits"""
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=50)  # Lucide icon name
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class Testimonial(models.Model):
    """Customer testimonials"""
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    testimonial = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.rating} stars"