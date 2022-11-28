from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import *
from .models import *
from Auth.models import *

def main_page(request):
    city = request.POST.get("search_by_city")
    if city == "" or city is None:
        book_list = BookModel.objects.get_queryset().order_by('id')
    else:
        book_list = BookModel.objects.filter(city=city).order_by('id')
    paginator = Paginator(book_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    role = get_role(request)
    try:
        return render(request, 'catalog.html', {"page_obj": page_obj, "role": role})
    except ObjectDoesNotExist:
        return render(request, 'catalog.html', {"page_obj": page_obj, "role": role})


def add_book(request):
    if get_role(request) == 0:
        return redirect('/')
    if request.method == 'GET':
        form = AddAndEditBookForm
        return render(request, "add-book.html", {"form": form})
    elif request.method == 'POST':
        book = BookModel()
        book.name = request.POST.get("name")
        book.author = request.POST.get("author")
        book.publisher = request.POST.get("publisher")
        book.city = request.POST.get("city")
        book.price = request.POST.get("price")
        book.save()
        return redirect("main-page")


def change_book(request, id):
    if get_role(request) in (0, 1):
        return redirect('/')
    try:
        book = BookModel.objects.get(id=id)
        if request.method == "GET":
            form = AddAndEditBookForm(
                initial={
                    "name": book.name,
                    "author": book.author,
                    "publisher": book.publisher,
                    "city": book.city,
                    "price": book.price},
                )
            form.name = book.name
            form.author = book.author
            form.publisher = book.publisher
            form.city = book.city
            form.price = book.price
            return render(request, "change-book.html", {"form": form})
        elif request.method == "POST":
            book.name = request.POST.get("name")
            book.author = request.POST.get("author")
            book.publisher = request.POST.get("publisher")
            book.city = request.POST.get("city")
            book.price = request.POST.get("price")
            book.save()
            return redirect("/")
    except BookModel.DoesNotExist:
        return redirect("/")


def delete_book(request, id):
    if get_role(request) in (0, 1):
        return redirect('/')
    try:
        book = BookModel.objects.get(id=id)
        book.delete()
        return HttpResponseRedirect("/")
    except BookModel.DoesNotExist:
        return HttpResponseRedirect("/")


def get_role(request):
    try:
        if UserModel.objects.get(login=request.session.get("login")) != None:
            role = UserModel.objects.get(login=request.session.get("login")).role
        else:
            role = 0
    except UserModel.DoesNotExist:
        role = 0
    return role
