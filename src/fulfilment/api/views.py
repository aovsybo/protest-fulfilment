from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from ..service.validation import CRMDealInfoValidator
from ..service.db import save_crm_deal_info, update_crm_deal_info
from ..service.logger import log_request


class CRMDealInfoCreateView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        """
        Принимает данные новосозданной сделки
        """
        validated_data = CRMDealInfoValidator.model_validate(request.data)
        log_request("CREATE", request.data, validated_data)
        save_crm_deal_info(validated_data)
        return Response(status=status.HTTP_200_OK)


class CRMDealInfoUpdateView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        """
        Принимает обновленные данные ранее созданной сделки
        """
        validated_data = CRMDealInfoValidator.model_validate(request.data)
        log_request("UPDATE", request.data, validated_data)
        update_crm_deal_info(validated_data)
        return Response(status=status.HTTP_200_OK)
