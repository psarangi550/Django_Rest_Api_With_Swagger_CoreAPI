from django.shortcuts import render
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import WFMTTASKMODEL
from .serializers import WFMTModelSerializer

class WFMTAPIVIEWSETS(ModelViewSet):
    queryset = WFMTTASKMODEL.objects.all()
    serializer_class = WFMTModelSerializer
    