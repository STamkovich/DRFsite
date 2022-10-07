from django.urls import path, include
from .views import WomenAPIView

urlpatterns = [
    path('v1/womenlist/', WomenAPIView.as_view()),
]
