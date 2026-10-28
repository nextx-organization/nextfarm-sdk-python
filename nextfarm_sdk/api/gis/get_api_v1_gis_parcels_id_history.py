from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gis_parcel_history_item_dto_paged_result import GisParcelHistoryItemDtoPagedResult
from ...models.gis_problem_details import GisProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/gis/parcels/{id}/history".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GisParcelHistoryItemDtoPagedResult | GisProblemDetails | None:
    if response.status_code == 200:
        response_200 = GisParcelHistoryItemDtoPagedResult.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = GisProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GisParcelHistoryItemDtoPagedResult | GisProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[GisParcelHistoryItemDtoPagedResult | GisProblemDetails]:
    """ Lịch sử thay đổi parcel

     Audit trail mọi thay đổi (created/boundary-updated/owner-changed/crop-type-changed/status-
    changed/deleted). Sắp xếp mới nhất trước.

    Args:
        id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisParcelHistoryItemDtoPagedResult | GisProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,
page=page,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> GisParcelHistoryItemDtoPagedResult | GisProblemDetails | None:
    """ Lịch sử thay đổi parcel

     Audit trail mọi thay đổi (created/boundary-updated/owner-changed/crop-type-changed/status-
    changed/deleted). Sắp xếp mới nhất trước.

    Args:
        id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisParcelHistoryItemDtoPagedResult | GisProblemDetails
     """


    return sync_detailed(
        id=id,
client=client,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[GisParcelHistoryItemDtoPagedResult | GisProblemDetails]:
    """ Lịch sử thay đổi parcel

     Audit trail mọi thay đổi (created/boundary-updated/owner-changed/crop-type-changed/status-
    changed/deleted). Sắp xếp mới nhất trước.

    Args:
        id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisParcelHistoryItemDtoPagedResult | GisProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,
page=page,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> GisParcelHistoryItemDtoPagedResult | GisProblemDetails | None:
    """ Lịch sử thay đổi parcel

     Audit trail mọi thay đổi (created/boundary-updated/owner-changed/crop-type-changed/status-
    changed/deleted). Sắp xếp mới nhất trước.

    Args:
        id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisParcelHistoryItemDtoPagedResult | GisProblemDetails
     """


    return (await asyncio_detailed(
        id=id,
client=client,
page=page,
page_size=page_size,

    )).parsed
