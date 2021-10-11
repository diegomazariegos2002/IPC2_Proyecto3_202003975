from django.urls import path
from webapp import views # Change 2 - import views of my app

urlpatterns = [ 
    path("", views.hello, name="hello"), #Change 3
]