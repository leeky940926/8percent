from django.urls import path

from deals.views import DealView

urlpatterns = [
    path('/<int:account_id>', DealView.as_view())
]
