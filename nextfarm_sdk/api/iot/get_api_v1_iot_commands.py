from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.iot_device_command_dto_paged_result import IotDeviceCommandDtoPagedResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    device_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_device_id: str | Unset = UNSET
    if not isinstance(device_id, Unset):
        json_device_id = str(device_id)
    params["deviceId"] = json_device_id

    params["page"] = page

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/iot/commands",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IotDeviceCommandDtoPagedResult | None:
    if response.status_code == 200:
        response_200 = IotDeviceCommandDtoPagedResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[IotDeviceCommandDtoPagedResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    device_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,

) -> Response[IotDeviceCommandDtoPagedResult]:
    """ Danh sách lệnh thiết bị

     Lọc theo deviceId (tùy chọn). Phân trang.

    Args:
        device_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IotDeviceCommandDtoPagedResult]
     """


    kwargs = _get_kwargs(
        device_id=device_id,
page=page,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    device_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,

) -> IotDeviceCommandDtoPagedResult | None:
    """ Danh sách lệnh thiết bị

     Lọc theo deviceId (tùy chọn). Phân trang.

    Args:
        device_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IotDeviceCommandDtoPagedResult
     """


    return sync_detailed(
        client=client,
device_id=device_id,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    device_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,

) -> Response[IotDeviceCommandDtoPagedResult]:
    """ Danh sách lệnh thiết bị

     Lọc theo deviceId (tùy chọn). Phân trang.

    Args:
        device_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IotDeviceCommandDtoPagedResult]
     """


    kwargs = _get_kwargs(
        device_id=device_id,
page=page,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    device_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,

) -> IotDeviceCommandDtoPagedResult | None:
    """ Danh sách lệnh thiết bị

     Lọc theo deviceId (tùy chọn). Phân trang.

    Args:
        device_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IotDeviceCommandDtoPagedResult
     """


    return (await asyncio_detailed(
        client=client,
device_id=device_id,
page=page,
page_size=page_size,

    )).parsed
