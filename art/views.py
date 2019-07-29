from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Art
# Create your views here.

def arthome(req):
    art = Art.objects.all()
    return render(req, 'arthome.html', {'art_home':art})

def artnew(req):
    return render(req,'artnew.html')

def artcreate(req):
    if(req.method =='POST'):
        new_art =Art()
        new_art.title = req.POST['title']
        new_art.content = req.POST['content']
        if 'image' in req.FILES.key():
            new_art.image = req.FILES['image']
        new_art.save()
    return redirect('/')

def artshow(req, art_id):
    art = get_object_or_404(Art, id = art_id)
    return render(req, 'artshow.html', {'art':art})