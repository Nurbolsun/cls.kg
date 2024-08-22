from rest_framework import serializers
from .models import *


class BranchImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = BranchImage
        fields = ['image_url']

    def get_image_url(self, obj):
        return obj.image_url if obj.image else ''


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = 'name'


class BranchSerializer(serializers.ModelSerializer):
    images = BranchImageSerializer(many=True)

    class Meta:
        model = Branch
        fields = ('id', 'name', 'description', 'region', 'address', 'time_work', 'images')
