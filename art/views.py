from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Art, ArtComent#, Like
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
try:
    from django.utils import simplejson as json
except ImportError:
    import json
#from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
# Create your views here.
def artList(req):
    category = req.GET['category']
    art = Art.objects.filter(category=category)
    return render(req,'fashion.html',{'fashion':art})

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
        new_art.category=req.POST.get('category',False)
        new_art.price = req.POST['price']
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

# @login_required
# def art_like_toggle(req,art_id):
#     art = get_object_or_404(Art,id=art_id)
#     user = req.user
#     profile = Profile.objects.get(user=user)

#     check_like_art = profile.like_arts.filter(id=art_id)

#     if check_like_art.exists():
#         profile.like_arts.remove(art)
#         art.like_count -=1
#         art.save()
#     else:
#         profile.like_arts.add(art)
#         art.like_count += 1
#         art.save()

#     return redirect('/')

# def like(req, art_id):
#     art = get_object_or_404(Art,pk=art_id)
#     liked = Like.objects.filter(user=req.user,art=art)
#     if not liked :
#         Like.objects.create(user=req.user,art=art)
#     else:
#         liked.delete()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
