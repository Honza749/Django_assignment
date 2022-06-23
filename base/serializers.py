from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = item
        fields = '__all__'
