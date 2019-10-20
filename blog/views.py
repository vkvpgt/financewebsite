from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post,Update
from .forms import PostForm, UpdateForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('amount')
    return render(request, 'blog/post_list.html',  {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    ram=Update.objects.filter(token=pk)
    sum1=0
    for e in ram:
        sum1=sum1+int(e.givenamount)
    print(sum1)
    return render(request, 'blog/post_detail.html', {'post': post,'post1': ram,'sum1':sum1})



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
def post_delete(request, pk):
     post = get_object_or_404(Post,pk=pk)
     post.delete()
     return redirect('post_list')

def post_update(request,pk):
    if request.method == "POST":
        form = UpdateForm(request.POST)
        if form.is_valid():
            update = form.save(commit=False)
            
            update.token= pk
            update.given_date = timezone.now()
            update.save()
            return redirect('post_list')
    else:
        form = UpdateForm()
        return render(request, 'blog/post_update.html', {'form': form})
