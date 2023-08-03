from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as tokens

from autoform import views

router = routers.DefaultRouter()
router.register(r'tokens', views.TokenViewSet)
router.register(r'processors', views.ProcessorViewSet)
router.register(r'actions', views.ActionViewSet)
router.register(r'operations', views.OperationViewSet)
router.register(r'authorisations', views.AuthorisationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', tokens.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
