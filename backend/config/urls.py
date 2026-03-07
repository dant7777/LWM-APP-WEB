from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/", include("organisation.urls")),
    path("api/", include("members.urls")),
    path("api/", include("departments.urls")),
    path("api/", include("assignments.urls")),
    path("api/", include("dashboard.urls")),
]
