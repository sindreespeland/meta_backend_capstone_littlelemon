from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuItemView, SingleMenuItemView, BookingViewSet

router = DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('menu/items', MenuItemView.as_view()),
    path('menu/items/<int:pk>', SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]