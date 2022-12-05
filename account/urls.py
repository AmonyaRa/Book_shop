from django.urls import path

from account.views import *

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', LoginApiView.as_view())
    ]
