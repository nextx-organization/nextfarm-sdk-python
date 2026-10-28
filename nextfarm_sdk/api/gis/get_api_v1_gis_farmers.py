from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gis_farmer_list_item_dto_paged_result import GisFarmerListItemDtoPagedResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    zone_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    deleted: bool | Unset = False,
    group_id: UUID | Unset = UNSET,
    member_type: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_zone_id: str | Unset = UNSET
    if not isinstance(zone_id, Unset):
        json_zone_id = str(zone_id)
    params["zoneId"] = json_zone_id

    params["page"] = page

    params["pageSize"] = page_size

    params["deleted"] = deleted

    json_group_id: str | Unset = UNSET
    if not isinstance(group_id, Unset):
        json_group_id = str(group_id)
    params["groupId"] = json_group_id

    params["memberType"] = member_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/gis/farmers",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GisFarmerListItemDtoPagedResult | None:
    if response.status_code == 200:
        response_200 = GisFarmerListItemDtoPagedResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GisFarmerListItemDtoPagedResult]:
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
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    deleted: bool | Unset = False,
    group_id: UUID | Unset = UNSET,
    member_type: str | Unset = UNSET,

) -> Response[GisFarmerListItemDtoPagedResult]:
    """ Danh sách nông dân

     Lọc theo zone_id. Phân trang.

    Args:
        zone_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        deleted (bool | Unset):  Default: False.
        group_id (UUID | Unset):
        member_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisFarmerListItemDtoPagedResult]
     """


    kwargs = _get_kwargs(
        zone_id=zone_id,
page=page,
page_size=page_size,
deleted=deleted,
group_id=group_id,
member_type=member_type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    zone_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    deleted: bool | Unset = False,
    group_id: UUID | Unset = UNSET,
    member_type: str | Unset = UNSET,

) -> GisFarmerListItemDtoPagedResult | None:
    """ Danh sách nông dân

     Lọc theo zone_id. Phân trang.

    Args:
        zone_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        deleted (bool | Unset):  Default: False.
        group_id (UUID | Unset):
        member_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisFarmerListItemDtoPagedResult
     """


    return sync_detailed(
        client=client,
zone_id=zone_id,
page=page,
page_size=page_size,
deleted=deleted,
group_id=group_id,
member_type=member_type,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    zone_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    deleted: bool | Unset = False,
    group_id: UUID | Unset = UNSET,
    member_type: str | Unset = UNSET,

) -> Response[GisFarmerListItemDtoPagedResult]:
    """ Danh sách nông dân

     Lọc theo zone_id. Phân trang.

    Args:
        zone_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        deleted (bool | Unset):  Default: False.
        group_id (UUID | Unset):
        member_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisFarmerListItemDtoPagedResult]
     """


    kwargs = _get_kwargs(
        zone_id=zone_id,
page=page,
page_size=page_size,
deleted=deleted,
group_id=group_id,
member_type=member_type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    zone_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    deleted: bool | Unset = False,
    group_id: UUID | Unset = UNSET,
    member_type: str | Unset = UNSET,

) -> GisFarmerListItemDtoPagedResult | None:
    """ Danh sách nông dân

     Lọc theo zone_id. Phân trang.

    Args:
        zone_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        deleted (bool | Unset):  Default: False.
        group_id (UUID | Unset):
        member_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisFarmerListItemDtoPagedResult
     """


    return (await asyncio_detailed(
        client=client,
zone_id=zone_id,
page=page,
page_size=page_size,
deleted=deleted,
group_id=group_id,
member_type=member_type,

    )).parsed
