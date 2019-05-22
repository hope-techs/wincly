from django.contrib import admin
from app.models import Hotel, HotelImage, Contact
from app.forms import ContactForm


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




@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    form = ContactForm
    fieldsets = [
        ('Information', {'fields': ['subject', 'first_name', 'last_name', 'email', 'phone', 'content']}),
        ('Admin', {'fields': ['checked',]})
    ]
    readonly_fields = ('updated',)
    # Display
    list_display = ('subject', 'email', 'updated', 'checked')

    # Filter
    list_filter = ['email', 'updated']

    # Search
    search_fields = ['subject', 'first_name', 'last_name', 'email', 'phone', 'content', 'updated']
