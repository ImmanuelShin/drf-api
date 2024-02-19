from django.urls import path
from .views import DRFList, DRFDetail

urlpatterns = [
    path('', DRFList.as_view(), name='drf_list'),
    path('<int:pk>/', DRFDetail.as_view(), name='drf_detail'),
]