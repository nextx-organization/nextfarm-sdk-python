from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gis_care_preview_dto import GisCarePreviewDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    year: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["year"] = year


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/gis/care-schedules/{id}/calendar".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GisCarePreviewDto | None:
    if response.status_code == 200:
        response_200 = GisCarePreviewDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GisCarePreviewDto]:
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
    year: int | Unset = UNSET,

) -> Response[GisCarePreviewDto]:
    """ Lịch cả năm của một kích hoạt

    Args:
        id (UUID):
        year (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisCarePreviewDto]
     """


    kwargs = _get_kwargs(
        id=id,
year=year,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,

) -> GisCarePreviewDto | None:
    """ Lịch cả năm của một kích hoạt

    Args:
        id (UUID):
        year (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisCarePreviewDto
     """


    return sync_detailed(
        id=id,
client=client,
year=year,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,

) -> Response[GisCarePreviewDto]:
    """ Lịch cả năm của một kích hoạt

    Args:
        id (UUID):
        year (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisCarePreviewDto]
     """


    kwargs = _get_kwargs(
        id=id,
year=year,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    year: int | Unset = UNSET,

) -> GisCarePreviewDto | None:
    """ Lịch cả năm của một kích hoạt

    Args:
        id (UUID):
        year (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisCarePreviewDto
     """


    return (await asyncio_detailed(
        id=id,
client=client,
year=year,

    )).parsed
