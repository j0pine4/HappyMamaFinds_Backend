from rest_framework.routers import DefaultRouter
from . import views

blogRouter = DefaultRouter()
blogRouter.register('', views.blogView, basename='blog')
urlpatterns = blogRouter.urls
