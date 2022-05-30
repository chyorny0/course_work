import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Car, Restoration, Range, RangeVoteAdd
from .forms import CarForm, RegisterForm, LoginForm, SearchForm



A = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]




def index(request):
    return render(request, 'index.html')




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password,)
                user.save()
                return redirect('login')

        else:
            return redirect('register')
    else:
        registerform = RegisterForm
        return render(request, 'register.html', {"form": registerform})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect ('login')
    else:
        loginform = LoginForm
        return render(request, 'login.html', {"form": loginform})

def logout(request):
    auth.logout(request)
    return redirect('/')

def restoration(request):
    if request.method == 'POST':
        search = request.POST['search']
        restoration = Restorstion.objects.filter(name = search)
        searchform = SearchForm()
        data = {"restorations": restorations, "form": searchform}
        return render(request, 'restoration.html', context=data)
    restorations = Restoration.objects.all()
    searchform = SearchForm()
    data = {"restorations": restorations, "form": searchform}
    return render(request, 'restoration.html', context=data)

def car(request):
    if request.method == 'POST':
        search = request.POST['search']
        cars = Car.objects.filter(name = search)
        searchform = SearchForm()
        data = {"cars": cars, "form": searchform,}
        return render(request, 'car.html', context=data)
    cars = Car.objects.all()
    searchform = SearchForm()
    data = {"cars": cars, "form": searchform}
    return render(request, 'car.html', context=data)

def car_ordered(request):
    cars = Car.objects.order_by('name')
    data = {"cars": cars}
    return render(request, 'car.html', context=data)

def restoration_ordered(request):
    restorations = Restoration.objects.order_by('name')
    data = {"restorations": restorations}
    return render(request, 'restoration.html', context=data)

def car_filtrated(request):
    cars = Car.objects.filter(price__lte = 8000)
    data = {"cars": cars}
    return render(request, 'car.html', context=data)

def restoration_filtrated(request):
    restorations = Restoration.objects.filter(total_price__lte = 5000)
    data = {"restorations": restorations}
    return render(request, 'restoration.html', context=data)



def car_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        mark = request.POST['mark']
        price = request.POST['price']
        year = request.POST['year']

        car = Car.objects.create(name=name, mark=mark, price=price, year=year)
        car.save()
        return redirect('car')
    else:
        carform = CarForm
        return render(request, 'car_create.html', {"form": carform})

def range(request):
    if request.method == 'POST':
        i0j1 = int(request.POST['i0j1'])
        i0j2 = int(request.POST['i0j2'])
        i0j3 = int(request.POST['i0j3'])
        i1j0 = int(request.POST['i1j0'])
        i1j2 = int(request.POST['i1j2'])
        i1j3 = int(request.POST['i1j3'])
        i2j0 = int(request.POST['i2j0'])
        i2j1 = int(request.POST['i2j1'])
        i2j3 = int(request.POST['i2j3'])
        i3j0 = int(request.POST['i3j0'])
        i3j1 = int(request.POST['i3j1'])
        i3j2 = int(request.POST['i3j2'])
        if i0j1 == 1:
            A[0][1] +=1
        if i0j2 == 1:
            A[0][2] +=1
        if i0j3 == 1:
            A[0][3] +=1
        if i1j0 == 1:
            A[1][0] +=1
        if i1j2 == 1:
            A[1][2] +=1
        if i1j3 == 1:
            A[1][3] +=1
        if i2j0 == 1:
            A[2][0] +=1
        if i2j1 == 1:
            A[2][1] +=1
        if i2j3 == 1:
            A[2][3] +=1
        if i3j0 == 1:
            A[3][0] +=1
        if i3j1 == 1:
            A[3][1] +=1
        if i3j2 == 1:
            A[3][2] +=1
        return redirect('/')
    else:
        restorations = RangeVoteAdd.objects.all().reverse()[0]
        return render(request, 'range.html', {"restorations":restorations})

def rangeresult(request):
    result1 = A[0][1] + A[0][2] + A[0][3]
    result2 = A[1][0] + A[1][2] + A[1][3]
    result3 = A[2][0] + A[2][1] + A[2][3]
    result4 = A[3][0] + A[3][1] + A[3][2]
    Range.objects.all().delete()
    resultnumber = 1
    rangeresult = Range.objects.create(result=result1, resultnumber=resultnumber)
    rangeresult.save()
    resultnumber = 2
    rangeresult = Range.objects.create(result=result2, resultnumber=resultnumber)
    rangeresult.save()
    resultnumber = 3
    rangeresult = Range.objects.create(result=result3, resultnumber=resultnumber)
    rangeresult.save()
    resultnumber = 4
    rangeresult = Range.objects.create(result=result4, resultnumber=resultnumber)
    rangeresult.save()
    rengeresult =  Range.objects.order_by('-result')
    restorations = RangeVoteAdd.objects.all().reverse()[0]
    data = {"rengeresult": rengeresult, "restorations": restorations}
    return render(request, 'result.html', context=data)







