from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  
    path('profiles/',views. ProfileList.as_view()),
    path('profiles/<int:pk>/',views. ProfileDetail.as_view()),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
