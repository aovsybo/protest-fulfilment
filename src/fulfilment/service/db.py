from ..api.serializers import CRMDealInfoSerializer
from ..models import CRMDealInfo
from ..service.validation import CRMDealInfoValidator


def save_or_update_crm_deal_info(validated_data: CRMDealInfoValidator):
    if CRMDealInfo.objects.filter(id=validated_data.id).exists():
        pass
        # TODO: update fields. If there is "status" - check if checked or finished
    else:
        serializer = CRMDealInfoSerializer(validated_data)
        if serializer.is_valid():
            serializer.save()

