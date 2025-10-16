
from django.contrib import admin
from django.urls import path
from . import views
from .views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('contact/', contact, name='contact'),
]
