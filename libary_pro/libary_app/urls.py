from django.urls import path
from libary_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('log_or_reg',views.log_or_reg,name='log_or_reg'),
    path('register_page',views.register_page,name='register_page'),
    path('login_page',views.login_page,name='login_page'),
    path('admin_page',views.admin_page,name='admin_page'),
    path('add_book',views.add_book,name='add_book'),
    path('view_book',views.view_book,name='view_book'),
    path('book_details',views.book_details,name='book_details'),
    path('delete_book/<id>',views.delete_book,name='delete_book'),
    path('update/<id>',views.update,name='update'),
]