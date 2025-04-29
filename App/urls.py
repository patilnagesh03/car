from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.CarsView, name='cars'),
    path('car/<int:id>/',views.Cars, name='car'),
    path('about/',views.About),
    path('contact/',views.contact),
    path('services/',views.services),
]