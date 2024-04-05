from django.urls import path

from .views import CRMDealInfoView


urlpatterns = [
    path('', CRMDealInfoView.as_view()),
]
