from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse

# Create your views here.
from .models import BOOKS


def home(req):
    data = BOOKS.objects.all()
    print("data", data)
    return render(req, 'index.html' , {"data" : data})








def create(req):
    if req.method == "POST":
        book_image = req.POST.get("book_image")
        book_title = req.POST.get("book_title")
        author_name = req.POST.get("author_name")
        publish = req.POST.get("publish")
        disc = req.POST.get("disc")
        BOOKS.objects.create(book_image=book_image,book_title=book_title,author_name=author_name,disc=disc)
        return redirect("home")   
    return render(req, 'create.html')

def update(req,id):
    data = BOOKS.objects.get(id=id)
    return render(req,'update.html',{'book':data})

def update_book(req):
    if req.method == "POST":
        id = req.POST.get("id")
        book_image = req.POST.get("book_image")
        book_title = req.POST.get("book_title")
        author_name = req.POST.get("author_name")
        publish = req.POST.get("publish")
        disc = req.POST.get("disc")
        BOOKS.objects.filter(id=id).update(book_image=book_image,book_title=book_title,author_name=author_name,publish=publish,disc=disc)
        return redirect("home")
    

def delete(req,id):
    data = get_object_or_404(BOOKS,id=id),
    BOOKS.objects.filter(id=id).delete()
    return redirect('home')