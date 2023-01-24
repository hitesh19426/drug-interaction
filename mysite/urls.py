
from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    path('', home, name="home"),
    # path('test/', test, name="test"),
]
