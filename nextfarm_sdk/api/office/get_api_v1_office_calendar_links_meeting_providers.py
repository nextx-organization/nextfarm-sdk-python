from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_meeting_provider_dto import OfficeMeetingProviderDto
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/calendar-links/meeting-providers",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[OfficeMeetingProviderDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = OfficeMeetingProviderDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[OfficeMeetingProviderDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[OfficeMeetingProviderDto]]:
    """ Những nơi cung cấp phòng họp trực tuyến đang bật

     CHỈ trả về nhà cung cấp đã khai đủ khoá kết nối trên máy chủ. Giao diện phải dựng ô chọn từ danh
    sách này thay vì khai cứng — công ty chưa bật Teams mà vẫn thấy lựa chọn Teams thì chọn xong là nhận
    lỗi. connected = false nghĩa là người dùng chưa nối tài khoản, khác hẳn với 'quản trị chưa bật'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeMeetingProviderDto]]
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

) -> list[OfficeMeetingProviderDto] | None:
    """ Những nơi cung cấp phòng họp trực tuyến đang bật

     CHỈ trả về nhà cung cấp đã khai đủ khoá kết nối trên máy chủ. Giao diện phải dựng ô chọn từ danh
    sách này thay vì khai cứng — công ty chưa bật Teams mà vẫn thấy lựa chọn Teams thì chọn xong là nhận
    lỗi. connected = false nghĩa là người dùng chưa nối tài khoản, khác hẳn với 'quản trị chưa bật'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeMeetingProviderDto]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[OfficeMeetingProviderDto]]:
    """ Những nơi cung cấp phòng họp trực tuyến đang bật

     CHỈ trả về nhà cung cấp đã khai đủ khoá kết nối trên máy chủ. Giao diện phải dựng ô chọn từ danh
    sách này thay vì khai cứng — công ty chưa bật Teams mà vẫn thấy lựa chọn Teams thì chọn xong là nhận
    lỗi. connected = false nghĩa là người dùng chưa nối tài khoản, khác hẳn với 'quản trị chưa bật'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeMeetingProviderDto]]
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

) -> list[OfficeMeetingProviderDto] | None:
    """ Những nơi cung cấp phòng họp trực tuyến đang bật

     CHỈ trả về nhà cung cấp đã khai đủ khoá kết nối trên máy chủ. Giao diện phải dựng ô chọn từ danh
    sách này thay vì khai cứng — công ty chưa bật Teams mà vẫn thấy lựa chọn Teams thì chọn xong là nhận
    lỗi. connected = false nghĩa là người dùng chưa nối tài khoản, khác hẳn với 'quản trị chưa bật'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeMeetingProviderDto]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
