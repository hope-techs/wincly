from django.shortcuts import render
from django.views import View, generic
from app.models import Hotel



# Tag Mixin View
class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context



# Home
class HomeView(View):
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
        query = req.GET.get('q', None)
        queryset = Hotel.objects.all()
        if query is not None:
            queryset = Hotel.objects.search(query)
        return queryset


class HotelDetailView(generic.DetailView, TagMixin):
    model = Hotel
    template_name = 'hotel_detail.html'
    context_object_name = 'Hotel'


