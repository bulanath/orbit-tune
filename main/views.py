# pylint: disable=E1101, W0613, W0622
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from main.models import Item
from main.forms import ItemForm
from django.urls import reverse
from django.core import serializers
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    items_count = items.count() #Menghitung berapa item yang telah disimpan

    context = {
        'items': items,
        'items_count': items_count,
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login'),
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "create_item.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        
    context = {'form':form}
    return render(request, 'signup.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

#Fungsi untuk fitur menambah dan mengurangi amount stok
def decrement_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        amount_change = int(request.POST.get('amount', 0))
        if item.amount > 0 and amount_change < 0:
            item.amount += amount_change
            item.save()
    return redirect('main:show_main')

def increment_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        amount_change = int(request.POST.get('amount', 0))
        if amount_change > 0:
            item.amount += amount_change
            item.save()
    return redirect('main:show_main')

#Fungsi untuk fitur menghapus objek dari inventori
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('main:show_main')
    return render(request, 'delete_item.html', {'item': item})

def edit_item(request, id):
    item = Item.objects.get(pk = id)

    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form, 'item':item}
    return render(request, "edit_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")