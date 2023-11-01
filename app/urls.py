
from django.urls import path,include
from app import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('Login/',views.Login,name='Login',),
    path('dashboard/',views.admin,name='admin'),
    path('user/',views.u_profile,name='u_profile'),
    path('notice/',views.all_notices,name='all_notices')
]