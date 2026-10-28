from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.iot_device_irrigation_output_dto import IotDeviceIrrigationOutputDto
from typing import cast
from uuid import UUID



def _get_kwargs(
    device_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/iot/devices/{device_id}/output-config/irrigation".format(device_id=quote(str(device_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[IotDeviceIrrigationOutputDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = IotDeviceIrrigationOutputDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[IotDeviceIrrigationOutputDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    device_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[IotDeviceIrrigationOutputDto]]:
    """ Cấu hình hệ tưới đã gán: bơm/van vùng/van phân bón kể cả van Denso (đọc bản backend đã persist từ
    echo irr_out — không phụ thuộc realtime)

    Args:
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[IotDeviceIrrigationOutputDto]]
     """


    kwargs = _get_kwargs(
        device_id=device_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    device_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> list[IotDeviceIrrigationOutputDto] | None:
    """ Cấu hình hệ tưới đã gán: bơm/van vùng/van phân bón kể cả van Denso (đọc bản backend đã persist từ
    echo irr_out — không phụ thuộc realtime)

    Args:
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[IotDeviceIrrigationOutputDto]
     """


    return sync_detailed(
        device_id=device_id,
client=client,

    ).parsed

async def asyncio_detailed(
    device_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[IotDeviceIrrigationOutputDto]]:
    """ Cấu hình hệ tưới đã gán: bơm/van vùng/van phân bón kể cả van Denso (đọc bản backend đã persist từ
    echo irr_out — không phụ thuộc realtime)

    Args:
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[IotDeviceIrrigationOutputDto]]
     """


    kwargs = _get_kwargs(
        device_id=device_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    device_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> list[IotDeviceIrrigationOutputDto] | None:
    """ Cấu hình hệ tưới đã gán: bơm/van vùng/van phân bón kể cả van Denso (đọc bản backend đã persist từ
    echo irr_out — không phụ thuộc realtime)

    Args:
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[IotDeviceIrrigationOutputDto]
     """


    return (await asyncio_detailed(
        device_id=device_id,
client=client,

    )).parsed
