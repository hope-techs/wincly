from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from wincly.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
                    ("Additional info", {"fields": ('phone', 'birth_date',)}),
                    ('User',{"fields": (),}),
                ) + auth_admin.UserAdmin.fieldsets

    list_display = ("username", 'email', 'date_joined', "is_superuser")
    search_fields = ('phone',) + auth_admin.UserAdmin.search_fields
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('date_joined', 'username')

