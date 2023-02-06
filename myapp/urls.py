from django.urls import path
from myapp.views import MyView

urlpatterns = [
    path('about/', MyView.as_view())
]