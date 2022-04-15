from django.urls import include, path
from api.views import UploadImage

urlpatterns = [

    path("upload/image", UploadImage.as_view()),
]