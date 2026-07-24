from django.conf import settings
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from . import forms
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from mysite import settings
# Create your views here.
"""

def post_list(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html' , {'posts': posts})
"""
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/post/list.html'




def post_detail(request, year,month,day,slug):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             publish__year=year,
                             publish__month=month,
                             publish__day = day,
                             slug=slug
                             )
    return render(request, 'blog/post/detail.html', {'post': post})

def post_share(request, post_id):
    post = get_object_or_404(Post,
                              id=post_id,
                              status=Post.Status.PUBLISHED)
    sent = False

    if request.method == "POST":
        form = forms.EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{post.author} поделился с вами {post.title}'
            message = (f'Читать {post.title} по ссылке {post_url}\n\n'
                       f'{cd["name"]} ({cd["email"]}) прокомментировал: {cd["comment"]}\n')
            send_mail(subject, message, settings.EMAIL_HOST_USER, [cd['to']])
            sent = True
    else:
        form = forms.EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post,'form': form,'sent': sent})

