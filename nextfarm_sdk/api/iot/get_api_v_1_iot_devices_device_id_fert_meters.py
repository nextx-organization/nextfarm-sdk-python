from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.iot_device_fert_meters_dto import IotDeviceFertMetersDto
from ...models.iot_problem_details import IotProblemDetails
from typing import cast
from uuid import UUID



def _get_kwargs(
    device_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/iot/devices/{device_id}/fert-meters".format(device_id=quote(str(device_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IotDeviceFertMetersDto | IotProblemDetails | None:
    if response.status_code == 200:
        response_200 = IotDeviceFertMetersDto.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = IotProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[IotDeviceFertMetersDto | IotProblemDetails]:
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

) -> Response[IotDeviceFertMetersDto | IotProblemDetails]:
    """ Đồng hồ các bồn phân: chỗ cắm, hệ số bo đang dùng, và số đếm xung thô mới nhất

     pulse_at = null nghĩa là CHƯA BAO GIỜ nhận được xung nào từ thiết bị này. Trong mỗi kênh: pulse = -1
    là không có đồng hồ / không đọc được · 0 là CÓ đồng hồ mà chưa quay · null là bo chưa gửi trường đó.
    Ba giá trị, ba nghĩa khác nhau.

    Args:
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IotDeviceFertMetersDto | IotProblemDetails]
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

) -> IotDeviceFertMetersDto | IotProblemDetails | None:
    """ Đồng hồ các bồn phân: chỗ cắm, hệ số bo đang dùng, và số đếm xung thô mới nhất

     pulse_at = null nghĩa là CHƯA BAO GIỜ nhận được xung nào từ thiết bị này. Trong mỗi kênh: pulse = -1
    là không có đồng hồ / không đọc được · 0 là CÓ đồng hồ mà chưa quay · null là bo chưa gửi trường đó.
    Ba giá trị, ba nghĩa khác nhau.

    Args:
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IotDeviceFertMetersDto | IotProblemDetails
     """


    return sync_detailed(
        device_id=device_id,
client=client,

    ).parsed

async def asyncio_detailed(
    device_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[IotDeviceFertMetersDto | IotProblemDetails]:
    """ Đồng hồ các bồn phân: chỗ cắm, hệ số bo đang dùng, và số đếm xung thô mới nhất

     pulse_at = null nghĩa là CHƯA BAO GIỜ nhận được xung nào từ thiết bị này. Trong mỗi kênh: pulse = -1
    là không có đồng hồ / không đọc được · 0 là CÓ đồng hồ mà chưa quay · null là bo chưa gửi trường đó.
    Ba giá trị, ba nghĩa khác nhau.

    Args:
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IotDeviceFertMetersDto | IotProblemDetails]
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

) -> IotDeviceFertMetersDto | IotProblemDetails | None:
    """ Đồng hồ các bồn phân: chỗ cắm, hệ số bo đang dùng, và số đếm xung thô mới nhất

     pulse_at = null nghĩa là CHƯA BAO GIỜ nhận được xung nào từ thiết bị này. Trong mỗi kênh: pulse = -1
    là không có đồng hồ / không đọc được · 0 là CÓ đồng hồ mà chưa quay · null là bo chưa gửi trường đó.
    Ba giá trị, ba nghĩa khác nhau.

    Args:
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IotDeviceFertMetersDto | IotProblemDetails
     """


    return (await asyncio_detailed(
        device_id=device_id,
client=client,

    )).parsed
