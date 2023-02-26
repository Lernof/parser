from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import serializers, models, repos
from utils import mixins
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ResourcesViewSet(mixins.ActionSerializerMixin,ModelViewSet):
    ACTION_SERIALIZER = {
        'create': serializers.ResourceCreateSerializer,
    }

    queryset = models.Resource.objects.all()
    serializer_class = serializers.ResourceRetrieveSerializer

class ItemsViewSet(ModelViewSet):
    
    rep: repos.ItemsReposInteface = repos.ItemsReposV1()
    
    queryset = models.Items.objects.all()
    serializer_class = serializers.ItemsCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = serializers.ItemsCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.rep.create_item(request.data)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)