from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("app.urls")),
    path("accounts/", include("app.accounts.urls")),
]

urlpatterns += [
    path("admin/", admin.site.urls),
]
