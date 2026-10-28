from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.harvest_problem_details import HarvestProblemDetails
from typing import cast



def _get_kwargs(
    code: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/harvest/trace-pdf/{code}".format(code=quote(str(code), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | HarvestProblemDetails | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = HarvestProblemDetails.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = HarvestProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | HarvestProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    code: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | HarvestProblemDetails]:
    """ Tải hồ sơ truy xuất PDF theo mã QR (YÊU CẦU ĐĂNG NHẬP)

     Trả PDF VietGAP của lô. Tệp có họ tên + số điện thoại nông hộ nên KHÔNG phát ra đường công khai. 404
    khi: mã không tồn tại · mã hết hạn · lô chưa kết xuất PDF · tệp không còn trong kho.

    Args:
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HarvestProblemDetails]
     """


    kwargs = _get_kwargs(
        code=code,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    code: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | HarvestProblemDetails | None:
    """ Tải hồ sơ truy xuất PDF theo mã QR (YÊU CẦU ĐĂNG NHẬP)

     Trả PDF VietGAP của lô. Tệp có họ tên + số điện thoại nông hộ nên KHÔNG phát ra đường công khai. 404
    khi: mã không tồn tại · mã hết hạn · lô chưa kết xuất PDF · tệp không còn trong kho.

    Args:
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HarvestProblemDetails
     """


    return sync_detailed(
        code=code,
client=client,

    ).parsed

async def asyncio_detailed(
    code: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | HarvestProblemDetails]:
    """ Tải hồ sơ truy xuất PDF theo mã QR (YÊU CẦU ĐĂNG NHẬP)

     Trả PDF VietGAP của lô. Tệp có họ tên + số điện thoại nông hộ nên KHÔNG phát ra đường công khai. 404
    khi: mã không tồn tại · mã hết hạn · lô chưa kết xuất PDF · tệp không còn trong kho.

    Args:
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HarvestProblemDetails]
     """


    kwargs = _get_kwargs(
        code=code,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    code: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | HarvestProblemDetails | None:
    """ Tải hồ sơ truy xuất PDF theo mã QR (YÊU CẦU ĐĂNG NHẬP)

     Trả PDF VietGAP của lô. Tệp có họ tên + số điện thoại nông hộ nên KHÔNG phát ra đường công khai. 404
    khi: mã không tồn tại · mã hết hạn · lô chưa kết xuất PDF · tệp không còn trong kho.

    Args:
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HarvestProblemDetails
     """


    return (await asyncio_detailed(
        code=code,
client=client,

    )).parsed
