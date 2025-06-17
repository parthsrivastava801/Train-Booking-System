from rest_framework.routers import DefaultRouter
from .views import TrainViewSet, BookingViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'trains', TrainViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
