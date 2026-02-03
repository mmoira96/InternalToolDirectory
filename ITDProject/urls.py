from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("codechallenge3.urls")),   # NO "tools/" here
]
