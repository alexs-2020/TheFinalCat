from django.urls import path, include
from . import views
# from contact.views import contact
# from contact.urls import urlpatterns
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('history/', views.history, name="history"),
    # path('catList/', views.catList, name="cat list"),
    path('contact/', include('contact.urls')),

]