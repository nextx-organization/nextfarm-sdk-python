from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_calendar_link_status_dto import OfficeCalendarLinkStatusDto
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/calendar-links",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeCalendarLinkStatusDto | None:
    if response.status_code == 200:
        response_200 = OfficeCalendarLinkStatusDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeCalendarLinkStatusDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[OfficeCalendarLinkStatusDto]:
    """ Tình trạng nối lịch của tôi

     providerConfigured = false nghĩa là máy chủ chưa có khoá kết nối Google — giao diện phải nói 'quản
    trị chưa bật', không phải 'bạn chưa nối'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeCalendarLinkStatusDto]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> OfficeCalendarLinkStatusDto | None:
    """ Tình trạng nối lịch của tôi

     providerConfigured = false nghĩa là máy chủ chưa có khoá kết nối Google — giao diện phải nói 'quản
    trị chưa bật', không phải 'bạn chưa nối'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeCalendarLinkStatusDto
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[OfficeCalendarLinkStatusDto]:
    """ Tình trạng nối lịch của tôi

     providerConfigured = false nghĩa là máy chủ chưa có khoá kết nối Google — giao diện phải nói 'quản
    trị chưa bật', không phải 'bạn chưa nối'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeCalendarLinkStatusDto]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> OfficeCalendarLinkStatusDto | None:
    """ Tình trạng nối lịch của tôi

     providerConfigured = false nghĩa là máy chủ chưa có khoá kết nối Google — giao diện phải nói 'quản
    trị chưa bật', không phải 'bạn chưa nối'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeCalendarLinkStatusDto
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
