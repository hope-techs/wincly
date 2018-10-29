from django.contrib import admin
from app.models import Hotel



@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info', {'fields': ['name', 'user', 'image', 'content', 'summary']}),
        ('Date & Time', {'fields': ['publish', 'draft', 'created', 'updated']}),
        ('Meta', {'fields': ['tags', 'slug']})
    ]
    readonly_fields = ('updated', 'created', 'slug')
    # Display
    list_display = ('name', 'updated', 'publish', 'was_published_recently')

    # Filter
    list_filter = ['updated', 'tags']

    # Search
    search_fields = ['updated', 'name', 'content', 'summary', 'tags']




