from django.urls import path
from users.views import SigninView

urlpatterns =[
    path('/signin', SigninView.as_view())
]