from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_automation_overlap_dto import OfficeAutomationOverlapDto
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/automations/{id}/overlaps".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[OfficeAutomationOverlapDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = OfficeAutomationOverlapDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[OfficeAutomationOverlapDto]]:
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

) -> Response[list[OfficeAutomationOverlapDto]]:
    """ Luật khác cùng kích hoạt và cùng làm việc này

     Các luật ĐANG BẬT khác của công ty có cùng kiểu kích hoạt, cùng phạm vi nghe (bảng, cột, loại sự
    kiện, kênh — bỏ phần lọc) và ít nhất một loại hành động chung với luật này, kèm `sharedActions`. Chỉ
    cảnh báo: bộ lọc khác nhau thì hai luật có thể không bao giờ cùng chạy, người dùng tự xét. Tối đa
    10.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeAutomationOverlapDto]]
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

) -> list[OfficeAutomationOverlapDto] | None:
    """ Luật khác cùng kích hoạt và cùng làm việc này

     Các luật ĐANG BẬT khác của công ty có cùng kiểu kích hoạt, cùng phạm vi nghe (bảng, cột, loại sự
    kiện, kênh — bỏ phần lọc) và ít nhất một loại hành động chung với luật này, kèm `sharedActions`. Chỉ
    cảnh báo: bộ lọc khác nhau thì hai luật có thể không bao giờ cùng chạy, người dùng tự xét. Tối đa
    10.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeAutomationOverlapDto]
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[OfficeAutomationOverlapDto]]:
    """ Luật khác cùng kích hoạt và cùng làm việc này

     Các luật ĐANG BẬT khác của công ty có cùng kiểu kích hoạt, cùng phạm vi nghe (bảng, cột, loại sự
    kiện, kênh — bỏ phần lọc) và ít nhất một loại hành động chung với luật này, kèm `sharedActions`. Chỉ
    cảnh báo: bộ lọc khác nhau thì hai luật có thể không bao giờ cùng chạy, người dùng tự xét. Tối đa
    10.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeAutomationOverlapDto]]
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

) -> list[OfficeAutomationOverlapDto] | None:
    """ Luật khác cùng kích hoạt và cùng làm việc này

     Các luật ĐANG BẬT khác của công ty có cùng kiểu kích hoạt, cùng phạm vi nghe (bảng, cột, loại sự
    kiện, kênh — bỏ phần lọc) và ít nhất một loại hành động chung với luật này, kèm `sharedActions`. Chỉ
    cảnh báo: bộ lọc khác nhau thì hai luật có thể không bao giờ cùng chạy, người dùng tự xét. Tối đa
    10.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeAutomationOverlapDto]
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
