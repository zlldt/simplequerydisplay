from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.search_form),
    path('<int:id_num>/', views.detail, name='detail'),
    path('search-form/', views.search_form),
    path('search/', views.search),
]