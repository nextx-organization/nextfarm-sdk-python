from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gis_gis_search_result import GisGisSearchResult
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    limit: int | Unset = 8,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/gis/search",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GisGisSearchResult | None:
    if response.status_code == 200:
        response_200 = GisGisSearchResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GisGisSearchResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = 8,

) -> Response[GisGisSearchResult]:
    """ Tìm thửa, mùa vụ, nông dân, vùng

     Không phân biệt dấu ("ca phe" khớp "Cà phê"). Dưới 2 ký tự trả rỗng. Mỗi nhóm tối đa `limit` (1–20,
    mặc định 8), đã lọc theo quyền + vùng được phép.

    Args:
        q (str | Unset):
        limit (int | Unset):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisGisSearchResult]
     """


    kwargs = _get_kwargs(
        q=q,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = 8,

) -> GisGisSearchResult | None:
    """ Tìm thửa, mùa vụ, nông dân, vùng

     Không phân biệt dấu ("ca phe" khớp "Cà phê"). Dưới 2 ký tự trả rỗng. Mỗi nhóm tối đa `limit` (1–20,
    mặc định 8), đã lọc theo quyền + vùng được phép.

    Args:
        q (str | Unset):
        limit (int | Unset):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisGisSearchResult
     """


    return sync_detailed(
        client=client,
q=q,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = 8,

) -> Response[GisGisSearchResult]:
    """ Tìm thửa, mùa vụ, nông dân, vùng

     Không phân biệt dấu ("ca phe" khớp "Cà phê"). Dưới 2 ký tự trả rỗng. Mỗi nhóm tối đa `limit` (1–20,
    mặc định 8), đã lọc theo quyền + vùng được phép.

    Args:
        q (str | Unset):
        limit (int | Unset):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisGisSearchResult]
     """


    kwargs = _get_kwargs(
        q=q,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = 8,

) -> GisGisSearchResult | None:
    """ Tìm thửa, mùa vụ, nông dân, vùng

     Không phân biệt dấu ("ca phe" khớp "Cà phê"). Dưới 2 ký tự trả rỗng. Mỗi nhóm tối đa `limit` (1–20,
    mặc định 8), đã lọc theo quyền + vùng được phép.

    Args:
        q (str | Unset):
        limit (int | Unset):  Default: 8.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisGisSearchResult
     """


    return (await asyncio_detailed(
        client=client,
q=q,
limit=limit,

    )).parsed
