from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField


class User(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self) -> str:
        return f"({self.pk}) {self.name}"

class Car(models.Model):
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    release_date = models.CharField(max_length=4)
    max_speed = models.IntegerField()
    weight = models.IntegerField()
    engine = models.CharField(max_length=20)
    engine_type = models.CharField(max_length=30)
    pokolenie = models.CharField(max_length=20)
    complectation = models.CharField(max_length=30)
    color = models.CharField(max_length=15)
    body = models.CharField(max_length=15)
    transmission = models.CharField(max_length=30)
    steering_wheel = models.CharField(max_length=6)
    image_path = models.CharField(max_length=100)
    privod = models.CharField(max_length=15)
    mileage = models.CharField(max_length=7)


class Product(models.Model):
    user_id = models.IntegerField()
    car_id = models.IntegerField()
    equipment_id = models.IntegerField()
    mile_history = models.IntegerField()
    date_product = models.DateField()
    phone_number = models.CharField(max_length=12)
    city = models.CharField(max_length=168)

class Equipment(models.Model):
    car_id = models.IntegerField()
    B_options = models.CharField(max_length=75)
    O_options = models.CharField(max_length=75)
    S_options = models.CharField(max_length=75)
    K_options = models.CharField(max_length=75)
    M_options = models.CharField(max_length=75)

class Mileage_History(models.Model):
    car_id = models.IntegerField()
    date_registration = models.IntegerField()
    past_mileage = models.IntegerField()

class Report(models.Model):
    car_id = models.IntegerField()
    quanity_RTA = models.IntegerField()
    prohibition_of_registration = models.CharField(max_length=3)
    quanity_fine = models.IntegerField()
    work_in_taxi = models.CharField(max_length=3)
    number_of_owners = models.IntegerField()
    is_the_car_leased = models.CharField(max_length=3)

class Basket(models.Model):
    product = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    count = models.IntegerField(default=0)

