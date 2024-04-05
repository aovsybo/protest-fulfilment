from datetime import datetime
import json
import logging


logger = logging.getLogger(__name__)


def log_request(request_type, request_data, validated_data):
    logger.info(
        f"{request_type}\n"
        f"request data: {json.dumps(request_data)}\n"
        f"validated data: {validated_data}\n"
        f"request time: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n"
    )
