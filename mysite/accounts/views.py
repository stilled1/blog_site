from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib import auth
from django.urls import  reverse_lazy
from .forms import SignUpForm, LoginForm, UpdateUserForm, UpdateProfileForm
from  django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    initial = {}
    template_name = 'registration/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='blog:post_list')

        return super(SignUpView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан для {username}')
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})

class CustomLoginView(LoginView):
    form_class = LoginForm
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True

        return super(CustomLoginView, self).form_valid(form)

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль успешно обновлен')
            return redirect(to='user-profile')

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'registration/profile.html', {'user_form': user_form,
                                            'profile_form': profile_form})



def author_profile(request, username):
    author = get_object_or_404(User, username=username)

    posts = Post.published.filter(author=author)

    return render(request, 'registration/author_profile.html', {
        'author': author,
        'profile': profile,
        'posts': posts,
    })