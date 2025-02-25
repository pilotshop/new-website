from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login_user,name='login'),
    path('about/',views.about,name='about'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('update_info/', views.update_info, name='update_info'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_user/', views.update_user, name='update_user'),
    path('product/<int:pk>', views.pro, name='product'),
    path('category/<str:foo>', views.category, name='category'),
    path('category_summary/', views.category_summary, name='category_summary'),
    path('search/', views.search, name='search'),
]
