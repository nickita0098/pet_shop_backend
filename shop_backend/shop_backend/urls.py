from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('authentication.urls')),
    path('api/', include('goods.urls')),
]
