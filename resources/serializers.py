from rest_framework import serializers
from . import models


class ResourceCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Resource
        fields = (
            'resource_name',
            'resource_url',
            'top_tag',
            'bottom_tag',
            'title_cut',
            'date_cut',
        )

class ResourceRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Resource
        fields = '__all__'

class ItemsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Items
        fields = (
            'res_id',
        )