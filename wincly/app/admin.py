from django.contrib import admin
from app.models import Hotel, HotelImage

class ImageInline(admin.TabularInline):
    model = HotelImage

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info', {'fields': ['name', 'user', 'image', 'content', 'summary']}),
        ('Location', {'fields': ['country', 'city']}),
        ('Date & Time', {'fields': ['publish', 'draft', 'created', 'updated']}),
        ('Meta', {'fields': ['tags', 'slug', 'website', 'booked']})
    ]
    inlines = [ImageInline]
    readonly_fields = ('updated', 'created', 'slug', 'user')
    # Display
    list_display = ('name', 'updated', 'publish', 'was_published_recently')

    # Filter
    list_filter = ['updated', 'tags']

    # Search
    search_fields = ['updated', 'name', 'content', 'summary', 'tags']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
