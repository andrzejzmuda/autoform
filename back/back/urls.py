from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as tokens

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from autoform import views

router = routers.DefaultRouter()
router.register(r'processors', views.ProcessorViewSet)
router.register(r'actions', views.ActionViewSet)
router.register(r'operations', views.OperationViewSet)
router.register(r'authorisations', views.AuthorisationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
]
