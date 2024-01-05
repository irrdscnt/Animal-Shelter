from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import (index,add_dog,dog_list,dog_detail,add_news,news_detail,update_dog,update_news,
    search,add_review,delete_animal,delete_news,delete_review)

urlpatterns = [
    path("", index, name="home"),
    path('add_dog/', add_dog, name='add_dog'),
    path('dog_list/', dog_list, name='dog_list'),
    path('dog_detail/<int:animal_id>',dog_detail,name='dog_detail'),
    path('news_detail/<int:news_id>',news_detail,name='news_detail'),
    path('add_news/',add_news,name='add_news'),
    path('update_dog/<int:animal_id>/', update_dog, name='update_dog'),
    path('update_news/<int:news_id>/', update_news, name='update_news'),
    path('search/', search, name='search'),
    path('add_review/', add_review, name='add_review'),
    path('thank_you_page/', TemplateView.as_view(template_name='thank_you_page.html'), name='thank_you_page'),
    path('delete_review/<int:review_id>', delete_review, name='delete_review'),
    path('delete_animal/<int:animal_id>', delete_animal, name='delete_animal'),
    path('delete_news/<int:news_id>', delete_news, name='delete_news'),



]