from rest_framework import viewsets
from restapp import serailizers
from restapp import models

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serailizers.PostSerailizer
