from rest_framework import viewsets, permissions
from .serializers import (ProcessorSerializer,
                          ActionsSerializer,
                          OperationsSerializer,
                          AuthorisationsSerializer)

from .models import Processor, Actions, Operations, Authorisations


class ProcessorViewSet(viewsets.ModelViewSet):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Actions.objects.all()
    serializer_class = ActionsSerializer
    permission_classes = [permissions.IsAuthenticated]


class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operations.objects.all()
    serializer_class = OperationsSerializer
    permission_classes = [permissions.IsAuthenticated]


class AuthorisationViewSet(viewsets.ModelViewSet):
    queryset = Authorisations.objects.all()
    serializer_class = AuthorisationsSerializer
    permission_classes = [permissions.IsAuthenticated]
