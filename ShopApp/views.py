from django.shortcuts import render,redirect
from ShopApp.models import categorydb,productdb
from FurApp.models import contactdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def fur_fun(req):
    return render(req,"index.html")
def cat_fun(req):
    return render(req,"category.html")
def save_cat(req):
    if req.method =="POST":
        a = req.POST.get('cname')
        b = req.FILES['cimg']
        c = req.POST.get('cdes')
        obj = categorydb(Name=a,Image=b,Description=c)
        obj.save()
        messages.success(req,"Category Saved..!")
        return redirect(cat_fun)
def display_cat(req):
    cat =categorydb.objects.all()
    return render(req,"displaycat.html",{'cat':cat})
def edit_cat(req,cat_id):
    cat = categorydb.objects.get(id=cat_id)
    return render(req,"editcat.html",{'cat':cat})
def update_cat(req,cat_id):
    if req.method=="POST":
        a = req.POST.get('cname')
        c = req.POST.get('cdes')
        try:
            img = req.FILES['cimg']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=cat_id).Image
        categorydb.objects.filter(id=cat_id).update(Name=a,Image=file,Description=c)
        messages.warning(req,"Data Updated..")
        return redirect(display_pro)
def delete_cat(req,cat_id):
    dlt = categorydb.objects.filter(id=cat_id)
    dlt.delete()
    messages.error(req,"Data Deleted..")
    return redirect(display_cat)

def pro_fun(req):
    cat = categorydb.objects.all()
    return render(req,"product.html",{'cat':cat})
def save_pro(req):
    if req.method =="POST":
        a = req.POST.get('psel')
        b = req.POST.get('pname')
        c = req.POST.get('qty')
        d = req.POST.get('amt')
        e = req.POST.get('coo')
        f = req.POST.get('man')
        g = req.POST.get('des')
        h = req.FILES['pimg']
        i = req.FILES['pimag']
        j = req.FILES['pimage']
        obj = productdb(Product_Category=a,Product_Name=b,Quantity=c,MRP=d,Country_Of_Orgin=e,Manufactured_By=f,Description=g,Image1=h,Image2=i,Image3=j)
        obj.save()
        messages.success(req, "Product Saved..!")
        return redirect(pro_fun)
def display_pro(req):
    pro =productdb.objects.all()
    return render(req,"displaypro.html",{'pro':pro})
def edit_pro(req,pro_id):
    cat = categorydb.objects.all()
    pro = productdb.objects.get(id=pro_id)
    return render(req,"editpro.html",{'pro':pro,'cat':cat})
def update_pro(req,pro_id):
    if req.method=="POST":
        a = req.POST.get('psel')
        b = req.POST.get('pname')
        c = req.POST.get('qty')
        d = req.POST.get('amt')
        e = req.POST.get('coo')
        f = req.POST.get('man')
        g = req.POST.get('des')
        try:
            img = req.FILES['pimg']
            fs = FileSystemStorage()
            file1 = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file1 = productdb.objects.get(id=pro_id).Image1
        try:
            imga = req.FILES['pimag']
            fs = FileSystemStorage()
            file2 = fs.save(imga.name, imga)
        except MultiValueDictKeyError:
            file2 = productdb.objects.get(id=pro_id).Image2
        try:
            imge = req.FILES['pimage']
            fs = FileSystemStorage()
            file3 = fs.save(imge.name, imge)
        except MultiValueDictKeyError:
            file3 = productdb.objects.get(id=pro_id).Image3
        productdb.objects.filter(id=pro_id).update(Product_Category=a,Product_Name=b,Quantity=c,MRP=d,Country_Of_Orgin=e,Manufactured_By=f,Description=g,Image1=file1,Image2=file2,Image3=file3)
        messages.warning(req, "Product Updated..")
        return redirect(display_pro)
def delete_pro(req,pro_id):
    dlt = productdb.objects.filter(id=pro_id)
    dlt.delete()
    messages.error(req, "Product Deleted..")
    return redirect(display_pro)
def login_fun(req):
    return render(req,"admin_login.html")
def login1(req):
    if req.method == "POST":
        un = req.POST.get('username')
        pswd = req.POST.get('pass')

        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=pswd)

        if user is not None:
            login(req,user)
            req.session['username']=un
            req.session['password'] =pswd
            messages.success(req,"Welcome..")
            return redirect(fur_fun)

        else:
            messages.error(req, "Please Check Your Password..")
            return redirect(login_fun)
    else:
        messages.warning(req, "Invalid Username")
        return redirect(login_fun)

def logout_fun(req):
    del req.session['username']
    del req.session['password']
    messages.success(req,"Successfully Logouted")
    return redirect(login_fun)
def display_contact(req):
    data = contactdb.objects.all()
    return render(req, "contact_data.html",{'data':data})
def delete_contact(req,data_id):
    dlt = contactdb.objects.filter(id=data_id)
    dlt.delete()
    return redirect(display_contact)





