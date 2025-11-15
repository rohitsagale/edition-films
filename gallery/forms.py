from django import forms
from .models import Booking, Photo, Video, Category

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'service_type', 'event_date', 'event_location', 'message']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'category', 'image', 'description', 'is_featured']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_type', 'video_url', 'thumbnail', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }