from django.shortcuts import render
from django.views import View, generic
from app.models import Hotel


# Home
class HomeView(View):
    # GET
    def get(self, reQ):

        Template = 'home.html'

        Hotels = Hotel.objects.all()

        context = {
            'Hotels': Hotels
        }

        return render(reQ, Template, context)


