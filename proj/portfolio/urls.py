from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greetings', views.portfolio, name='portfolio'),
    path('', views.index,name='index')

]