from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.harvest_trace_anchors_response import HarvestTraceAnchorsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    take: int | Unset = 60,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["take"] = take


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/harvest/trace-anchors",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HarvestTraceAnchorsResponse | None:
    if response.status_code == 200:
        response_200 = HarvestTraceAnchorsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HarvestTraceAnchorsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    take: int | Unset = 60,

) -> Response[HarvestTraceAnchorsResponse]:
    """ Lượt neo có lô của workspace (D7) + lô đã niêm phong chờ lượt tới

    Args:
        take (int | Unset):  Default: 60.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HarvestTraceAnchorsResponse]
     """


    kwargs = _get_kwargs(
        take=take,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    take: int | Unset = 60,

) -> HarvestTraceAnchorsResponse | None:
    """ Lượt neo có lô của workspace (D7) + lô đã niêm phong chờ lượt tới

    Args:
        take (int | Unset):  Default: 60.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HarvestTraceAnchorsResponse
     """


    return sync_detailed(
        client=client,
take=take,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    take: int | Unset = 60,

) -> Response[HarvestTraceAnchorsResponse]:
    """ Lượt neo có lô của workspace (D7) + lô đã niêm phong chờ lượt tới

    Args:
        take (int | Unset):  Default: 60.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HarvestTraceAnchorsResponse]
     """


    kwargs = _get_kwargs(
        take=take,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    take: int | Unset = 60,

) -> HarvestTraceAnchorsResponse | None:
    """ Lượt neo có lô của workspace (D7) + lô đã niêm phong chờ lượt tới

    Args:
        take (int | Unset):  Default: 60.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HarvestTraceAnchorsResponse
     """


    return (await asyncio_detailed(
        client=client,
take=take,

    )).parsed
