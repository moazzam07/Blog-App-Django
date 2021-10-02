from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("login",views.login,name='login'),
    path("signup",views.signup,name='signup'),
    path("",views.home,name='home'),
    path("compose",views.compose,name='compose'),
    path("profile",views.profile,name='profile')
]
