from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Photo, Video, Booking, Category
from .forms import BookingForm, PhotoForm, VideoForm, CategoryForm

def admin_login(request):
    # If user is already authenticated and is staff, redirect to dashboard
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_staff:
                login(request, user)
                messages.success(request, 'Welcome to Admin Panel!')
                return redirect('admin_dashboard')
            else:
                messages.error(request, 'Access denied. Only staff members can access admin panel.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'gallery/admin/login.html')

@login_required
def admin_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('admin_login')

@login_required
def admin_dashboard(request):
    # Check if user is staff
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('admin_login')
    
    # Get statistics
    total_photos = Photo.objects.count()
    total_videos = Video.objects.count()
    total_bookings = Booking.objects.count()
    pending_bookings = Booking.objects.filter(is_confirmed=False).count()
    total_categories = Category.objects.count()
    
    # Recent bookings
    recent_bookings = Booking.objects.all().order_by('-created_at')[:5]
    
    context = {
        'total_photos': total_photos,
        'total_videos': total_videos,
        'total_bookings': total_bookings,
        'pending_bookings': pending_bookings,
        'total_categories': total_categories,
        'recent_bookings': recent_bookings,
    }
    return render(request, 'gallery/admin/dashboard.html', context)

# Add staff check to all admin views
def staff_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            messages.error(request, 'Access denied. Please login as staff.')
            return redirect('admin_login')
        return view_func(request, *args, **kwargs)
    return wrapper

# Apply staff_required decorator to all admin views
@login_required
@staff_required
def admin_photos(request):
    photos = Photo.objects.all().order_by('-upload_date')
    categories = Category.objects.all()
    return render(request, 'gallery/admin/photos.html', {
        'photos': photos,
        'categories': categories
    })

@login_required
@staff_required
def admin_add_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Photo added successfully!')
            return redirect('admin_photos')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PhotoForm()
    
    return render(request, 'gallery/admin/photo_form.html', {
        'form': form,
        'title': 'Add Photo'
    })

@login_required
@staff_required
def admin_edit_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Photo updated successfully!')
            return redirect('admin_photos')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PhotoForm(instance=photo)
    
    return render(request, 'gallery/admin/photo_form.html', {
        'form': form,
        'title': 'Edit Photo',
        'photo': photo
    })

@login_required
@staff_required
def admin_delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if request.method == 'POST':
        photo.delete()
        messages.success(request, 'Photo deleted successfully!')
        return redirect('admin_photos')
    
    return JsonResponse({'success': False})

@login_required
@staff_required
def admin_videos(request):
    videos = Video.objects.all().order_by('-upload_date')
    return render(request, 'gallery/admin/videos.html', {'videos': videos})

@login_required
@staff_required
def admin_add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video added successfully!')
            return redirect('admin_videos')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = VideoForm()
    
    return render(request, 'gallery/admin/video_form.html', {
        'form': form,
        'title': 'Add Video'
    })

@login_required
@staff_required
def admin_edit_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video updated successfully!')
            return redirect('admin_videos')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = VideoForm(instance=video)
    
    return render(request, 'gallery/admin/video_form.html', {
        'form': form,
        'title': 'Edit Video',
        'video': video
    })

@login_required
@staff_required
def admin_delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        video.delete()
        messages.success(request, 'Video deleted successfully!')
        return redirect('admin_videos')
    
    return JsonResponse({'success': False})

@login_required
@staff_required
def admin_bookings(request):
    bookings = Booking.objects.all().order_by('-created_at')
    return render(request, 'gallery/admin/bookings.html', {'bookings': bookings})

@login_required
@staff_required
def admin_update_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.method == 'POST':
        is_confirmed = request.POST.get('is_confirmed') == 'true'
        booking.is_confirmed = is_confirmed
        booking.save()
        messages.success(request, 'Booking updated successfully!')
        return redirect('admin_bookings')
    
    return JsonResponse({'success': False})

@login_required
@staff_required
def admin_delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking deleted successfully!')
        return redirect('admin_bookings')
    
    return JsonResponse({'success': False})

@login_required
@staff_required
def admin_categories(request):
    categories = Category.objects.all()
    return render(request, 'gallery/admin/categories.html', {'categories': categories})

@login_required
@staff_required
def admin_add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('admin_categories')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CategoryForm()
    
    return render(request, 'gallery/admin/category_form.html', {
        'form': form,
        'title': 'Add Category'
    })

@login_required
@staff_required
def admin_edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('admin_categories')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'gallery/admin/category_form.html', {
        'form': form,
        'title': 'Edit Category',
        'category': category
    })

@login_required
@staff_required
def admin_delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        # Check if category has photos
        if category.photo_set.exists():
            messages.error(request, 'Cannot delete category that has photos. Please reassign photos first.')
        else:
            category.delete()
            messages.success(request, 'Category deleted successfully!')
        return redirect('admin_categories')
    
    return JsonResponse({'success': False})