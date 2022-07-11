from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post
from .form import AppoinmentForm
from django.core.mail import send_mail


# Create your views here.
def index(request):
    # get home content

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AppoinmentForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            form.save()

            #cc_myself = form.cleaned_data['email']
            #send_mail("Dây là mai test", 'Dây là mai test', 'hoaithuong.data@gmail.com', [cc_myself])

    else:
        form = AppoinmentForm()

    posts = Post.objects.filter(active= True, status= 1)

    context = {
        'posts': posts,
        'form': form
    }

    return render(request, 'index.html', context=context)


def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk, active= True, status= 1)

    context = {
        'post': post,
    }
    return render(request, "detail.html", context=context)

def postDetailWithSlug(request, slug):
    post = get_object_or_404(Post, slug=slug, active= True, status= 1)

    context = {
        'post': post,
    }

    return render(request, "detail.html", context=context)
