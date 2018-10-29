from django.urls import path, include

from app.views import HomeView

# NameSpace
app_name = 'App'


urlpatterns = [

    path('', HomeView.as_view(), name="home"),

    # DRF API
    # path('API/', include('app.api.urls')),

]
