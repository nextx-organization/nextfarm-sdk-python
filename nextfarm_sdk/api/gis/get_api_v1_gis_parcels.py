from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gis_parcel_list_item_dto_paged_result import GisParcelListItemDtoPagedResult
from ...models.gis_problem_details import GisProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    bbox: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
    owner_id: UUID | Unset = UNSET,
    crop_type_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    deleted: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["bbox"] = bbox

    json_zone_id: str | Unset = UNSET
    if not isinstance(zone_id, Unset):
        json_zone_id = str(zone_id)
    params["zoneId"] = json_zone_id

    json_owner_id: str | Unset = UNSET
    if not isinstance(owner_id, Unset):
        json_owner_id = str(owner_id)
    params["ownerId"] = json_owner_id

    json_crop_type_id: str | Unset = UNSET
    if not isinstance(crop_type_id, Unset):
        json_crop_type_id = str(crop_type_id)
    params["cropTypeId"] = json_crop_type_id

    params["status"] = status

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id

    params["page"] = page

    params["pageSize"] = page_size

    params["deleted"] = deleted


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/gis/parcels",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GisParcelListItemDtoPagedResult | GisProblemDetails | None:
    if response.status_code == 200:
        response_200 = GisParcelListItemDtoPagedResult.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GisProblemDetails.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GisParcelListItemDtoPagedResult | GisProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    bbox: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
    owner_id: UUID | Unset = UNSET,
    crop_type_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    deleted: bool | Unset = False,

) -> Response[GisParcelListItemDtoPagedResult | GisProblemDetails]:
    """ Danh sách lô thửa

     Lọc theo bbox (minLon,minLat,maxLon,maxLat), zoneId, ownerId, cropTypeId, status, branchId. Phân
    trang. Bbox max 2°×2°, tối đa 1000 results.

    Args:
        bbox (str | Unset):
        zone_id (UUID | Unset):
        owner_id (UUID | Unset):
        crop_type_id (UUID | Unset):
        status (str | Unset):
        branch_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        deleted (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisParcelListItemDtoPagedResult | GisProblemDetails]
     """


    kwargs = _get_kwargs(
        bbox=bbox,
zone_id=zone_id,
owner_id=owner_id,
crop_type_id=crop_type_id,
status=status,
branch_id=branch_id,
page=page,
page_size=page_size,
deleted=deleted,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    bbox: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
    owner_id: UUID | Unset = UNSET,
    crop_type_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    deleted: bool | Unset = False,

) -> GisParcelListItemDtoPagedResult | GisProblemDetails | None:
    """ Danh sách lô thửa

     Lọc theo bbox (minLon,minLat,maxLon,maxLat), zoneId, ownerId, cropTypeId, status, branchId. Phân
    trang. Bbox max 2°×2°, tối đa 1000 results.

    Args:
        bbox (str | Unset):
        zone_id (UUID | Unset):
        owner_id (UUID | Unset):
        crop_type_id (UUID | Unset):
        status (str | Unset):
        branch_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        deleted (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisParcelListItemDtoPagedResult | GisProblemDetails
     """


    return sync_detailed(
        client=client,
bbox=bbox,
zone_id=zone_id,
owner_id=owner_id,
crop_type_id=crop_type_id,
status=status,
branch_id=branch_id,
page=page,
page_size=page_size,
deleted=deleted,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    bbox: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
    owner_id: UUID | Unset = UNSET,
    crop_type_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    deleted: bool | Unset = False,

) -> Response[GisParcelListItemDtoPagedResult | GisProblemDetails]:
    """ Danh sách lô thửa

     Lọc theo bbox (minLon,minLat,maxLon,maxLat), zoneId, ownerId, cropTypeId, status, branchId. Phân
    trang. Bbox max 2°×2°, tối đa 1000 results.

    Args:
        bbox (str | Unset):
        zone_id (UUID | Unset):
        owner_id (UUID | Unset):
        crop_type_id (UUID | Unset):
        status (str | Unset):
        branch_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        deleted (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisParcelListItemDtoPagedResult | GisProblemDetails]
     """


    kwargs = _get_kwargs(
        bbox=bbox,
zone_id=zone_id,
owner_id=owner_id,
crop_type_id=crop_type_id,
status=status,
branch_id=branch_id,
page=page,
page_size=page_size,
deleted=deleted,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    bbox: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
    owner_id: UUID | Unset = UNSET,
    crop_type_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    deleted: bool | Unset = False,

) -> GisParcelListItemDtoPagedResult | GisProblemDetails | None:
    """ Danh sách lô thửa

     Lọc theo bbox (minLon,minLat,maxLon,maxLat), zoneId, ownerId, cropTypeId, status, branchId. Phân
    trang. Bbox max 2°×2°, tối đa 1000 results.

    Args:
        bbox (str | Unset):
        zone_id (UUID | Unset):
        owner_id (UUID | Unset):
        crop_type_id (UUID | Unset):
        status (str | Unset):
        branch_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        deleted (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisParcelListItemDtoPagedResult | GisProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
bbox=bbox,
zone_id=zone_id,
owner_id=owner_id,
crop_type_id=crop_type_id,
status=status,
branch_id=branch_id,
page=page,
page_size=page_size,
deleted=deleted,

    )).parsed
