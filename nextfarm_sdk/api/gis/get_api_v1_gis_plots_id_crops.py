from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gis_plot_crop_dto import GisPlotCropDto
from ...models.gis_problem_details import GisProblemDetails
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/gis/plots/{id}/crops".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GisProblemDetails | list[GisPlotCropDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = GisPlotCropDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 404:
        response_404 = GisProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GisProblemDetails | list[GisPlotCropDto]]:
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

) -> Response[GisProblemDetails | list[GisPlotCropDto]]:
    """ Các loài trồng trong khu (trồng xen)

     Loài chính đứng đầu (role = main, trùng crop_type_id của khu). Vai trò: main · intercrop (xen) ·
    shade (che bóng) · border (ranh) · temporary (tạm).

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisProblemDetails | list[GisPlotCropDto]]
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

) -> GisProblemDetails | list[GisPlotCropDto] | None:
    """ Các loài trồng trong khu (trồng xen)

     Loài chính đứng đầu (role = main, trùng crop_type_id của khu). Vai trò: main · intercrop (xen) ·
    shade (che bóng) · border (ranh) · temporary (tạm).

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisProblemDetails | list[GisPlotCropDto]
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GisProblemDetails | list[GisPlotCropDto]]:
    """ Các loài trồng trong khu (trồng xen)

     Loài chính đứng đầu (role = main, trùng crop_type_id của khu). Vai trò: main · intercrop (xen) ·
    shade (che bóng) · border (ranh) · temporary (tạm).

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisProblemDetails | list[GisPlotCropDto]]
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

) -> GisProblemDetails | list[GisPlotCropDto] | None:
    """ Các loài trồng trong khu (trồng xen)

     Loài chính đứng đầu (role = main, trùng crop_type_id của khu). Vai trò: main · intercrop (xen) ·
    shade (che bóng) · border (ranh) · temporary (tạm).

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisProblemDetails | list[GisPlotCropDto]
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
