from .models import Actions, Operations, Authorisations
from rest_framework import serializers


class ActionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actions
        fields = ['action']


class OperationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operations
        fields = ['operation', 'details']


class AuthorisationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Authorisations
        fields = ['actions', 'operation']