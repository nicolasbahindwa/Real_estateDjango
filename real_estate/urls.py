from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from apps.users import views
from django.views.generic import RedirectView

urlpatterns = [
    path("supersecret/", admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/profile/", include("apps.profiles.urls")),
    path('', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Real Estate Admin"
admin.site.site_title = "Real estate Admin Portal"
admin.site.index_title = "welcome to the real estate portal"