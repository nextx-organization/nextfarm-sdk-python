from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_field_dto import OfficeFieldDto
from typing import cast
from uuid import UUID



def _get_kwargs(
    table_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/tables/{table_id}/fields".format(table_id=quote(str(table_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[OfficeFieldDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = OfficeFieldDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[OfficeFieldDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[OfficeFieldDto]]:
    """ Liệt kê field của table

    Args:
        table_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeFieldDto]]
     """


    kwargs = _get_kwargs(
        table_id=table_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    table_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> list[OfficeFieldDto] | None:
    """ Liệt kê field của table

    Args:
        table_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeFieldDto]
     """


    return sync_detailed(
        table_id=table_id,
client=client,

    ).parsed

async def asyncio_detailed(
    table_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[OfficeFieldDto]]:
    """ Liệt kê field của table

    Args:
        table_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeFieldDto]]
     """


    kwargs = _get_kwargs(
        table_id=table_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    table_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> list[OfficeFieldDto] | None:
    """ Liệt kê field của table

    Args:
        table_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeFieldDto]
     """


    return (await asyncio_detailed(
        table_id=table_id,
client=client,

    )).parsed
