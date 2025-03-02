from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('studentapi', views.StudentModelViewSet, basename= 'student')  # Auto-generates URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]