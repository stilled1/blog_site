
from django.db import models
from django.db.models import ForeignKey, CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


# class Employee(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     age = models.PositiveIntegerField(default=18)
#     job_title = models.CharField(max_length=20)
#     speciality = models.CharField(max_length=100)
#     from_date = models.DateField()
#
# class Contact(models.Model):
#     phone = models.CharField(max_length=20)
#     email = models.EmailField()
#     address = models.CharField(max_length=255)
#     employee = models.OneToOneField(Employee, on_delete=models.CASCADE)




class Clients(models.Model):
    id = models.IntegerField(primary_key=True)
    last_name = models.CharField()
    first_name = models.CharField()
    phone = models.CharField()
    email = models.EmailField()
    created_at = models.DateField(auto_now_add=True)

class Tables(models.Model):
    class Status(models.TextChoices):
        FREE = 'FR', 'Free'
        BUSY = 'BS', 'Busy'

    id = models.IntegerField(primary_key=True)
    number = models.IntegerField()
    capacity = models.IntegerField()
    location = models.CharField()
    status = models.CharField()

class Waiters(models.Model):
    id = models.IntegerField(primary_key=True)
    last_name = models.CharField()
    first_name = models.CharField()
    patronymic = models.CharField()
    phone = models.CharField()
    hours = models.CharField()
    experience = models.IntegerField()


class WaiterInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    waiter_id = models.OneToOneField(Waiters, on_delete=CASCADE)
    passport_info = models.CharField()
    bank_account = models.CharField()
    emergency_contact = models.CharField()

class Reservations(models.Model):
    id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(Clients, on_delete=CASCADE)
    table_id = models.ForeignKey(Tables, on_delete=CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guest_count = models.IntegerField()


class Dishes(models.Model):
    CATEGORY_CHOICES = [('DRINK', 'Напитки'), ('DESSERTS', 'Десерты'), ('HOT', 'Горячее')]
    id = models.IntegerField(primary_key=True)
    name = models.CharField()
    category = models.CharField(choices=CATEGORY_CHOICES)
    price = models.DecimalField()
    cooking_time_minutes = models.IntegerField()

class Orders(models.Model):
    id = models.IntegerField(primary_key=True)
    table_id = models.ForeignKey(Tables, on_delete=CASCADE)
    waiter_id = models.ForeignKey(Waiters, on_delete=models.SET_NULL)
    date = models.DateField()
    status = models.CharField()
    price = models.DecimalField()

class OrderItems(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=CASCADE)
    dishes_id = models.ForeignKey(Dishes, on_delete=CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField()

