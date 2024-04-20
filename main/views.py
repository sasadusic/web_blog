from django.shortcuts import render, redirect
from .models import Blog, Comment
from .forms import CommentForm

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'main/index.html', {'blogs': blogs})

def detail(request, pk):
    post = Blog.objects.get(pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = post
            comment.save()

            return redirect('detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'main/detail.html', {'post': post, 'comments': comments, 'form': form})