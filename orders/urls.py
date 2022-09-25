from django.urls import path
from . import views


urlpatterns=[
    path('',views.helloOrderView.as_view(),name="HelloAuth")
]