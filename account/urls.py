from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('index/',views.index,name ='index'),
    path('signup/', views.form_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('', TemplateView.as_view(template_name='account/home.html'), name='home'),
    path('gallery/', TemplateView.as_view(template_name='account/gallery.html'), name='gallery'),
    path('about/', TemplateView.as_view(template_name='account/about.html'), name='about'),

]