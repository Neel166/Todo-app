from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from frontend1 import views

router = routers.DefaultRouter()
router.register(r'frontend', views.TodoView, 'frontend')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]