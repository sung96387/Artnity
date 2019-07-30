"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from art import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.arthome, name='arthome'),
    path('art/new/', views.artnew, name = 'artnew'),
    path('account/',include('account.urls')),
    path('art/create', views.artcreate, name='artcreate'),
    path('art/show/<int:art_id>',views.artshow, name='artshow'),
    path('art/delete/<int:art_id>',views.artdelete, name='artdelete'),
    path('art/edit/<int:art_id>',views.artedit, name='artedit'),
    path('art/update/<int:art_id>',views.artupdate, name='artupdate'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)