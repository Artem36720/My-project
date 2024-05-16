from django.urls import path
from .views import index, Inkup

urlpatterns = [
    path('hello/', index),
    path('<int:my_id>/', Inkup,name='retail'),
    
]
