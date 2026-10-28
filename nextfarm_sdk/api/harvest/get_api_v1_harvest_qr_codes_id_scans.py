from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.harvest_qr_scan_series_dto import HarvestQrScanSeriesDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    days: int | Unset = 30,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["days"] = days


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/harvest/qr-codes/{id}/scans".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HarvestQrScanSeriesDto | None:
    if response.status_code == 200:
        response_200 = HarvestQrScanSeriesDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HarvestQrScanSeriesDto]:
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
    days: int | Unset = 30,

) -> Response[HarvestQrScanSeriesDto]:
    """ Lượt quét theo ngày của một mã QR (Q6)

    Args:
        id (UUID):
        days (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HarvestQrScanSeriesDto]
     """


    kwargs = _get_kwargs(
        id=id,
days=days,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,

) -> HarvestQrScanSeriesDto | None:
    """ Lượt quét theo ngày của một mã QR (Q6)

    Args:
        id (UUID):
        days (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HarvestQrScanSeriesDto
     """


    return sync_detailed(
        id=id,
client=client,
days=days,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,

) -> Response[HarvestQrScanSeriesDto]:
    """ Lượt quét theo ngày của một mã QR (Q6)

    Args:
        id (UUID):
        days (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HarvestQrScanSeriesDto]
     """


    kwargs = _get_kwargs(
        id=id,
days=days,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,

) -> HarvestQrScanSeriesDto | None:
    """ Lượt quét theo ngày của một mã QR (Q6)

    Args:
        id (UUID):
        days (int | Unset):  Default: 30.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HarvestQrScanSeriesDto
     """


    return (await asyncio_detailed(
        id=id,
client=client,
days=days,

    )).parsed
