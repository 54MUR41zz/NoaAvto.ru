from dataclasses import dataclass

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, AbstractUser
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import CarForm #, ProductForm, EquipmentForm, Mileage_HistoryForm, ReportForm
from .models import User, Car, Basket, Equipment, Mileage_History, Report


@dataclass
class CarDto:
    car: Car
    is_in_basket: bool
    count_in_basket: int


def get_cars(request: HttpRequest) -> HttpResponse:
    q = request.GET.get('q', "")
    pages = request.GET.get('pages', 0)
    user1 = request.GET.get('user')

    result = ((Car.objects.filter(name__icontains=q)
               | Car.objects.filter(user__name__icontains=q))
              & Car.objects.filter(count_pages__gt=int(pages)))

    if user:
        result = result.difference(Car.objects.filter(author_id__exact=None))

    if request.user is None or not request.user.is_authenticated:
        return redirect('/')

    basket = Basket.objects.filter(user_id=request.user.id)

    books_dto = []

    for car in result:
        for item in basket:
            if item.product.pk == car.pk:
                car_dto = CarDto(
                    car = car,
                    is_in_basket=True,
                    count_in_basket=item.count,
                )
                car_dto.append(car_dto)
                break
        else:
            car_dto = CarDto(
                car = car,
                is_in_basket=False,
                count_in_basket=0,
            )
            books_dto.append(car_dto)

    return render(request, 'books.html', {
        'books': books_dto,
        'q': q,
        'pages': pages,
        'basket': basket,
    })


def create_car(request: HttpRequest) -> HttpResponse:
    if request.user is None or not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('/')

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            pages = form.cleaned_data['count_pages']
            author = form.cleaned_data['author']
            Car.objects.create(name=name, author=author, count_pages=pages)
            return redirect("/")
        else:
            return render(request, 'formform.html', {
                'form': form,
                'errors': form.errors,
            })
    else:
        form = CarForm()
        return render(request, 'formform.html', {
            'form': form,
        })


def edit_car(request: HttpRequest) -> HttpResponse:
    if request.user is None or not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('/')

    car_id = request.GET.get('car_id')
    car = Car.objects.get(id=car_id)

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            pages = form.cleaned_data['count_pages']
            author = form.cleaned_data['author']

            car.name = name
            car.count_pages = pages
            car.author = author
            car.save()

            return redirect("/")
        else:
            return render(request, 'test.html', {
                'form': form,
                'errors': form.errors,
            })
    else:
        form = CarForm()

        form.fields['name'].initial = car.name
        form.fields['count_pages'].initial = car.count_pages
        form.fields['author'].initial = car.author

        return render(request, 'test.html', {
            'form': form,
        })


def delete_car(request: HttpRequest) -> HttpResponse:
    car_id = request.GET.get('car_id')
    car = Car.objects.get(id=car_id)

    if request.method == 'POST':
        car.delete()
        return redirect("/")
    else:
        return render(request, 'delete_accept.html', {
            "name": car.name,
        })


def get_basket(request: HttpRequest) -> HttpResponse:
    if request.user is None or not request.user.is_authenticated:
        return redirect('/')

    basket = Basket.objects.filter(user_id=request.user.id)
    return render(request, 'basket.html', {
        "basket": basket,
    })


def add_to_basket(request: HttpRequest) -> HttpResponse:
    car_id = request.GET.get('car_id')
    car = Car.objects.get(id=car_id)

    if request.user is None or not request.user.is_authenticated:
        return redirect('/')

    user = request.user

    basket = Basket.objects.create(user=user, product=car, count=1)
    basket.save()

    return redirect("/")


def minus_from_basket(request: HttpRequest) -> HttpResponse:
    car_id = request.GET.get('product_id')
    car = Car.objects.get(id=car_id)

    update_count_in_basket(car, request.user, "-")
    return redirect("/")


def plus_to_basket(request: HttpRequest) -> HttpResponse:
    car_id = request.GET.get('product_id')
    car = Car.objects.get(id=car_id)

    update_count_in_basket(car, request.user, "+")
    return redirect("/")


def update_count_in_basket(product: Car, user: AbstractBaseUser, operation: str) -> int:
    basket_item = Basket.objects.get(user=user, product=product)
    if operation == '-':
        basket_item.count -= 1
        if basket_item.count == 0:
            basket_item.delete()
            return 0
    else:
        basket_item.count += 1

    basket_item.save()
    return basket_item.count