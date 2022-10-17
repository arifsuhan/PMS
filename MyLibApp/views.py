from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Book

def read(request):
    objects = Book.objects.values()
    return render(request, 'book/read.html', context={'objects': objects})

def create(request):

    if request.method == 'POST':
        print('bookfrom post')
        name = request.POST['name']
        genre = request.POST['genre']

        book_obj = Book.objects.create(name = name, genre = genre)
        print("saved " + str(book_obj))
        return redirect('/book/')
    return render(request, 'book/create.html')

def update(request):

    context = {}

    if request.method == "POST":
        pk_id =  request.POST['pk_id']
        mode = request.POST['mode']

        if mode == "read":
            # temp = Book.objects.get(pk = pk_id)
            temp = Book.objects.all().filter(id=pk_id).values()[0]
            context = temp
        elif mode == "update":
            obj = Book.objects.get(pk=pk_id)
            obj.name = request.POST['update_name']
            obj.genre = request.POST['update_genre']
            obj.save()
            return redirect("/book/")
        return render(request, 'book/update.html', context={'context': context})

def delete(request):
    if request.method == "POST":
        pk_id = request.POST['pk_id']
        instance = Book.objects.get(id=pk_id)
        instance.delete()

    return redirect('/book/')