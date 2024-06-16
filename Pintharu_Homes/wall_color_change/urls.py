from django.urls import path
from .  import views

urlpatterns = [
    path('changecolor/', views.color_change, name='color-change'),
    # Other paths for your app's views can be defined here
]