from django.urls import path
from .views import All,Detail

urlpatterns = [
    path('all',All,name='all'),
    path('details/<int:pk>',Detail.as_view(),name='details')
    
]



