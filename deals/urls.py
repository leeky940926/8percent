from django.urls import path

from deals.views import DealView

urlpatterns = [
    path('', DealView.as_view())
]
