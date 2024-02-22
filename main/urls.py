from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', welcome, name='welcome'),
    path('credit', credit_view, name='credit_view'),
    path('credit/<int:id>', credit_edit, name='credit')
]