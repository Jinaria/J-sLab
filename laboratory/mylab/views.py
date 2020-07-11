from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post, Comment
from .forms import PostForm, CommentForm
# Create your views here.

def index(request):
    """
    첫 페이지
    """
    post_list = Post.objects.order_by('-create_date')

    context = {'post_list':post_list}
    return render(request, "mylab/index.html", context)

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.save()
            return redirect('mylab:index')
    else:
        form = PostForm()        
    context = {'form':form}
    return render(request, 'mylab/post_form.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    context = {'post':post}
    return render(request, 'mylab/post_detail.html', context)
