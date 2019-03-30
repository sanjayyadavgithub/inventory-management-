from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *

# Create your views here.


def index(request):
    return render(request, 'index.html')


def display_laptops(request):
    items = Laptop.objects.all()

    context = {
        'items' : items,
        'header': 'Laptops'
    }

    return render(request, 'index.html', context)#3 argument 
    
def display_desktops(request):
    items = Desktop.objects.all()

    context = {
        'items' : items,
        #'name': name,
        'header': 'Desktops'
    }

    return render(request, 'index.html', context)#3 argument 
    
def display_mobiles(request):
    items = Mobile.objects.all()

    context = {
        'items' : items,
        'header': 'Mobiles'
    }

    return render(request, 'index.html', context)#3 argument 
    

def add_laptop(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = LaptopForm()
        return render(request, 'add_new.html', {'form':form})


def add_desktop(request):
    if request.method == "POST":
        form = DesktopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = DesktopForm()
        return render(request, 'add_new.html', {'form':form})


def add_mobile(request):
    if request.method == "POST":
        form = MobileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = MobileForm()
        return render(request, 'add_new.html', {'form':form})



def edit_device(request,pk, model , cls):
    item = get_object_or_404(model,pk=pk)


    if request.method=='POST':
        form = cls(request.POST , instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')




    else:
        form = cls(instance=item)


        return render(request, 'edit_item.html',{'form':form})



def edit_laptop(request,pk):
    return edit_device(request, pk, Laptop, LaptopForm)

def edit_desktop(request,pk):
    return edit_device(request, pk, Desktop, DesktopForm)

def edit_mobile(request,pk):
    return edit_device(request, pk, Mobile, MobileForm)





def delete_laptop(request, pk):
        Laptop.objects.filter(id=pk).delete()

        items = Laptop.objects.all()

        context = {
                'items':items
        }

        return render(request, 'index.html',context)



def delete_desktop(request, pk):
        Desktop.objects.filter(id=pk).delete()

        items = Desktop.objects.all()

        context = {
                'items':items
        }

        return render(request, 'index.html',context)


def delete_mobile(request, pk):
        Mobile.objects.filter(id=pk).delete()

        items = Mobile.objects.all()

        context = {
                'items':items
        }

        return render(request, 'index.html',context)



