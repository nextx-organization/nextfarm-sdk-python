from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gis_crop_variety_dto import GisCropVarietyDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    kind: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["kind"] = kind


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/gis/crop-types/{id}/varieties".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[GisCropVarietyDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = GisCropVarietyDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[GisCropVarietyDto]]:
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
    kind: str | Unset = UNSET,

) -> Response[list[GisCropVarietyDto]]:
    """ Giống và gốc ghép của loài

     kind = variety (giống) | rootstock (gốc ghép); bỏ trống = cả hai.

    Args:
        id (UUID):
        kind (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[GisCropVarietyDto]]
     """


    kwargs = _get_kwargs(
        id=id,
kind=kind,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    kind: str | Unset = UNSET,

) -> list[GisCropVarietyDto] | None:
    """ Giống và gốc ghép của loài

     kind = variety (giống) | rootstock (gốc ghép); bỏ trống = cả hai.

    Args:
        id (UUID):
        kind (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[GisCropVarietyDto]
     """


    return sync_detailed(
        id=id,
client=client,
kind=kind,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    kind: str | Unset = UNSET,

) -> Response[list[GisCropVarietyDto]]:
    """ Giống và gốc ghép của loài

     kind = variety (giống) | rootstock (gốc ghép); bỏ trống = cả hai.

    Args:
        id (UUID):
        kind (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[GisCropVarietyDto]]
     """


    kwargs = _get_kwargs(
        id=id,
kind=kind,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    kind: str | Unset = UNSET,

) -> list[GisCropVarietyDto] | None:
    """ Giống và gốc ghép của loài

     kind = variety (giống) | rootstock (gốc ghép); bỏ trống = cả hai.

    Args:
        id (UUID):
        kind (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[GisCropVarietyDto]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
kind=kind,

    )).parsed
