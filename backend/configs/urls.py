"""
URL configuration for configs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Auto parks",
        default_version='v1',
        description="About cars and how to build api endpoints",
        contact=openapi.Contact(email='nadinyman@gmail.com'),
    ),

    public=True,
    permission_classes=[AllowAny, ]
)

urlpatterns = [
    path('api/cars', include('apps.cars.urls')),
    path('api/auto_parks', include('apps.auto_parks.urls')),
    path('api/users', include('apps.users.urls')),
    path('api/auth', include('apps.auth.urls')),
    path('api/doc', schema_view.with_ui('swagger', cache_timeout=0), name='documentation'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
