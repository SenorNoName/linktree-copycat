from django.contrib import admin
from django.urls import path, include
from register import views as v

from django.conf import settings
from django.conf.urls.static import static

from linktreeApp.views import index
from linktreeApp import views as user_views

urlpatterns = [
    path('app/', include('linktreeApp.urls')),
    path('register/', v.register, name="register"),
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('', index, name='home_page'),
    path('profile/', user_views.my_profile, name='profile'),
    path('profile/<str:username>/', user_views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)