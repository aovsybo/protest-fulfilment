import requests

from django.conf import settings


def get_headers():
    return {
        "Content-Type": "application/json",
        "Login": settings.FULFILMENT_API_LOGIN,
        "Password": settings.FULFILMENT_API_PASSWORD,
    }


def register_new_order(data: dict):
    url = "https://api.euro-ff.com/NB/hs/exch/v1/order/"
    response = requests.get(
        url=url,
        headers=get_headers(),
        data={"Orders": data},
    )
    return response.json()


def get_order_statuses(order_ids: list[str]):
    url = "https://api.euro-ff.com/NB/hs/exch/v1/status"
    response = requests.get(
        url=url,
        headers=get_headers(),
        data={"Orders": order_ids},
    )
    return response.json()
