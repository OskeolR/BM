import json

from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from pip._vendor import requests
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect



# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'INDEX.html')

def profil(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            profile = RegisterUser.objects.get(user=request.user)
            products = Product.objects.all()
            footer = Footer.objects.all()
            footer1 = footer[0]
            most_viewed = Product.objects.all().order_by('-number_click')
            most_viewed_female = Product_female.objects.all().order_by('-number_click')
            most_viewed_category = Category.objects.all().order_by('-number_click')
            orders = Orders_male.objects.filter(user=request.user)
            orders_f = Orders_female.objects.filter(user=request.user)
            context = {'profile':profile, 'products': products, 'footer1': footer1, 'orders_f': orders_f,
                       'most_viewed': most_viewed, 'orders': orders, 'most_viewed_category': most_viewed_category, 'most_viewed_female': most_viewed_female, 'profil':profil}
            return render(request, 'Profile.html', context)
        else:
            return HttpResponseRedirect('/login_user/')

def privacy(request):
    if request.method =='GET':
        footer = Footer.objects.all()
        footer1 = footer[0]
        context = {'footer1':footer1}
        return render(request, 'privacy.html', context)

def edit_profile(request):
    if request.method =='POST':
        edit_profile = request.POST
        name = edit_profile['name']
        surname = edit_profile['surname']
        birthday = edit_profile['birthday']
        adress = edit_profile['adress']
        phone = edit_profile['phone']
        email = edit_profile['email']
        username = name + ' ' + surname
        user_profile = request.user
        register_user_profile = RegisterUser.objects.get(user=request.user)
        register_user_profile.name = name
        register_user_profile.surname = surname
        register_user_profile.birthday = birthday
        register_user_profile.adress = adress
        register_user_profile.phone = phone
        register_user_profile.email = email
        register_user_profile.save()

        user_profile.username = username
        user_profile.email = email
        user_profile.save()

        return HttpResponseRedirect('/profil/')



def terms(request):
    if request.method =='GET':
        footer = Footer.objects.all()
        footer1 = footer[0]
        context = {'footer1':footer1}
        return render(request, 'terms.html', context)

def create_order(request):
    if request.method == 'POST':
        id = request.POST['id']
        quantity = request.POST['quantity']
        gift = request.POST.get('gift', 'No Gift')
        if Product.objects.get(id=id, gender='Male'):
            product = Product.objects.get(id=id, gender__contains='Male')
            order = Orders_male(user=request.user, quantity=quantity, gift=gift, order=product)
            order.save()

            return HttpResponseRedirect('/profil/')

        if Product_female.objects.get(id=id, gender__contains='Female'):
            product_f = Product_female.objects.get(id=id, gender__contains='Female')
            order = Orders_female(user=request.user, quantity=quantity, gift=gift, order=product_f)
            order.save()

            return HttpResponseRedirect('/profil/')


def search(request):
    if request.method ==  'POST':
        keyword = request.POST['search']
        products_male = Product.objects.all()
        results_male = products_male.filter(name__contains=keyword) | products_male.filter(
            category__category__contains=keyword)

        products_female = Product_female.objects.all()
        results_female = products_female.filter(name__contains=keyword) | products_female.filter(
            category__category__contains=keyword)

        footer = Footer.objects.all()
        footer1 = footer[0]

        context = {'results_male': results_male, 'results_female': results_female, 'footer1': footer1}
        return render(request, 'search_result.html', context)

def success(request):
    if request.method == 'GET':
        products = Product.objects.all()
        footer = Footer.objects.all()
        footer1 = footer[0]
        context = {'footer1': footer1, 'products':products}
        return render(request, 'Success.html', context)

def men(request):
    if request.method == 'GET':
        products = Product.objects.all()
        footer = Footer.objects.all()
        footer1 = footer[0]
        unique_all = Unique_ProductMale.objects.all()
        unique = unique_all[0]
        most_viewed = Product.objects.all().order_by('-number_click')
        most_viewed_category = Category.objects.all().order_by('-number_click')
        context = {'products': products, 'footer1':footer1, 'unique':unique, 'most_viewed':most_viewed, 'most_viewed_category':most_viewed_category}
        return render(request, 'MEN.html', context)
def female(request):
    if request.method == 'GET':
        products_female = Product_female.objects.all().order_by()

        footer = Footer.objects.all()
        footer1 = footer[0]
        unique_all = Unique_ProductFemale.objects.all()
        uniqueFemale = unique_all[0]
        most_viewed = Product_female.objects.all().order_by('-number_click')
        most_viewed_category = Category.objects.all().order_by('-number_click')
        context = {'footer1': footer1, 'uniqueFemale':uniqueFemale, 'most_viewed':most_viewed, 'products_female':products_female, 'most_viewed_category':most_viewed_category}
        return render(request, 'projektBM.html', context)

@csrf_protect
def login_user(request):
    if request.method == 'GET':
        footer = Footer.objects.all()
        footer1 = footer[0]
        context = {'footer1': footer1}
        return render(request, 'Login.html', context)
    elif request.method == 'POST':
        login_data = request.POST
        username = login_data['username']
        password = login_data['password']
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/profil/')
                else:
                    user_error = "User is not active"
                    context = {'user_error': user_error}
                    return render(request, 'login.html', context)
            else:
                user_error = 'Data is not correct'
                context = {'user_error': user_error}
                return render(request, 'login.html', context)
        else:
            user_error = 'This username does not exist!'
            context = {'user_error': user_error}
            return render(request, 'login.html', context)

def product_male(request):
    if request.method == 'GET':
        footer = Footer.objects.all()
        footer1 = footer[0]
        id=request.GET['id']
        product=Product.objects.get(id=id)
        images = P_M_images.objects.filter(product_id=id)
        sasi_klikime = 0
        sasi_klikime = product.number_click + 1
        product.number_click = sasi_klikime
        product.save()
        category = Category.objects.get(category=product.category.category)
        sasi_klikime_category = 0
        sasi_klikime_category = category.number_click + 1
        category.number_click = sasi_klikime_category
        category.save()
        most_viewed_category = Category.objects.all().order_by('-number_click')
        most_viewed = Product.objects.all().order_by('-number_click')
        context = { 'footer1': footer1, 'product': product, 'images':images, 'most_viewed':most_viewed, 'most_viewed_category':most_viewed_category}
        return render(request, 'Products.html', context)


def product_female(request):
    if request.method == 'GET':
        footer = Footer.objects.all()
        footer1 = footer[0]

        id = request.GET['id']
        product=Product_female.objects.get(id=id)
        images = P_F_images.objects.filter(product_id=id)
        sasi_klikime = 0
        sasi_klikime = product.number_click + 1
        product.number_click = sasi_klikime
        product.save()
        category = Category.objects.get(category=product.category.category)
        sasi_klikime_category = 0
        sasi_klikime_category = category.number_click + 1
        category.number_click = sasi_klikime_category
        category.save()
        most_viewed_category = Category.objects.all().order_by('-number_click')
        most_viewed = Product_female.objects.all().order_by('-number_click')
        context = {'footer1': footer1,'product': product, 'images':images, 'most_viewed':most_viewed, 'most_viewed_category':most_viewed_category}
        return render(request, 'Products.html', context)


def register(request):
    if request.method == 'GET':
        footer = Footer.objects.all()
        footer1 = footer[0]
        context = { 'footer1': footer1}
        return render(request, 'RegisterForm.html', context)
    elif request.method == 'POST':
        footer = Footer.objects.all()
        footer1 = footer[0]

        captcha_token = request.POST.get("g-recaptcha-response")
        cap_url = "https://www.google.com/recaptcha/api/siteverify"
        cap_secret = "6Lcu418kAAAAAOAXk4Cri9BvVRfaxtffunoTmCeI"
        cap_data = {"secret": cap_secret, "response": captcha_token}
        cap_server_response = requests.post(url=cap_url, data=cap_data)
        cap_json = json.loads(cap_server_response.text)


        register = request.POST
        name = register['name']
        surname = register['surname']
        birthday = register['birthday']
        adress = register['adress']
        phone = register['phone']
        email = register['email']
        password = register['password']
        confirmpassword = register['confirmpassword']
        username = name + ' ' + surname

        if User.objects.filter(username=username).exists():
            user_error = 'This User Already Exists!'
            footer = Footer.objects.all()
            footer1 = footer[0]
            context = {'user_error': user_error, 'footer1': footer1}
            return render(request, 'RegisterForm.html', context)

        elif User.objects.filter(email=email).exists():
            user_error = 'This Email Already Exists!'
            footer = Footer.objects.all()
            footer1 = footer[0]
            context = {'user_error': user_error, 'footer1': footer1}
            return render(request, 'RegisterForm.html', context)
        elif password == confirmpassword:
            if cap_json['success'] == False:
                user_error = 'Make sure you are not a robot!'
                footer = Footer.objects.all()
                footer1 = footer[0]
                context = {'user_error': user_error, 'footer1': footer1}
                return render(request, 'RegisterForm.html', context)
            else:
                user = User.objects.create(username=username, email=email, password=password)
                user.save()
                RegisterInsert = RegisterUser(user=user,phone=phone, name=name, surname=surname, birthday=birthday, adress=adress, email=email,
                                              password=password, confirmpassword=confirmpassword)
                RegisterInsert.save()
                return HttpResponseRedirect('/login_user/')
def payment(request):
    if request.method == 'GET':
        footer = Footer.objects.all()
        footer1 = footer[0]
        context = {'footer1': footer1}
        return render(request, 'payment-getway.html', context)
    elif request.method == 'POST':
        footer = Footer.objects.all()
        footer1 = footer[0]

        contact = request.POST
        fullname = contact['fullname']
        email = contact['email']
        creditcard = contact['creditcard']
        exp = contact['exp']
        cvc = contact['cvc']
        InsertPayment = Payment(fullname=fullname, email=email, creditcard=creditcard, exp=exp, cvc=cvc)
        InsertPayment.save()

        context = {'footer1': footer1}
        return render(request, 'payment-getway.html', context)



def products(request):
    if request.method == 'GET':
        products = Product.objects.all()

        footer = Footer.objects.all()
        footer1 = footer[0]
        context = {'products': products, 'footer1': footer1,}
        return render(request, 'All.html', context)



def products_female(request):
    if request.method == 'GET':
        products = Product_female.objects.all()
        Product_female.objects.all()

        footer = Footer.objects.all()
        footer1 = footer[0]
        context = {'product_female': products, 'footer1': footer1,}
        return render(request, 'All_female.html', context)


def subscribe(request):
    if request.method == 'POST':
        contact = request.POST
        email = contact['subscribe']
        ContactForm = Subscribe ( email=email )
        ContactForm.save()
        return render(request, 'form.html')


def form(request):
    if request.method == 'GET':
        products = Product.objects.all()
        footer = Footer.objects.all()
        footer1 = footer[0]
        context = {'products': products, 'footer1':footer1}
        return render(request, 'form.html', context)
    elif request.method == 'POST':

        captcha_token = request.POST.get("g-recaptcha-response")
        cap_url = "https://www.google.com/recaptcha/api/siteverify"
        cap_secret = "6Lcu418kAAAAAOAXk4Cri9BvVRfaxtffunoTmCeI"
        cap_data = {"secret": cap_secret, "response": captcha_token}
        cap_server_response = requests.post(url=cap_url, data=cap_data)
        cap_json = json.loads(cap_server_response.text)

        contact = request.POST
        name = contact['emri']
        surname = contact['mbiemri']
        email = contact['email']
        phone = contact['telefon']
        comment = contact['comment']

        if cap_json['success'] == False:
            user_error = 'Make sure you are not a robot!'
            context = {'user_error': user_error}
            return render(request, 'form.html', context)
        else:

            ContactForm = Contact(name=name, surname=surname, email=email, phone=phone, Comment=comment)
            ContactForm.save()

            return HttpResponseRedirect('/success/')