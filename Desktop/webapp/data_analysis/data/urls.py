from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('dataset/', views.upload_file, name='store_files'),
    path('dataset/1/compute', views.analyze, name='display'),
]

