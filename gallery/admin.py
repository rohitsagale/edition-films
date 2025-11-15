from django.contrib import admin
from .models import Category, Photo, Video, Booking

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'upload_date', 'is_featured']
    list_filter = ['category', 'is_featured', 'upload_date']
    search_fields = ['title', 'description']
    list_editable = ['is_featured']

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_type', 'upload_date']
    list_filter = ['video_type', 'upload_date']
    search_fields = ['title', 'description']

class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'service_type', 'event_date', 'is_confirmed', 'created_at']
    list_filter = ['service_type', 'is_confirmed', 'event_date', 'created_at']
    search_fields = ['name', 'email', 'event_location']
    list_editable = ['is_confirmed']
    readonly_fields = ['created_at']

admin.site.register(Category)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Booking, BookingAdmin)