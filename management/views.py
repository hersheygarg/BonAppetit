from django.shortcuts import render, redirect
from management.models import *
from customer.models import *
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def Total(usr):
    dishes = Add_to_cart.objects.filter(user = usr)
    total = 0
    for i in dishes:
        total += (i.dish.price) * (i.qty)
    return dishes, total

def About(request):
    team = Team.objects.all()
    d= {'team':team}
    if request.user.is_authenticated:
        Cartdish, total = Total(request.user)
        d = {'team':team,'Cartdish':Cartdish, 'total':total}

    return render(request, 'about.html',d)

def Menu(request):
    cat = Category.objects.all()
    dishes = Dish.objects.filter(avail = True)
    d = {'cat':cat, 'dishes':dishes}
    if request.user.is_authenticated:
        Cartdish, total = Total(request.user)
        d = {'cat':cat, 'dishes':dishes,'Cartdish':Cartdish, 'total':total}

    return render(request, 'menu.html',d)

def Contact(request):
    if request.user.is_authenticated:
        Cartdish, total = Total(request.user)
        d={'Cartdish':Cartdish, 'total':total}
        return render(request, 'contact.html',d)
    else:
        return render(request, 'contact.html')

def Shop(request, dishid):
    dish = Dish.objects.filter(id = dishid).first()
    if request.POST:
        if not request.user.is_authenticated:
            return redirect('account')
        qty = request.POST['qty']
        data = Add_to_cart.objects.filter(user = request.user, dish = dish).first()
        if data:
            Add_to_cart.objects.filter(user = request.user, dish = dish).update(qty=qty)
        else:
            Add_to_cart.objects.create(user = request.user, dish = dish,)
    d = {'dish':dish}
    return render(request, 'shop.html',d)

    
def AdminHome(request):
    if request.user.is_anonymous:
        return redirect('account')
    if not request.user.is_staff:
        return redirect('home')
    res = Reservation.objects.all()
    order = Add_to_cart.objects.all()
    if "confirm" in request.POST:
        Reservation.objects.filter(id = request.POST['confirm']).update(confirm = True)
        r = Reservation.objects.get(id = request.POST['confirm'])
        sub = "Reservation Confirmed at Tomato"
        from_mail = settings.EMAIL_HOST_USER
        data = dict()
        data = {'name':r.name,'guests':r.guests,'date':r.date,'time':r.time}
        html = get_template('mail.html').render(data)
        msg = EmailMultiAlternatives(sub,'',from_mail,[r.email])
        msg.attach_alternative(html, 'text/html')
        print('result=', msg.send())
    if 'delete' in request.POST:
        Reservation.objects.get(id = request.POST['delete']).delete()
    if 'deleteOrder' in request.POST:
        Add_to_cart.objects.get(id = request.POST['deleteOrder']).delete()
    if "confirmOrder" in request.POST:
        Add_to_cart.objects.filter(id = request.POST['confirmOrder']).update(confirmation = True)
    d = {'res':res, 'order':order}
    return render(request,'index2.html',d)

def EditCategory(request):
    cat = Category.objects.all()
    if 'addCat' in request.POST:
        Category.objects.create(name = request.POST['name'])
    if 'delete' in request.POST:
        Category.objects.get(id = request.POST['delete']).delete()
    d = {'cat':cat}
    return render(request, 'editCat.html',d)

def EditDish(request):
    dish = Dish.objects.all()
    cat = Category.objects.all()
    if 'unavial' in request.POST:
        Dish.objects.filter(id = request.POST['unavial']).update(avail = False)
    if 'avail' in request.POST:
        Dish.objects.filter(id = int(request.POST['avail'])).update(avail = True)
    if 'add' in request.POST:
        category = Category.objects.get(id = request.POST['cat'])
        title = request.POST['title']
        price = request.POST['price']
        mrp = request.POST['mrp']
        dis = request.POST['dis']
        img = request.FILES['img']
        img1 = request.FILES['img1']
        img2 = request.FILES['img2']
        Dish.objects.create(cat = category, title = title, dis = dis, price = price, mrp = mrp, img = img, img1 = img1, img2 = img2)
    if 'delete' in request.POST:
        Dish.objects.get(id = request.POST['delete']).delete()
    d = {'dish':dish, 'cat':cat}
    return render(request, 'editdish.html',d)

def editTeam(request):
    team = Team.objects.all()
    if 'add' in request.POST:
        name = request.POST['name']
        des = request.POST['des']
        fb = request.POST['fb']
        insta = request.POST['insta']
        twt = request.POST['twt']
        img = request.FILES['img']
        Team.objects.create(name = name, designation = des, fb = fb, twiter = twt, insta = insta, img = img)
    if 'delete' in request.POST:
        Team.objects.get(id = request.POST['delete']).delete()   
    d= {'team':team}
    return render(request, 'editteam.html',d)