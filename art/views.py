from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Art, ArtComent
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def arthome(req):
    art = Art.objects.all()
    return render(req, 'arthome.html', {'art_home':art})

def artnew(req):
    return render(req,'artnew.html')

@login_required(redirect_field_name='login')
def artcreate(req):
    if(req.method =='POST'):
        new_art =Art()
        new_art.title = req.POST['title']
        new_art.content = req.POST['content']
        new_art.user = req.user
        if 'image' in req.FILES.keys():
            new_art.image = req.FILES['image']
        new_art.save()
    return redirect('/')
def artdelete(req,art_id):
    art = get_object_or_404(Art,id=art_id)
    art.delete()
    return redirect('/')
def artshow(req, art_id):
    art = get_object_or_404(Art, id = art_id)
    coments = art.artcoment_set.all()
    return render(req, 'artshow.html', {'art':art, 'coment':coments})
def artedit(req,art_id):
    art = get_object_or_404(Art, id = art_id)
    return render(req,'artedit.html',{'art_edit':art})

def artupdate(req, art_id):
    art = get_object_or_404(Art, id=art_id)
    art.title = req.POST['title']
    art.content = req.POST['content']
    art.save()
    return redirect('/art/show/'+ str(art_id))

def comentcreate(req, art_id):
    if(req.method == 'POST'):
        user = get_object_or_404(User, id=req.user.id)
        art = get_object_or_404(Art, id=art_id)
        art.artcoment_set.create(content=req.POST['coment_content'], user=user)

    return redirect('/art/show/' + str(art_id))

def comentdelete(req, coment_id):
    coment = get_object_or_404(ArtComent, id=coment_id)
    art_id = coment.art.id
    coment.delete()
    return redirect('/art/show/'+str(art_id))