""" URL mappings for the User API """

from django.urls import path
from . import views
from . import routers

app_name = 'UserAuth'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]

urlpatterns += routers.router.urls
