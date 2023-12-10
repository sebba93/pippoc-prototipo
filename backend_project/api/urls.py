from django.urls import path,include
from .views_ai import consult

urlpatterns = [
    path("gpt_request/", consult),
]
