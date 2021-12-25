from rest_framework.serializers import ModelSerializer
from .models import WFMTTASKMODEL
class WFMTModelSerializer(ModelSerializer):
    class Meta:
        model=WFMTTASKMODEL
        fields="__all__"
