from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', views.StudentList.as_view()),
    # path('studentapi/', views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>', views.StudentRetrieve.as_view()),
    # path('studentapi/<int:pk>', views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>', views.StudentDestroy.as_view()),
    path('studentapi/', views.StudentListCreate.as_view()),
    path('studentapi/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]