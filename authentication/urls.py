import imp
from django.urls import path
from . import views


urlpatterns=[
    path('',views.helloAuthView.as_view(),name="HelloAuth")
]