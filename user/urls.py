from django.urls import path
from .views import Index

urlpatterns = [
    path('v1/user/', Index.as_view(), name='index'),
]