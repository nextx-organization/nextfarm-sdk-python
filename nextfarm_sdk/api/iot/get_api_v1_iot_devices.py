from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.iot_device_list_item_dto_paged_result import IotDeviceListItemDtoPagedResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    parcel_id: UUID | Unset = UNSET,
    unassigned: bool | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["status"] = status

    params["page"] = page

    params["pageSize"] = page_size

    json_parcel_id: str | Unset = UNSET
    if not isinstance(parcel_id, Unset):
        json_parcel_id = str(parcel_id)
    params["parcelId"] = json_parcel_id

    params["unassigned"] = unassigned

    json_zone_id: str | Unset = UNSET
    if not isinstance(zone_id, Unset):
        json_zone_id = str(zone_id)
    params["zoneId"] = json_zone_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/iot/devices",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IotDeviceListItemDtoPagedResult | None:
    if response.status_code == 200:
        response_200 = IotDeviceListItemDtoPagedResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[IotDeviceListItemDtoPagedResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    parcel_id: UUID | Unset = UNSET,
    unassigned: bool | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,

) -> Response[IotDeviceListItemDtoPagedResult]:
    """ Danh sách thiết bị IoT

     Lọc theo status. Phân trang.

    Args:
        status (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        parcel_id (UUID | Unset):
        unassigned (bool | Unset):
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IotDeviceListItemDtoPagedResult]
     """


    kwargs = _get_kwargs(
        status=status,
page=page,
page_size=page_size,
parcel_id=parcel_id,
unassigned=unassigned,
zone_id=zone_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    parcel_id: UUID | Unset = UNSET,
    unassigned: bool | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,

) -> IotDeviceListItemDtoPagedResult | None:
    """ Danh sách thiết bị IoT

     Lọc theo status. Phân trang.

    Args:
        status (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        parcel_id (UUID | Unset):
        unassigned (bool | Unset):
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IotDeviceListItemDtoPagedResult
     """


    return sync_detailed(
        client=client,
status=status,
page=page,
page_size=page_size,
parcel_id=parcel_id,
unassigned=unassigned,
zone_id=zone_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    parcel_id: UUID | Unset = UNSET,
    unassigned: bool | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,

) -> Response[IotDeviceListItemDtoPagedResult]:
    """ Danh sách thiết bị IoT

     Lọc theo status. Phân trang.

    Args:
        status (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        parcel_id (UUID | Unset):
        unassigned (bool | Unset):
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IotDeviceListItemDtoPagedResult]
     """


    kwargs = _get_kwargs(
        status=status,
page=page,
page_size=page_size,
parcel_id=parcel_id,
unassigned=unassigned,
zone_id=zone_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    parcel_id: UUID | Unset = UNSET,
    unassigned: bool | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,

) -> IotDeviceListItemDtoPagedResult | None:
    """ Danh sách thiết bị IoT

     Lọc theo status. Phân trang.

    Args:
        status (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        parcel_id (UUID | Unset):
        unassigned (bool | Unset):
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IotDeviceListItemDtoPagedResult
     """


    return (await asyncio_detailed(
        client=client,
status=status,
page=page,
page_size=page_size,
parcel_id=parcel_id,
unassigned=unassigned,
zone_id=zone_id,

    )).parsed
