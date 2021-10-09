from rest_framework import serializers
from restapp import models
from rest_framework.response import Response

class PostSerailizer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('id','title','description','created_at','updated_at')
        
