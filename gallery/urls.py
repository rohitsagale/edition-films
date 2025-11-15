from django.urls import path
from . import views
from . import admin_views

urlpatterns = [
    # Public URLs
    path('', views.home, name='home'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('videos/', views.videos_view, name='videos'),
    path('booking/', views.booking_view, name='booking'),
    path('booking/success/', views.booking_success, name='booking_success'),
    path('contact/', views.contact_view, name='contact'),
    
    # Custom Admin URLs - This will take over /admin/ completely
    path('admin/', admin_views.admin_login, name='admin_login'),
    path('admin/dashboard/', admin_views.admin_dashboard, name='admin_dashboard'),
    path('admin/logout/', admin_views.admin_logout, name='admin_logout'),
    path('admin/photos/', admin_views.admin_photos, name='admin_photos'),
    path('admin/photos/add/', admin_views.admin_add_photo, name='admin_add_photo'),
    path('admin/photos/edit/<int:photo_id>/', admin_views.admin_edit_photo, name='admin_edit_photo'),
    path('admin/photos/delete/<int:photo_id>/', admin_views.admin_delete_photo, name='admin_delete_photo'),
    path('admin/videos/', admin_views.admin_videos, name='admin_videos'),
    path('admin/videos/add/', admin_views.admin_add_video, name='admin_add_video'),
    path('admin/videos/edit/<int:video_id>/', admin_views.admin_edit_video, name='admin_edit_video'),
    path('admin/videos/delete/<int:video_id>/', admin_views.admin_delete_video, name='admin_delete_video'),
    path('admin/bookings/', admin_views.admin_bookings, name='admin_bookings'),
    path('admin/bookings/update/<int:booking_id>/', admin_views.admin_update_booking, name='admin_update_booking'),
    path('admin/bookings/delete/<int:booking_id>/', admin_views.admin_delete_booking, name='admin_delete_booking'),
    path('admin/categories/', admin_views.admin_categories, name='admin_categories'),
    path('admin/categories/add/', admin_views.admin_add_category, name='admin_add_category'),
    path('admin/categories/edit/<int:category_id>/', admin_views.admin_edit_category, name='admin_edit_category'),
    path('admin/categories/delete/<int:category_id>/', admin_views.admin_delete_category, name='admin_delete_category'),
]