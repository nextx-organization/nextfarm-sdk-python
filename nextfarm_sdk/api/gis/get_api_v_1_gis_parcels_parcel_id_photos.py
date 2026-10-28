from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gis_parcel_photo_dto import GisParcelPhotoDto
from ...models.gis_problem_details import GisProblemDetails
from typing import cast
from uuid import UUID



def _get_kwargs(
    parcel_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/gis/parcels/{parcel_id}/photos".format(parcel_id=quote(str(parcel_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GisProblemDetails | list[GisParcelPhotoDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = GisParcelPhotoDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 404:
        response_404 = GisProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GisProblemDetails | list[GisParcelPhotoDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    parcel_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GisProblemDetails | list[GisParcelPhotoDto]]:
    """ Danh sách ảnh của lô thửa

     Trả về danh sách ảnh kèm presigned GET URL (TTL 1 giờ).

    Args:
        parcel_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisProblemDetails | list[GisParcelPhotoDto]]
     """


    kwargs = _get_kwargs(
        parcel_id=parcel_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    parcel_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> GisProblemDetails | list[GisParcelPhotoDto] | None:
    """ Danh sách ảnh của lô thửa

     Trả về danh sách ảnh kèm presigned GET URL (TTL 1 giờ).

    Args:
        parcel_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisProblemDetails | list[GisParcelPhotoDto]
     """


    return sync_detailed(
        parcel_id=parcel_id,
client=client,

    ).parsed

async def asyncio_detailed(
    parcel_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GisProblemDetails | list[GisParcelPhotoDto]]:
    """ Danh sách ảnh của lô thửa

     Trả về danh sách ảnh kèm presigned GET URL (TTL 1 giờ).

    Args:
        parcel_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisProblemDetails | list[GisParcelPhotoDto]]
     """


    kwargs = _get_kwargs(
        parcel_id=parcel_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    parcel_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> GisProblemDetails | list[GisParcelPhotoDto] | None:
    """ Danh sách ảnh của lô thửa

     Trả về danh sách ảnh kèm presigned GET URL (TTL 1 giờ).

    Args:
        parcel_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisProblemDetails | list[GisParcelPhotoDto]
     """


    return (await asyncio_detailed(
        parcel_id=parcel_id,
client=client,

    )).parsed
