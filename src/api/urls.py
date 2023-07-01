from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from rest_framework import permissions, routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from src.apps.core.views import LogoutView, UserViewSet

schema = swagger_get_schema_view(
    openapi.Info(
        title='SOCIO Swagger',
        default_version='1.0.0',
        description='API for socio project of zoom',
        contact=openapi.Contact(email='guilherme.dias@zoom.education'),
        license=openapi.License(name='Apache 2.0'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.SimpleRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/v1/',
        include(
            [
                path(r'', include(router.urls)),
                path(
                    'token/',
                    TokenObtainPairView.as_view(),
                    name='token_obtain_pair',
                ),
                path(
                    'token/refresh/',
                    TokenRefreshView.as_view(),
                    name='token_refresh',
                ),
                path('logout/', LogoutView.as_view(), name='logout'),
                path('', schema.with_ui('swagger', cache_timeout=0)),
                path('swagger/', schema.with_ui('swagger', cache_timeout=0)),
                path('redoc/', schema.with_ui('redoc', cache_timeout=0)),
            ]
        ),
    ),
]
