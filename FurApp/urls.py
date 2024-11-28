from django.urls import path
from FurApp import views

urlpatterns =[
    path('fur/',views.fur,name="fur"),
    path('propage/',views.propage,name="propage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contactpg/',views.contactpg,name="contactpg"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('pro_fil/<cat_name>/', views.pro_fil, name="pro_fil"),
    path('single_fun/<int:pro_id>/',views.single_fun,name="single_fun"),
    path('blogpg/',views.blogpg,name="blogpg"),
    path('', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('save_signup/',views.save_signup,name="save_signup"),
    path('save_login/',views.save_login,name="save_login"),
    path('logout_fun/',views.logout_fun,name="logout_fun"),
    path('save_cart/', views.save_cart, name="save_cart"),
    path('cart_fun/', views.cart_fun, name="cart_fun"),
    path('delete_cart<int:cart_id>/', views.delete_cart, name="delete_cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('save_check/',views.save_check,name="save_check"),
    path('paymentpg/',views.paymentpg,name="paymentpg")


]