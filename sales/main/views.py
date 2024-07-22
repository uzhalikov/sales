from django.shortcuts import render, redirect
from .forms import AnnouncementForm
from .models import *

def index(request):
    announcements = Announcement.objects.all()
    context = {
        'title': 'Список объявлений',
        'announcements': announcements,
    }
    return render(request, 'main/index.html', context)

def contacts(request):
    return render(request, 'main/contacts.html')

def about(request):
    return render(request, 'main/about.html')



def add_announcement(request):
    user = User.objects.get(id=2)
    form = AnnouncementForm()
    
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.author = user
            author.save()
            return redirect('main/')
        
    context = {
        'title': 'Публикация объявления',
        'form': form,
    }
    return render(request, 'main/add_announcement.html', context)