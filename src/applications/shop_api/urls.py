from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserList
from django.urls import path, include
from .views import ProductViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserList.as_view()),
    path('viewsets/', include(router.urls)),
]

