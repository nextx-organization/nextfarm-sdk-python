from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.iot_sensor_reading_dto import IotSensorReadingDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    zone_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_zone_id: str | Unset = UNSET
    if not isinstance(zone_id, Unset):
        json_zone_id = str(zone_id)
    params["zoneId"] = json_zone_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/iot/sensor-readings/latest",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[IotSensorReadingDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = IotSensorReadingDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[IotSensorReadingDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    zone_id: UUID | Unset = UNSET,

) -> Response[list[IotSensorReadingDto]]:
    """ Giá trị mới nhất của từng thiết bị (30 phút gần nhất)

     Dùng cho Dashboard thời gian thực. Lọc theo zoneId tùy chọn.

    Args:
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[IotSensorReadingDto]]
     """


    kwargs = _get_kwargs(
        zone_id=zone_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    zone_id: UUID | Unset = UNSET,

) -> list[IotSensorReadingDto] | None:
    """ Giá trị mới nhất của từng thiết bị (30 phút gần nhất)

     Dùng cho Dashboard thời gian thực. Lọc theo zoneId tùy chọn.

    Args:
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[IotSensorReadingDto]
     """


    return sync_detailed(
        client=client,
zone_id=zone_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    zone_id: UUID | Unset = UNSET,

) -> Response[list[IotSensorReadingDto]]:
    """ Giá trị mới nhất của từng thiết bị (30 phút gần nhất)

     Dùng cho Dashboard thời gian thực. Lọc theo zoneId tùy chọn.

    Args:
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[IotSensorReadingDto]]
     """


    kwargs = _get_kwargs(
        zone_id=zone_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    zone_id: UUID | Unset = UNSET,

) -> list[IotSensorReadingDto] | None:
    """ Giá trị mới nhất của từng thiết bị (30 phút gần nhất)

     Dùng cho Dashboard thời gian thực. Lọc theo zoneId tùy chọn.

    Args:
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[IotSensorReadingDto]
     """


    return (await asyncio_detailed(
        client=client,
zone_id=zone_id,

    )).parsed
