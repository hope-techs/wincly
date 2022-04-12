from django.shortcuts import render
from django.views import View, generic
from app.models import Hotel, HotelImage, Contact
from django.db.models import Q
from itertools import chain
from app.forms import ContactForm



# Tag Mixin View
class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context



# Home
class HomeView(View, TagMixin):
    # GET
    def get(self, reQ):

        Template = 'home.html'

        Hotels = Hotel.objects.all()[:6]

        context = {
            'Hotels': Hotels
        }

        return render(reQ, Template, context)


# Hotels
class HotelView(generic.ListView, TagMixin):
    template_name = 'hotels.html'
    context_object_name = 'Hotels'
    paginate_by = 12

    def get_queryset(self):
        req = self.request
        country_query = req.GET.get('country', None)
        city_query = req.GET.get('city', None)
        hotel_query = req.GET.get('hotel', None)
        queryset = Hotel.objects.all()
        # Country
        if country_query :
            queryset = queryset.filter(
                    Q(country__icontains=country_query) |
                    Q(tags__name__icontains=country_query)
                ).distinct()
        # City
        if city_query :
            queryset = queryset.filter(
                    Q(city__icontains=city_query) |
                    Q(tags__name__icontains=city_query)
                ).distinct()
        # Hotel
        if hotel_query :
            queryset = queryset.filter(
                    Q(name__icontains=hotel_query) |
                    Q(slug__icontains=hotel_query) |
                    Q(tags__name__icontains=hotel_query)
                ).distinct()


        query_chain = chain(
            queryset
        )
        return sorted(query_chain, key=lambda instance: instance.pk, reverse=True)


# Hotel Detail View
class HotelDetailView(generic.DetailView, TagMixin):
    model = Hotel
    template_name = 'hotel_detail.html'
    context_object_name = 'hotel'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        current_hotel = context.get('hotel')
        # Add in a QuerySet of all the books
        context['hotel_images'] = current_hotel.hotel_image.all()
        return context


# About
class AboutView(View, TagMixin):
    # GET
    def get(self, reQ):
        Template = 'about.html'
        context = {  }

        return render(reQ, Template, context)


# Contact us
# Contact Mixin
class ContactMixin:
    fields = ['first_name', 'last_name', 'email', 'phone', 'subject', 'content']

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.

        # Why use commin = false ?
        # print (form.cleand_data.get('title'))
        # print (form.cleand_data['title'))

        ins = form.save(commit = False)

        # The Answer of top question
        # print(ins.title)

        # Do custom logic here
        # It should return an HttpResponse
        ins.save()
        # We can put logic in template {% if "html_safe" in messages.tags %} {{ messages | safe}} {% else %} {{ messages }} {% endif %}
        # messages.success(self.request, "Message Sent Successfully", extra_tags='html_safe')
        messages.info(self.request, self.success_msg)
        return super(ContactMixin, self).form_valid(form)

    def form_invalid(self, form):
        # Do custom logic here
        messages.error(self.request, "Try Again!")
        return super(ContactView, self).form_invalid(form)


# Contact
class ContactView(ContactMixin, generic.FormView):

    template_name = 'contact_us.html'
    form_class = ContactForm
    success_url = '/Contact'
    success_msg = "Message Sent Successfully"
