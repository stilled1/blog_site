from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label='Имя')
    last_name = forms.CharField(max_length=100, label='Фамилия')
    username = forms.CharField(max_length=30, label='Имя пользователя')
    email = forms.EmailField(max_length=100, label='Почта')
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(), label='Подтверждение пароля')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        error_messages = {
            'username': 'Логин занят другим пользователям'
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    remember_me = forms.BooleanField(required=False)

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label='Имя')
    email = forms.EmailField(max_length=100, label='Почта')

    class Meta:
        model = User
        fields = ('username', 'email')

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput())
    bio = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = User
        fields = ('avatar', 'bio')