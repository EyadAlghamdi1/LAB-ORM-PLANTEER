from django.urls import path 
from . import views

app_name = "plant"

urlpatterns = [
    path('new/',views.add_view,name="add_view"),
    path('update/<plant_id>',views.update_view,name="update_view"),
    path('delete/<plant_id>',views.delete_view,name="delete_view"),
    path('detail/<plant_id>',views.detail_view,name="detail_view"),
    path('search/',views.search_view,name="search_view"),
    path('all/',views.all_view,name="all_view"),
]