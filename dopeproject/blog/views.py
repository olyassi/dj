
from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    latest_post_list = Post.objects.order_by('-published_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.html',context)
def main(request):
    return HttpResponse ("Notfound")
from django.http import HttpResponse

def article(request, post_id):
    return render(request, 'blog/ind.html')

def create(request):
    if request.method == 'POST': #здесь пост - имя HTTP метода
        post = Post(title = request.POST['title'], text= request.POST['text'])
        post.save()
        return HttpResponseRedirect(reverse('blog:index'))
    else:
        return render(request, 'blog/create.html')