from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TrainViewSet,
    BookingViewSet,
    RegisterView,
    LoginView,
)

router = DefaultRouter()
router.register(r'trains', TrainViewSet, basename='train')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]
