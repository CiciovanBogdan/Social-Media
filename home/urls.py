from django.urls import path

from home import views

urlpatterns = [
    path('', views.HomePageListView.as_view(), name='home_page')
]
