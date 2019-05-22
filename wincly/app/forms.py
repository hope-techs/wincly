

from django import forms
# from django.contrib import admin
from .models import Contact



class ContactForm(forms.ModelForm):
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 6}))
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 6, 'class': 'form-control'}))
    # slug = CharField(validators=[validate_slug])
    # my_secret = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    # my_secret = forms.CharField(widget=forms.PasswordInput())

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

    # def clean(self):
    #     cleaned_data = super(ContactForm, self).clean()
    #     name = cleaned_data.get('name')
    #     email = cleaned_data.get('email')
    #     phone
    #     if phone ....
    #     subject = cleaned_data.get('subject')
    #     content = cleaned_data.get('content')
    #


    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'phone', 'subject', 'content')
        localized_fields = ('updated',)

        # https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#overriding-the-default-fields
        widgets = {
            # 'content': forms.Textarea(attrs={'cols': 140, 'rows': 60}),
            # 'content': CKEditorWidget(config_name='ck_comment'),
        }

        # field_classes = {
        #     'slug': MySlugFormField,
        # }
        # labels = {
        #     'name': _('Writer'),
        # }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }
