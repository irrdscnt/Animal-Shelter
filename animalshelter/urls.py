from django.urls import path
from . import views
from .views import (HomePageView,index,add_dog,dog_list,dog_detail,add_news,news_detail,update_dog,update_news)

urlpatterns = [
    path("", index, name="home"),
    path('add_dog/', add_dog, name='add_dog'),
    path('dog_list/', dog_list, name='dog_list'),
    path('dog_detail/<int:dog_id>',dog_detail,name='dog_detail'),
    path('news_detail/<int:news_id>',news_detail,name='news_detail'),
    path('add_news/',add_news,name='add_news'),
    path('update_dog/<int:dog_id>/', update_dog, name='update_dog'),
    path('update_news/<int:news_id>/', update_news, name='update_news'),

]