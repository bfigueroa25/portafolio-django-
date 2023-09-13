from django.shortcuts import render
from .models import post    
# Create your views here.


def render_posts(request):
     Posts = post.objects.all()
     return render(request, 'posts.html', {'Posts': Posts})
