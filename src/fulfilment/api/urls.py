from django.urls import path

from .views import CRMDealInfoCreateView, CRMDealInfoUpdateView


urlpatterns = [
    path('create/', CRMDealInfoCreateView.as_view()),
    path('update/', CRMDealInfoUpdateView.as_view()),
]
