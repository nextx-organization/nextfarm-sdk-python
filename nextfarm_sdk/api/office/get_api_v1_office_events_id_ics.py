from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import File, FileTypes
from io import BytesIO
from uuid import UUID



def _get_kwargs(
    id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/events/{id}.ics".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> File | None:
    if response.status_code == 200:
        response_200 = File(
             payload = BytesIO(response.json())
        )



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[File]:
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

) -> Response[File]:
    """ Tải tệp lịch .ics của sự kiện

     Cho người TRONG công ty đã đăng nhập (chủ trì/người dự/lịch chia sẻ đủ mức). Khách ngoài công ty đi
    qua liên kết công khai riêng trong thư mời — xem PublicCalendarController, KHÔNG phải endpoint này.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
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

) -> File | None:
    """ Tải tệp lịch .ics của sự kiện

     Cho người TRONG công ty đã đăng nhập (chủ trì/người dự/lịch chia sẻ đủ mức). Khách ngoài công ty đi
    qua liên kết công khai riêng trong thư mời — xem PublicCalendarController, KHÔNG phải endpoint này.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[File]:
    """ Tải tệp lịch .ics của sự kiện

     Cho người TRONG công ty đã đăng nhập (chủ trì/người dự/lịch chia sẻ đủ mức). Khách ngoài công ty đi
    qua liên kết công khai riêng trong thư mời — xem PublicCalendarController, KHÔNG phải endpoint này.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
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

) -> File | None:
    """ Tải tệp lịch .ics của sự kiện

     Cho người TRONG công ty đã đăng nhập (chủ trì/người dự/lịch chia sẻ đủ mức). Khách ngoài công ty đi
    qua liên kết công khai riêng trong thư mời — xem PublicCalendarController, KHÔNG phải endpoint này.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
