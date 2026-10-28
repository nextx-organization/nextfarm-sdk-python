from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_dashboard_widget_data_dto import OfficeDashboardWidgetDataDto
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    widget_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/dashboards/{id}/widgets/{widget_id}/data".format(id=quote(str(id), safe=""),widget_id=quote(str(widget_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeDashboardWidgetDataDto | None:
    if response.status_code == 200:
        response_200 = OfficeDashboardWidgetDataDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeDashboardWidgetDataDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    widget_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[OfficeDashboardWidgetDataDto]:
    """ Số liệu một ô, tính theo quyền người xem

     unavailable = table_missing (bảng đã xoá) | no_access (ô đọc cột/bảng người xem không được thấy).

    Args:
        id (UUID):
        widget_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeDashboardWidgetDataDto]
     """


    kwargs = _get_kwargs(
        id=id,
widget_id=widget_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    widget_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> OfficeDashboardWidgetDataDto | None:
    """ Số liệu một ô, tính theo quyền người xem

     unavailable = table_missing (bảng đã xoá) | no_access (ô đọc cột/bảng người xem không được thấy).

    Args:
        id (UUID):
        widget_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeDashboardWidgetDataDto
     """


    return sync_detailed(
        id=id,
widget_id=widget_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    widget_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[OfficeDashboardWidgetDataDto]:
    """ Số liệu một ô, tính theo quyền người xem

     unavailable = table_missing (bảng đã xoá) | no_access (ô đọc cột/bảng người xem không được thấy).

    Args:
        id (UUID):
        widget_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeDashboardWidgetDataDto]
     """


    kwargs = _get_kwargs(
        id=id,
widget_id=widget_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    widget_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> OfficeDashboardWidgetDataDto | None:
    """ Số liệu một ô, tính theo quyền người xem

     unavailable = table_missing (bảng đã xoá) | no_access (ô đọc cột/bảng người xem không được thấy).

    Args:
        id (UUID):
        widget_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeDashboardWidgetDataDto
     """


    return (await asyncio_detailed(
        id=id,
widget_id=widget_id,
client=client,

    )).parsed
