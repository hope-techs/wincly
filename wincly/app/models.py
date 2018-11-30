from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.utils import timezone
from django.urls import reverse
from app.utils.Unique_Slug_Generator import unique_slug_generator
from django.utils.translation import ugettext_lazy as _



User = settings.AUTH_USER_MODEL


# initial a directory for files of each user
def upload_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/year-month-day/UserName/FileName
    # return ('Uploads/{0}/{1}/{2}'.format(strftime('%Y-%m-%d'), self.author, filename))
    return ('{0}/{1}'.format(self.user, filename))


class Hotel(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = _('User'))
    name = models.CharField(max_length = 255, verbose_name = _('Name'))
    image = models.ImageField(blank = True, null = True, upload_to = upload_path, verbose_name = _('Image'))
    content = models.TextField(verbose_name = _('Content'))
    summary = models.CharField(max_length = 511, blank = True, null = True, verbose_name = _('Summary'))
    country = models.CharField(max_length = 255, verbose_name = _('Country'))
    city = models.CharField(max_length = 255, verbose_name = _('City'))
    # Date Time Information
    created = models.DateTimeField(auto_now_add = True, auto_now = False, verbose_name = _('Created'))
    updated = models.DateTimeField(auto_now_add = False, auto_now = True, verbose_name = _('Updated'))
    draft = models.BooleanField(default = False, verbose_name = _('Draft'))
    publish = models.DateTimeField(blank = True, null = True, verbose_name = _('Publish'))
    # Utils
    slug = models.SlugField(allow_unicode = True, unique = True, verbose_name = _('Slug'))
    tags = TaggableManager(blank = True, verbose_name = _('Tags'))


    def was_published_recently(self):
        if self.publish:
            now = timezone.now()
            return (self.publish <= now and not self.draft)
        return None

    was_published_recently.admin_order_field = 'publish'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published'


    def get_absolute_url(self):
        return reverse('App:hotel', kwargs={"slug": self.slug})


    class Meta:
        verbose_name = _('Hotel')
        verbose_name_plural = _('Hotels')
        ordering = ['-publish', 'name']

    # formatting hotel objects to show
    def __str__(self):
        return '{} - {}'.format(self.name, self.created)


    # OverRiding Save Method
    # https://docs.djangoproject.com/en/2.1/topics/db/models/#overriding-predefined-model-methods
    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self)
        # Call the "real" save() method.
        super().save(*args, **kwargs)
        # do_something_else()



