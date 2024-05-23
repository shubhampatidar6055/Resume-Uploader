from django.urls import path
from.views import *

urlpatterns = [
    path("",Resume_view.as_view()),
]
