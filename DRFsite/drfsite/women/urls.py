from django.urls import path, include
from .views import WomenAPIView

urlpatterns = [
    path('womenlist/', WomenAPIView.as_view()),
    path('womenlist/<int:pk>/', WomenAPIView.as_view())
]
