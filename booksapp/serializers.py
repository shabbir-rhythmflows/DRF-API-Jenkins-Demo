from rest_framework import serializers
from .models import Post, APILogsModel2

class PostSerializer(serializers.ModelSerializer):
    
    class Meta: # to link serializer class to a model
        model = Post
        fields = '__all__'
        # exclude = ['created_at', 'updated_at'] # to exclude any particular fields
        
class APILogsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = APILogsModel2
        # fields = '__all__'
        exclude = ['execution_time']