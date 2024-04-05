from rest_framework import serializers

from ..models import CRMDealInfo


class CRMDealInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMDealInfo
        fields = '__all__'
