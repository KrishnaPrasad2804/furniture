from django.shortcuts import render,redirect
from ShopApp.models import productdb,categorydb
from FurApp.models import contactdb,signupdb,cartdb,orderdb
from django.contrib import messages

import razorpay

# Create your views here.
def fur(req):
    cat = categorydb.objects.all()
    cart=cartdb.objects.filter(Name_up=req.session['Name_up'])
    x=cart.count()
    return render(req,"home.html",{'cat':cat,'x':x})
def propage(req):
    products = productdb.objects.all()
    return render(req,"productpage.html",{'products':products})
def aboutpage(req):
    return render(req,"aboutus.html")
def contactpg(req):
    return render(req,"contact.html")
def save_contact(req):
    if req.method =="POST":
        a = req.POST.get('name')
        b = req.POST.get('email')
        c = req.POST.get('no')
        d = req.POST.get('msg')
        obj = contactdb(Name=a,Email=b,Number=c,Message=d)
        obj.save()
        return redirect(contactpg)
def pro_fil(req,cat_name):
    data =productdb.objects.filter(Product_Category=cat_name)
    return render(req,"product_filter.html",{'data':data})
def single_fun(req,pro_id):
    cate = productdb.objects.get(id=pro_id)
    return render(req,"single_pro.html",{'cate':cate})
def blogpg(req):
    return render(req,"blogpg.html")

def login(req):
    return render(req,"login.html")
def signup(req):
    return render(req,"signup.html")
def save_signup(request):
    if request.method =="POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('number')
        d = request.POST.get('pass')
        e = request.POST.get('re_pass')
        obj = signupdb(Name_up=a,Email_up=b,Number_up=c,Password=d,Confirm=e)
        if signupdb.objects.filter(Name_up=a).exists():
            messages.warning(request,"User Already Exists..!")
            return redirect(signup)
        elif signupdb.objects.filter(Email_up=b).exists():
            messages.warning(request, "Email Address Already Exists..!")
            return redirect(signup)
        obj.save()
        messages.success(request,"Success")
        return redirect(signup)
def save_login(req):
    if req.method=="POST":
        a=req.POST.get('yname')
        b = req.POST.get('ypass')
        if signupdb.objects.filter(Name_up=a,Password=b).exists():
            req.session['Name_up']=a
            req.session['Password']=b
            messages.success(req, "Welcome")
            return redirect(fur)
        else:
            messages.error(req, "Please Check Your Password")
            return redirect(login)
    else:
        messages.warning(req, "Invalid Username")
        return redirect(login)
def logout_fun(req):
    del req.session['Name_up']
    del req.session['Password']
    messages.success(req, "successfully Logouted")
    return redirect(fur)
def save_cart(req):
    if req.method =="POST":
        a = req.POST.get('name')
        b = req.POST.get('pname')
        c = req.POST.get('qty')
        d = req.POST.get('price')
        e = req.POST.get('total')
        f=req.POST.get('')
        try:
            x=productdb.objects.get(product_name=pn)
            img = x.product_image1
        except productdb.DoesNotExists:
            img = None
        obj = cartdb(Name_up=a,Product_Name=b,Quantity=c,Price=d,Total_Price=e)
        obj.save()
        return redirect(fur)
def cart_fun(req):
    cart_data = cartdb.objects.filter(Name_up=req.session['Name_up'])
    subtotal =0
    shipping = 0
    total = 0
    for i in cart_data:
        subtotal = subtotal + i.Total_Price
        if subtotal>50000:
            shipping = 100
        else:
            shipping = 250
        total = subtotal+shipping
    return render(req,"cart.html",{'cart_data':cart_data,'subtotal':subtotal,
                                   'shipping':shipping,
                                   'total':total})
def delete_cart(req,cart_id):
    dlt = cartdb.objects.filter(id=cart_id)
    dlt.delete()
    return redirect(cart_fun)
def checkout(req):
    cart_data = cartdb.objects.filter(Name_up=req.session['Name_up'])
    subtotal = 0
    shipping = 0
    total = 0
    for i in cart_data:
        subtotal = subtotal + i.Total_Price
        if subtotal > 50000:
            shipping = 100
        else:
            shipping = 250
        total = subtotal + shipping
    return render(req,"checkout.html",{'cart_data':cart_data,'subtotal':subtotal,
                                   'shipping':shipping,
                                   'total':total})
def save_check(req):
    if req.method =="POST":
        a = req.POST.get('name')
        b = req.POST.get('place')
        c = req.POST.get('email')
        d = req.POST.get('address')
        e = req.POST.get('number')
        f = req.POST.get('message')
        g = req.POST.get('price')
        obj = orderdb(Name=a,Place=b,Email=c,Address=d,Phone_Number=e,Message=f,Total_Price=g)
        obj.save()
        return redirect(paymentpg)
def paymentpg(req):
    # reterive data from order_db with the specified ID

    customer= orderdb.objects.order_by('-id').first()

    # get the payment amount of the specified customer

    payy= customer.Total_Price

    #convert the amount into paisa (smallst currency unit)

    amount = int(payy*100)   # assuming the payment amount in rupees

    payy_str= str(amount)
    for i in payy_str:
          print(i)
          if req.method=="POST":
              order_currency ='INR'
              client = razorpay.Client(auth=('rzp_test_TkWBp5GMlK0tXv ','gA849IEPQfw2TAva6tmZ7Jfv '))
              payment = Client.order.create({'amount':amount,'currency':order_currency})

    return render(req,"payment.html",{'customer':customer,'payy_str':payy_str})

