from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Photo, Video, Category, Booking
from .forms import BookingForm

def home(request):
    featured_photos = Photo.objects.filter(is_featured=True)[:6]
    wedding_videos = Video.objects.filter(video_type='wedding')[:3]
    return render(request, 'gallery/index.html', {
        'featured_photos': featured_photos,
        'wedding_videos': wedding_videos
    })

def gallery_view(request):
    category_id = request.GET.get('category')
    photos = Photo.objects.all()
    
    if category_id:
        photos = photos.filter(category_id=category_id)
    
    categories = Category.objects.all()
    
    # Pagination
    paginator = Paginator(photos, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'gallery/gallery.html', {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category_id
    })

def videos_view(request):
    video_type = request.GET.get('type', 'wedding')
    videos = Video.objects.filter(video_type=video_type)
    return render(request, 'gallery/videos.html', {
        'videos': videos,
        'selected_type': video_type
    })

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking request has been submitted successfully! We will contact you soon.')
            return redirect('booking_success')
    else:
        form = BookingForm()
    
    return render(request, 'gallery/booking.html', {'form': form})

def booking_success(request):
    return render(request, 'gallery/booking_success.html')

def contact_view(request):
    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Here you would typically send an email or save to database
        messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
        return redirect('contact')
    
    return render(request, 'gallery/contact.html')