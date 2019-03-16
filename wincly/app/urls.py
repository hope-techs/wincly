from django.urls import path, include

from app.views import HomeView, HotelView, AboutView

# NameSpace
app_name = 'App'


urlpatterns = [

    path('', HomeView.as_view(), name="home"),
    path('Hotels', HotelView.as_view(), name="hotels"),
    path('About', AboutView.as_view(), name="about"),

    # DRF API
    # path('API/', include('app.api.urls')),

]
