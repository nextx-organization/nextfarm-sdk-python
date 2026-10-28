from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_table_dto import OfficeTableDto
from typing import cast
from uuid import UUID



def _get_kwargs(
    app_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/apps/{app_id}/tables".format(app_id=quote(str(app_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[OfficeTableDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = OfficeTableDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[OfficeTableDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[OfficeTableDto]]:
    """ Liệt kê table của app

    Args:
        app_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeTableDto]]
     """


    kwargs = _get_kwargs(
        app_id=app_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    app_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> list[OfficeTableDto] | None:
    """ Liệt kê table của app

    Args:
        app_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeTableDto]
     """


    return sync_detailed(
        app_id=app_id,
client=client,

    ).parsed

async def asyncio_detailed(
    app_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[OfficeTableDto]]:
    """ Liệt kê table của app

    Args:
        app_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeTableDto]]
     """


    kwargs = _get_kwargs(
        app_id=app_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    app_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> list[OfficeTableDto] | None:
    """ Liệt kê table của app

    Args:
        app_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeTableDto]
     """


    return (await asyncio_detailed(
        app_id=app_id,
client=client,

    )).parsed
