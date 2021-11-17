from django.contrib import admin
from django.urls import path, include
from django_api.views import create_student, get_students
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', get_students, name='Get'),
    path('post/', create_student, name='Create'),
    path('api/token/', obtain_auth_token, name='Token')
]
