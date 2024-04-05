from ..api.serializers import CRMDealInfoSerializer
from ..models import CRMDealInfo
from ..service.validation import CRMDealInfoValidator


def save_crm_deal_info(validated_data: CRMDealInfoValidator):
    serializer = CRMDealInfoSerializer(validated_data)
    if serializer.is_valid():
        serializer.save()


def update_crm_deal_info(validated_data: CRMDealInfoValidator):
    pass
    # TODO: update fields. If there is "status" - check if "checked" or "finished"
