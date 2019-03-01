from django.shortcuts import render
from django.views import View, generic
from app.models import Hotel
from django.db.models import Q
from itertools import chain



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
        qs = sorted(query_chain, key=lambda instance: instance.pk,
            reverse=True)
        return qs



class HotelDetailView(generic.DetailView, TagMixin):
    model = Hotel
    template_name = 'hotel_detail.html'
    context_object_name = 'Hotel'


