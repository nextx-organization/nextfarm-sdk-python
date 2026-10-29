from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gis_zone_list_item_dto_paged_result import GisZoneListItemDtoPagedResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    zone_type: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
    deleted: bool | Unset = False,
    include_stats: bool | Unset = False,
    branch_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["zone_type"] = zone_type

    params["page"] = page

    params["page_size"] = page_size

    params["deleted"] = deleted

    params["include_stats"] = include_stats

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branch_id"] = json_branch_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/gis/zones",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GisZoneListItemDtoPagedResult | None:
    if response.status_code == 200:
        response_200 = GisZoneListItemDtoPagedResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GisZoneListItemDtoPagedResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    zone_type: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
    deleted: bool | Unset = False,
    include_stats: bool | Unset = False,
    branch_id: UUID | Unset = UNSET,

) -> Response[GisZoneListItemDtoPagedResult]:
    """ Danh sách zones

     Lọc theo zone_type (province/district/commune/material_zone). Phân trang.

    Args:
        zone_type (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 100.
        deleted (bool | Unset):  Default: False.
        include_stats (bool | Unset):  Default: False.
        branch_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisZoneListItemDtoPagedResult]
     """


    kwargs = _get_kwargs(
        zone_type=zone_type,
page=page,
page_size=page_size,
deleted=deleted,
include_stats=include_stats,
branch_id=branch_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    zone_type: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
    deleted: bool | Unset = False,
    include_stats: bool | Unset = False,
    branch_id: UUID | Unset = UNSET,

) -> GisZoneListItemDtoPagedResult | None:
    """ Danh sách zones

     Lọc theo zone_type (province/district/commune/material_zone). Phân trang.

    Args:
        zone_type (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 100.
        deleted (bool | Unset):  Default: False.
        include_stats (bool | Unset):  Default: False.
        branch_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisZoneListItemDtoPagedResult
     """


    return sync_detailed(
        client=client,
zone_type=zone_type,
page=page,
page_size=page_size,
deleted=deleted,
include_stats=include_stats,
branch_id=branch_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    zone_type: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
    deleted: bool | Unset = False,
    include_stats: bool | Unset = False,
    branch_id: UUID | Unset = UNSET,

) -> Response[GisZoneListItemDtoPagedResult]:
    """ Danh sách zones

     Lọc theo zone_type (province/district/commune/material_zone). Phân trang.

    Args:
        zone_type (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 100.
        deleted (bool | Unset):  Default: False.
        include_stats (bool | Unset):  Default: False.
        branch_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisZoneListItemDtoPagedResult]
     """


    kwargs = _get_kwargs(
        zone_type=zone_type,
page=page,
page_size=page_size,
deleted=deleted,
include_stats=include_stats,
branch_id=branch_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    zone_type: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 100,
    deleted: bool | Unset = False,
    include_stats: bool | Unset = False,
    branch_id: UUID | Unset = UNSET,

) -> GisZoneListItemDtoPagedResult | None:
    """ Danh sách zones

     Lọc theo zone_type (province/district/commune/material_zone). Phân trang.

    Args:
        zone_type (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 100.
        deleted (bool | Unset):  Default: False.
        include_stats (bool | Unset):  Default: False.
        branch_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisZoneListItemDtoPagedResult
     """


    return (await asyncio_detailed(
        client=client,
zone_type=zone_type,
page=page,
page_size=page_size,
deleted=deleted,
include_stats=include_stats,
branch_id=branch_id,

    )).parsed
