from django.urls import path
from .views import WomenViewSet  # WomenAPIList, WomenAPIUpdate, WomenAPIDetailView

urlpatterns = [
    # path('womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
    # path('womenlist/', WomenAPIList.as_view()),
    # path('womenlist/<int:pk>/', WomenAPIUpdate.as_view()),
    # path('womendetail/<int:pk>/', WomenAPIDetailView.as_view())
]
