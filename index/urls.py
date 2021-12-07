from . import views
from django.urls import path

urlpatterns = [

    path('main', views.index_view)




]