from django.urls import path
from ShopApp import views
# from FurApp import views
urlpatterns =[
    path('fur_fun/',views.fur_fun,name="fur_fun"),
    path('cat_fun/',views.cat_fun,name="cat_fun"),
    path('save_cat/',views.save_cat,name="save_cat"),
    path('display_cat/',views.display_cat,name="display_cat"),
    path('edit_cat/<int:cat_id>/', views.edit_cat, name="edit_cat"),
    path('update_cat/<int:cat_id>/', views.update_cat, name="update_cat"),
    path('delete_cat/<int:cat_id>/', views.delete_cat, name="delete_cat"),
    path('pro_fun/',views.pro_fun,name="pro_fun"),
    path('save_pro/',views.save_pro,name="save_pro"),
    path('display_pro/',views.display_pro,name="display_pro"),
    path('edit_pro/<int:pro_id>/', views.edit_pro,name="edit_pro"),
    path('update_pro/<int:pro_id>/', views.update_pro, name="update_pro"),
    path('delete_pro/<int:pro_id>/', views.delete_pro, name="delete_pro"),
    path('login_fun/',views.login_fun,name="login_fun"),
    path('login1/',views.login1,name="login1"),
    path('logout_fun/',views.logout_fun,name="logout_fun"),
    path('display_contact/',views.display_contact,name="display_contact"),
    path('delete_contact/<int:data_id>/', views.delete_contact, name="delete_contact")

]