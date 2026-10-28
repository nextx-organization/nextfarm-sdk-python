from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gis_map_layer_list_item_dto_paged_result import GisMapLayerListItemDtoPagedResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    layer_type: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["layerType"] = layer_type

    json_zone_id: str | Unset = UNSET
    if not isinstance(zone_id, Unset):
        json_zone_id = str(zone_id)
    params["zoneId"] = json_zone_id

    params["status"] = status

    params["page"] = page

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/gis/layers",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GisMapLayerListItemDtoPagedResult | None:
    if response.status_code == 200:
        response_200 = GisMapLayerListItemDtoPagedResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GisMapLayerListItemDtoPagedResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    layer_type: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[GisMapLayerListItemDtoPagedResult]:
    """ Danh sách map layers

     Lọc theo layer_type (ndvi/satellite/custom/soil/weather), zone_id, status
    (processing/ready/failed/archived). Phân trang.

    Args:
        layer_type (str | Unset):
        zone_id (UUID | Unset):
        status (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisMapLayerListItemDtoPagedResult]
     """


    kwargs = _get_kwargs(
        layer_type=layer_type,
zone_id=zone_id,
status=status,
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
    layer_type: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> GisMapLayerListItemDtoPagedResult | None:
    """ Danh sách map layers

     Lọc theo layer_type (ndvi/satellite/custom/soil/weather), zone_id, status
    (processing/ready/failed/archived). Phân trang.

    Args:
        layer_type (str | Unset):
        zone_id (UUID | Unset):
        status (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisMapLayerListItemDtoPagedResult
     """


    return sync_detailed(
        client=client,
layer_type=layer_type,
zone_id=zone_id,
status=status,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    layer_type: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[GisMapLayerListItemDtoPagedResult]:
    """ Danh sách map layers

     Lọc theo layer_type (ndvi/satellite/custom/soil/weather), zone_id, status
    (processing/ready/failed/archived). Phân trang.

    Args:
        layer_type (str | Unset):
        zone_id (UUID | Unset):
        status (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisMapLayerListItemDtoPagedResult]
     """


    kwargs = _get_kwargs(
        layer_type=layer_type,
zone_id=zone_id,
status=status,
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
    layer_type: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> GisMapLayerListItemDtoPagedResult | None:
    """ Danh sách map layers

     Lọc theo layer_type (ndvi/satellite/custom/soil/weather), zone_id, status
    (processing/ready/failed/archived). Phân trang.

    Args:
        layer_type (str | Unset):
        zone_id (UUID | Unset):
        status (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisMapLayerListItemDtoPagedResult
     """


    return (await asyncio_detailed(
        client=client,
layer_type=layer_type,
zone_id=zone_id,
status=status,
page=page,
page_size=page_size,

    )).parsed
