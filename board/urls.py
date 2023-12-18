from django.urls import path

from . import views

app_name = "board"

urlpatterns = [
    path('detail/<int:board_id>/', views.detail, name='detail'),
    path('create/', views.create.as_view(), name='create'),
    path('list/', views.list, name='list'),
    path('bottom/', views.bottom, name='bottom'),
    path('top/', views.top, name='bottom'),
    path('outer/', views.outer, name='bottom'),
]


   