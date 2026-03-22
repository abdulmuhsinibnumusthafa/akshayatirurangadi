from django.shortcuts import render, get_object_or_404
from .models import Announcement, ContactInfo

def home(request):
    announcements = Announcement.objects.all().order_by('-created_at')[:5]
    contact = ContactInfo.objects.first()

    return render(request, 'home.html', {
        'announcements': announcements,
        'contact': contact
    })


def announcements(request):
    posts = Announcement.objects.all().order_by('-created_at')
    return render(request, 'announcements.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Announcement, id=id)
    return render(request, 'post_detail.html', {'post': post})


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    contact = ContactInfo.objects.first()
    return render(request, 'contact.html', {'contact': contact})