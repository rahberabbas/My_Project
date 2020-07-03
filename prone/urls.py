from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('vid/<int:myid>',views.vid,name="Video"),
    # path('add/',views.add,name="Add")
]
