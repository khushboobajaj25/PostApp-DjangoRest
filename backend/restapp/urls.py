from rest_framework import routers
from restapp import views

route = routers.DefaultRouter()

route.register('post', views.PostViewSet, basename="post")


urlpatterns = route.urls
