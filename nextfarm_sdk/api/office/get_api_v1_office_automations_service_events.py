from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_service_event_service_dto import OfficeServiceEventServiceDto
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/automations/service-events",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[OfficeServiceEventServiceDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = OfficeServiceEventServiceDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[OfficeServiceEventServiceDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[OfficeServiceEventServiceDto]]:
    """ Danh mục sự kiện của phần mềm khác (kích hoạt service_event)

     `[{ service, label, events: [{ code, label, requiresFilter, perMinuteCap, keys: [{ key, label, type,
    token }] }] }]` — phần mềm → sự kiện → khoá dữ liệu (nhãn tiếng Việt). `code` đi vào `eventType` của
    cấu hình KHI; `key` đi vào `filters.groups[].rules[].key`; `token` là biến chèn được
    (`trigger.payload.<khoá>`). `type`: text · number · date · datetime · id · boolean. Danh mục này
    chính là danh sách sự kiện hệ thống đang nhận — luật có `eventType` không còn ở đây là
    `event_unknown` (không bật lại được).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeServiceEventServiceDto]]
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

) -> list[OfficeServiceEventServiceDto] | None:
    """ Danh mục sự kiện của phần mềm khác (kích hoạt service_event)

     `[{ service, label, events: [{ code, label, requiresFilter, perMinuteCap, keys: [{ key, label, type,
    token }] }] }]` — phần mềm → sự kiện → khoá dữ liệu (nhãn tiếng Việt). `code` đi vào `eventType` của
    cấu hình KHI; `key` đi vào `filters.groups[].rules[].key`; `token` là biến chèn được
    (`trigger.payload.<khoá>`). `type`: text · number · date · datetime · id · boolean. Danh mục này
    chính là danh sách sự kiện hệ thống đang nhận — luật có `eventType` không còn ở đây là
    `event_unknown` (không bật lại được).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeServiceEventServiceDto]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[OfficeServiceEventServiceDto]]:
    """ Danh mục sự kiện của phần mềm khác (kích hoạt service_event)

     `[{ service, label, events: [{ code, label, requiresFilter, perMinuteCap, keys: [{ key, label, type,
    token }] }] }]` — phần mềm → sự kiện → khoá dữ liệu (nhãn tiếng Việt). `code` đi vào `eventType` của
    cấu hình KHI; `key` đi vào `filters.groups[].rules[].key`; `token` là biến chèn được
    (`trigger.payload.<khoá>`). `type`: text · number · date · datetime · id · boolean. Danh mục này
    chính là danh sách sự kiện hệ thống đang nhận — luật có `eventType` không còn ở đây là
    `event_unknown` (không bật lại được).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeServiceEventServiceDto]]
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

) -> list[OfficeServiceEventServiceDto] | None:
    """ Danh mục sự kiện của phần mềm khác (kích hoạt service_event)

     `[{ service, label, events: [{ code, label, requiresFilter, perMinuteCap, keys: [{ key, label, type,
    token }] }] }]` — phần mềm → sự kiện → khoá dữ liệu (nhãn tiếng Việt). `code` đi vào `eventType` của
    cấu hình KHI; `key` đi vào `filters.groups[].rules[].key`; `token` là biến chèn được
    (`trigger.payload.<khoá>`). `type`: text · number · date · datetime · id · boolean. Danh mục này
    chính là danh sách sự kiện hệ thống đang nhận — luật có `eventType` không còn ở đây là
    `event_unknown` (không bật lại được).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeServiceEventServiceDto]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
