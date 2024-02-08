from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from drf_api_logger import API_LOGGER_SIGNAL
from elasticsearch import Elasticsearch
from .serializers import APILogsModelSerializer
import json

esclient = Elasticsearch("http://localhost:9200")

def listener_one(**kwargs):
    print(kwargs)
    kwargs['headers'] = json.dumps(kwargs['headers'])
    kwargs['body'] = json.dumps(kwargs['body'])
    kwargs['response'] = json.dumps(kwargs['response'])
    kwargs['execution_time'] = '{:.15f}'.format(float(kwargs['execution_time']))
    doc_serializer = APILogsModelSerializer(data=kwargs)

    if doc_serializer.is_valid():
        serialized_data = doc_serializer.validated_data
        
        res = esclient.index(index="shabbirapi3", document=serialized_data)
        print(f"Successfully saved APILogsModel instance with id: {res['_id']}")
    # print("haha")
    else:
    # print("haha2")
        print(f"Error in serializer data: {doc_serializer.errors}")

API_LOGGER_SIGNAL.listen += listener_one

# /api/index
@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        print("GET lol")
        return Response("GET LOL")
    return Response("Not GET")

class PostAPI(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('-updated_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("POST was saved")
            return Response(serializer.data)
        return Response(serializer.errors())
    def patch(self, request):
        foundpost = Post.objects.get(id = request.data['id'])
        serializer = PostSerializer(foundpost, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self, request):
        foundpost = Post.objects.get(id = request.data['id'])
        foundpost.delete()
        return Response("deleted post")

