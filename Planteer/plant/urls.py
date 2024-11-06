from django.urls import path 
from . import views

app_name = "plant"

urlpatterns = [
    path('detail/',views.detail_view,name="detail_view"),
]