from django.urls import path
from main import views
ulrpatterns=[
    path('',views.Index.as_view())
]