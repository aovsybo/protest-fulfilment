from _datetime import datetime
import json
import logging

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from ..service.validation import CRMDealInfoValidator
from ..service.db import save_or_update_crm_deal_info

logger = logging.getLogger(__name__)


class CRMDealInfoView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        validated_data = CRMDealInfoValidator.model_validate(request.data)
        logger.info(
            f"request data: {json.dumps(request.data)}\n"
            f"validated data: {validated_data}\n"
            f"request time: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n"
        )
        # save_or_update_crm_deal_info(validated_data)
        return Response(status=status.HTTP_200_OK)
