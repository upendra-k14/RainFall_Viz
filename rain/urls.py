from django.conf.urls import url
from . import views

urlpatterns = [
    # Basic index page for the application
    url(r'^$', views.index, name='index'),
    ]
