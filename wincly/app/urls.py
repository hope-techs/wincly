from django.urls import path, include

from app.views import HomeView, HotelView, AboutView, HotelDetailView, ContactView

# NameSpace
app_name = 'App'


urlpatterns = [

    path('', HomeView.as_view(), name="home"),
    path('Hotels', HotelView.as_view(), name="hotels"),
    path('Hotels/<slug>', HotelDetailView.as_view(), name="hotel"),
    path('About', AboutView.as_view(), name="about"),
    path('Contact', ContactView.as_view(), name="contact"),

    # DRF API
    # path('API/', include('app.api.urls')),

]
