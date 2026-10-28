from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gis_parcel_detail_dto import GisParcelDetailDto
from ...models.gis_problem_details import GisProblemDetails
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/gis/parcels/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GisParcelDetailDto | GisProblemDetails | None:
    if response.status_code == 200:
        response_200 = GisParcelDetailDto.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = GisProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GisParcelDetailDto | GisProblemDetails]:
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

) -> Response[GisParcelDetailDto | GisProblemDetails]:
    """ Chi tiết lô thửa

     Trả về thông tin đầy đủ gồm GeoJSON boundary + nested zone/owner/crop_type + ndvi_history.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisParcelDetailDto | GisProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> GisParcelDetailDto | GisProblemDetails | None:
    """ Chi tiết lô thửa

     Trả về thông tin đầy đủ gồm GeoJSON boundary + nested zone/owner/crop_type + ndvi_history.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisParcelDetailDto | GisProblemDetails
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GisParcelDetailDto | GisProblemDetails]:
    """ Chi tiết lô thửa

     Trả về thông tin đầy đủ gồm GeoJSON boundary + nested zone/owner/crop_type + ndvi_history.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisParcelDetailDto | GisProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> GisParcelDetailDto | GisProblemDetails | None:
    """ Chi tiết lô thửa

     Trả về thông tin đầy đủ gồm GeoJSON boundary + nested zone/owner/crop_type + ndvi_history.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisParcelDetailDto | GisProblemDetails
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
