from django.urls import path
from . import views # Instead of importing the entire `views` module
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
]
