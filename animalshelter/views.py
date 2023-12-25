from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)
from .models import Dog,News
from .forms import DogForm,DogFilterForm,NewsForm
import base64


class HomePageView(ListView):  # просмотр начальной страницы
    # model = models.News
    context_object_name = "first_page"
    template_name = "index.html"

def index(request):
    news_items = News.objects.all()  # Assuming you want all news items, adjust the queryset as needed
    print(type(news_items), news_items)
    for dog in news_items:
            if dog.photo:
                dog.photo_base64 = base64.b64encode(dog.photo).decode("utf-8")
            else:
                dog.photo_base64 = None
    return render(request, 'index.html', {'news_items': news_items})

def dog_detail(request, dog_id):
    dog = Dog.objects.get(pk=dog_id)

    if dog.photo:
        dog.photo_base64 = base64.b64encode(dog.photo).decode("utf-8")
    else:
        dog.photo_base64 = None
    return render(request, 'dog_detail.html', {'dog': dog})

def news_detail(request, news_id):
    news = News.objects.get(pk=news_id)

    if news.photo:
        news.photo_base64 = base64.b64encode(news.photo).decode("utf-8")
    else:
        news.photo_base64 = None
    return render(request, 'news_detail.html', {'news': news})

def dog_list(request):
    form=DogFilterForm(request.GET)
    if 'reset' in request.GET:
        return redirect('dog_list')

    if form.is_valid():
        age = form.cleaned_data.get('age')
        size = form.cleaned_data.get('size')
        color = form.cleaned_data.get('color')
        temper = form.cleaned_data.get('temper')

        animals = Dog.objects.all()

        if age:
            animals = animals.filter(age=age)

        if size:
            animals = animals.filter(size=size)

        if color:
            animals = animals.filter(color=color)

        if temper:
            animals = animals.filter(temper=temper)

    else:
        animals = Dog.objects.all()
    for dog in animals:
        if dog.photo:
            dog.photo_base64 = base64.b64encode(dog.photo).decode("utf-8")
        else:
            dog.photo_base64 = None
    return render(request, 'dog_list.html', {'form': form, 'animals': animals})
    # for dog in dogs:
    #     if dog.photo:
    #         dog.photo_base64 = base64.b64encode(dog.photo).decode("utf-8")
    #     else:
    #         dog.photo_base64 = None

    # return render(request, 'dog_list.html', {'dogs': dogs})
# def dog_list(request):
#     dogs = Dog.objects.all()
#     return render(request, 'dog_list.html', {'dogs': dogs})

def add_dog(request):
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)  # Вывод отладочной информации
            dog_instance = form.save(commit=False)
            # Преобразование файла в бинарные данные
            dog_instance.photo = form.cleaned_data['photo'].read()
            dog_instance.save()
            return redirect('dog_list') 
    else:
        form = DogForm()

    return render(request, 'add_dog.html', {'form': form})
    
def update_dog(request, dog_id):
    dog_instance = get_object_or_404(Dog, pk=dog_id)

    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES, instance=dog_instance)
        if form.is_valid():
            print(form.cleaned_data)  # Вывод отладочной информации
            dog_instance = form.save(commit=False)
            if 'photo' in form.changed_data:
                # Преобразование файла в бинарные данные
                dog_instance.photo = form.cleaned_data['photo'].read()
            dog_instance.save()
            return redirect('dog_list') 
    else:
        form = DogForm(instance=dog_instance)

    return render(request, 'add_dog.html', {'form': form, 'dog_id': dog_id})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)  # Вывод отладочной информации
            news_instance = form.save(commit=False)
            # Преобразование файла в бинарные данные
            news_instance.photo = form.cleaned_data['photo'].read()
            news_instance.save()
            return redirect('home')  
    else:
        form = NewsForm()

    return render(request, 'add_news.html', {'form': form})

def update_news(request, news_id):
    news_instance = get_object_or_404(News, pk=news_id)

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news_instance)
        if form.is_valid():
            print(form.cleaned_data)  # Вывод отладочной информации
            news_instance = form.save(commit=False)
            if 'photo' in form.changed_data:
                # Преобразование файла в бинарные данные
                news_instance.photo = form.cleaned_data['photo'].read()
            news_instance.save()
            return redirect('home') 
    else:
        form = NewsForm(instance=news_instance)

    return render(request, 'add_news.html', {'form': form, 'news_id': news_id})