from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, DateField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # OverWrite base email field
    email = EmailField(_('Email Address'), unique=True)
    
    phone = CharField(_('Phone Number'), blank=True, null=True, max_length=255)
    birth_date = DateField(_('Birth Date'), blank=True, null=True)


    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['-date_joined']


    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
