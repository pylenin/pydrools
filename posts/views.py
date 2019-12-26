from django.shortcuts import render

from .models import Posts
# Create your views here.
def home(request):
    posts = Posts.objects.all()
    context = {"posts":posts}
    return render(request, "home.html", context)