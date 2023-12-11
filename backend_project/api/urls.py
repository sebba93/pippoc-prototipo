from django.urls import path,include
from .views_ai import consult
from .views import upload_file, view_file

urlpatterns = [
    path("gpt_request/", consult),
    path("upload/", upload_file),
    path("archivos/<str:name>", view_file)
]
