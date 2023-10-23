from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('project_first_app/', include('project_first_app.urls')),
    path('admin/', admin.site.urls)
]

