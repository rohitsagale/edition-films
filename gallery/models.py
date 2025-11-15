from django.db import models
from django.core.validators import RegexValidator

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    description = models.TextField(blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Video(models.Model):
    VIDEO_TYPES = [
        ('wedding', 'Wedding Video'),
        ('birthday', 'Birthday Video'),
        ('event', 'Event Video'),
    ]
    
    title = models.CharField(max_length=200)
    video_type = models.CharField(max_length=20, choices=VIDEO_TYPES)
    video_url = models.URLField(help_text="YouTube or Vimeo URL")
    thumbnail = models.ImageField(upload_to='video_thumbnails/', blank=True)
    description = models.TextField(blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('wedding', 'Wedding Photography'),
        ('birthday', 'Birthday Photography'),
        ('portrait', 'Portrait Session'),
        ('event', 'Event Photography'),
        ('video', 'Video Shooting'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(validators=[phone_regex], max_length=17)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    event_date = models.DateField()
    event_location = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.service_type}"