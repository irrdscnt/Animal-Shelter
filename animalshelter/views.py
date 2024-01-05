from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)
from .models import Animal,News,Review,Adoption
from .forms import AnimalForm,AnimalFilterForm,NewsForm,ReviewForm,AdoptionForm
import base64
from .filters import AnimalFilter
from django.http import HttpResponseRedirect
from django.urls import reverse


def search(request):
    animal_list = Animal.objects.all()
    filter = AnimalFilter(request.GET, queryset=animal_list)

    context = {
        'filter': filter,
    }

    return render(request, 'dog_list.html', context)

def index(request):
    news_items = News.objects.all()  
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the index page or another appropriate page
    else:
        form = ReviewForm()
        print(form.errors)


    review_list = Review.objects.all()
    for review in review_list:
            if review.photo:
                review.photo_base64 = base64.b64encode(review.photo).decode("utf-8")
            else:
                review.photo_base64 = None
    for dog in news_items:
            if dog.photo:
                dog.photo_base64 = base64.b64encode(dog.photo).decode("utf-8")
            else:
                dog.photo_base64 = None
    animals = Animal.objects.all()
    if request.method == 'POST':
        adoptform = AdoptionForm(request.POST)
        if adoptform.is_valid():
            adoptform.save()
            return redirect('thank_you_page')
    else:
        adoptform = AdoptionForm()
    return render(request, 'index.html', {'news_items': news_items,'form':form, 'review_list': review_list,'adoptform':adoptform})

def dog_detail(request, animal_id):
    dog = Animal.objects.get(pk=animal_id)

    if dog.photo:
        dog.photo_base64 = base64.b64encode(dog.photo).decode("utf-8")
    else:
        dog.photo_base64 = None
    
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            form.instance.animal = dog
            form.save()
            return redirect('thank_you_page') 
    else:
        form = AdoptionForm()

    return render(request, 'dog_detail.html', {'dog': dog, 'form': form})

def news_detail(request, news_id):
    news = News.objects.get(pk=news_id)

    if news.photo:
        news.photo_base64 = base64.b64encode(news.photo).decode("utf-8")
    else:
        news.photo_base64 = None
    return render(request, 'news_detail.html', {'news': news})

def dog_list(request):
    form=AnimalFilterForm(request.GET)
    if 'reset' in request.GET:
        return redirect('dog_list')

    if form.is_valid():
        age = form.cleaned_data.get('age')
        size = form.cleaned_data.get('size')
        color = form.cleaned_data.get('color')
        temper = form.cleaned_data.get('temper')
        type_of_animal=form.cleaned_data.get('type_of_animal')

        animals = Animal.objects.all()
        if type_of_animal:
            animals=animals.filter(type_of_animal=type_of_animal)
            
        if age:
            animals = animals.filter(age=age)

        if size:
            animals = animals.filter(size=size)

        if color:
            animals = animals.filter(color=color)

        if temper:
            animals = animals.filter(temper=temper)

    else:
        animals = Animal.objects.all()
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
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            dog_instance = form.save(commit=False)
            dog_instance.photo = form.cleaned_data['photo'].read()
            dog_instance.save()
            return redirect('dog_list') 
    else:
        form = AnimalForm()

    return render(request, 'add_dog.html', {'form': form})

# def add_dog(request):
#     if request.method == 'POST':
#         form = AnimalForm(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)  # Вывод отладочной информации
#             dog_instance = form.save(commit=False)
#             # Преобразование файла в бинарные данные
#             dog_instance.photo = form.cleaned_data['photo'].read()
#             dog_instance.save()
#             return redirect('dog_list') 
#     else:
#         form = AnimalForm()

#     return render(request, 'add_dog.html', {'form': form})
    
def update_dog(request, animal_id):
    dog_instance = get_object_or_404(Animal, pk=animal_id)

    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=dog_instance)
        if form.is_valid():
            print(form.cleaned_data)  # Вывод отладочной информации
            dog_instance = form.save(commit=False)
            if 'photo' in form.changed_data:
                # Преобразование файла в бинарные данные
                dog_instance.photo = form.cleaned_data['photo'].read()
            dog_instance.save()
            return redirect('dog_list') 
    else:
        form = AnimalForm(instance=dog_instance)

    return render(request, 'add_dog.html', {'form': form, 'animal_id': animal_id})

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


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)  # Вывод отладочной информации
            news_instance = form.save(commit=False)
            # Преобразование файла в бинарные данные
            news_instance.photo = form.cleaned_data['photo'].read()
            news_instance.save()
            return redirect('home')  
    else:
        form = ReviewForm()

    return render(request, 'index.html', {'form': form})

def delete_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    animal.delete()
    return redirect('dog_list')  

def delete_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    news.delete()
    return redirect('home')  

def delete_review(request, id):
    review = get_object_or_404(Review, pk=id)
    review.delete()
    return redirect('home')  

def delete_adoption(request, id):
    adoption = get_object_or_404(Adoption, pk=id)
    adoption.delete()
    return redirect('adoption_requests')  

def adoption_requests(request):
    adoption_forms = Adoption.objects.all()
    return render(request, 'adoption_requests.html', {'adoption_forms': adoption_forms})
# class AddReview(CreateView):
#     model = Review
#     form_class = ReviewForm
#     template_name = "index.html"
#     success_url = "home"

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)

#         context["review_list"] = Review.objects.all()  # Add this line to fetch existing reviews
#         return context

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         return response

#     def form_invalid(self, form):
#         response = super().form_invalid(form)
#         return response