from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import index, MenuItemView, SingleMenuItemView, BookingViewSet

router = DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('menu/items/', MenuItemView.as_view(), name='menuitems'),
    path('menu/items/<int:pk>/', SingleMenuItemView.as_view(), name='menuitem-detail'),
    path('booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]