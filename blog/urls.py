from django.urls import path
from . import views
from . import routers

urlpatterns = [
    path('featured', views.FeaturedBlogsView.as_view()),
    path('latest', views.LatestBlogView.as_view())
]

urlpatterns += routers.blogRouter.urls