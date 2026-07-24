from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)


object = Article.objects.filter(id=18)
object.title = 'Django 5.0 released!'
object.save()

result = Article.objects.filter(created__year=2020).exclude(title__startswith='Django')


def edit_profile(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)

        if user_form.is_valid():
            user_form.save()
            return redirect('user_profile', id=user.id)
        else:
            return render(request, 'edit_profile.html', {'user_form': user_form})
    else:
        user_form = UserForm(instance=user)
        return render(request, 'edit_profile.html', {'user_form': user_form})



def users_page(request):
    users = User.objects.all()
    paginator = Paginator(users, 5)
    page_number = request.GET.get('page', 1)
    users_data = paginator.page(page_number)
    return render(request, 'blog/users_page.html', {'users_data' : users_data})

def books_list(request):
    books = Book.objects.all()
    per_page = request.GET.get('per_page')
    if not per_page or per_page not in [5,10,20]:
        paginator = Paginator(books, 10)
    else:
        paginator = Paginator(books, per_page)

    page_number = request.GET.get('page',1)
    books_data = paginator.page(page_number)
    return render(request,'blog/books_list.html', {'books_data': books_data})