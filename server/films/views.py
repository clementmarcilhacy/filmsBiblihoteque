from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Film

from .forms import FilmForm, RawFilmForm

# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello world</h1>")
    return render(request, 'home.html', {})

# def about_view(request, *args, **kwargs):
#     my_context = {
#         "my_text": "this is about django context",
#         "my_number": 123,
#         "my_list": [123, 456, 789]
#     }
#     return render(request, 'about.html', my_context)

# def film_create_view(request):
#     form = FilmForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = FilmForm()
#
#     context = {
#         "form": form
#     }
#     return render(request, 'films/film_create.html', context)

# def film_create_view(request):
#     #print(request.POST)
#     if request.method == 'POST':
#         my_title = request.POST.get('title')
#         print(my_title)
#         #Film.objects.create(title=my_title)
#     context = {}
#     return render(request, 'films/film_create.html', context)

def film_create_view(request):
    my_form = RawFilmForm() # request.GET
    if request.method == 'POST':
        my_form = RawFilmForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Film.objects.create(**my_form.cleaned_data)
            my_form = RawFilmForm() #request.GET
        else:
            print(my_form.erros)
    context = {
        "form": my_form
    }
    return render(request, 'films/film_create.html', context)

def films_list_view(request):
    queryset = Film.objects.all()
    context = {"object_list": queryset}
    return render(request, 'films/films_list.html', context)

# def film_details_view(request, id):
#     obj = Film.objects.get(id=1)
#     context = {"object": obj}
#     return render(request, 'films/film_details.html', context)

def film_details_view(request, my_id):
    #obj = Film.objects.get(id=my_id)
    obj = get_object_or_404(Film, id=my_id)
    context = {"object": obj}
    return render(request, 'films/film_details.html', context)

def film_delete_view(request, my_id):
    obj = get_object_or_404(Film, id=my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../list')

def film_update_view(request, my_id):
    obj = get_object_or_404(Film, id=my_id)
    form = FilmForm(request.POST or None, instance=obj)
    if form.is_valid():
        print("modify film")
        form.save()
        return redirect('../../list')
    context = {"form": form}
    return render(request, 'films/film_create.html', context)
