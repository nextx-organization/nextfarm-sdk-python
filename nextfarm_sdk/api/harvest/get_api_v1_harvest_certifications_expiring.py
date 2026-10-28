from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.harvest_certification_list_dto import HarvestCertificationListDto
from ...models.harvest_problem_details import HarvestProblemDetails
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    within_days: int | Unset = 90,
    include_expired: bool | Unset = True,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["within_days"] = within_days

    params["include_expired"] = include_expired


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/harvest/certifications/expiring",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HarvestProblemDetails | list[HarvestCertificationListDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = HarvestCertificationListDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 422:
        response_422 = HarvestProblemDetails.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HarvestProblemDetails | list[HarvestCertificationListDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    within_days: int | Unset = 90,
    include_expired: bool | Unset = True,

) -> Response[HarvestProblemDetails | list[HarvestCertificationListDto]]:
    """ Chứng nhận sắp hết hạn

     Sắp theo ngày hết hạn TĂNG DẦN — bản đã hết hạn lâu nhất đứng đầu. within_days là cửa sổ nhìn tới
    tính từ hôm nay (mặc định 90). include_expired mặc định BẬT: nhóm đã hết hạn mới là nhóm gấp nhất.

    Args:
        within_days (int | Unset):  Default: 90.
        include_expired (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HarvestProblemDetails | list[HarvestCertificationListDto]]
     """


    kwargs = _get_kwargs(
        within_days=within_days,
include_expired=include_expired,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    within_days: int | Unset = 90,
    include_expired: bool | Unset = True,

) -> HarvestProblemDetails | list[HarvestCertificationListDto] | None:
    """ Chứng nhận sắp hết hạn

     Sắp theo ngày hết hạn TĂNG DẦN — bản đã hết hạn lâu nhất đứng đầu. within_days là cửa sổ nhìn tới
    tính từ hôm nay (mặc định 90). include_expired mặc định BẬT: nhóm đã hết hạn mới là nhóm gấp nhất.

    Args:
        within_days (int | Unset):  Default: 90.
        include_expired (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HarvestProblemDetails | list[HarvestCertificationListDto]
     """


    return sync_detailed(
        client=client,
within_days=within_days,
include_expired=include_expired,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    within_days: int | Unset = 90,
    include_expired: bool | Unset = True,

) -> Response[HarvestProblemDetails | list[HarvestCertificationListDto]]:
    """ Chứng nhận sắp hết hạn

     Sắp theo ngày hết hạn TĂNG DẦN — bản đã hết hạn lâu nhất đứng đầu. within_days là cửa sổ nhìn tới
    tính từ hôm nay (mặc định 90). include_expired mặc định BẬT: nhóm đã hết hạn mới là nhóm gấp nhất.

    Args:
        within_days (int | Unset):  Default: 90.
        include_expired (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HarvestProblemDetails | list[HarvestCertificationListDto]]
     """


    kwargs = _get_kwargs(
        within_days=within_days,
include_expired=include_expired,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    within_days: int | Unset = 90,
    include_expired: bool | Unset = True,

) -> HarvestProblemDetails | list[HarvestCertificationListDto] | None:
    """ Chứng nhận sắp hết hạn

     Sắp theo ngày hết hạn TĂNG DẦN — bản đã hết hạn lâu nhất đứng đầu. within_days là cửa sổ nhìn tới
    tính từ hôm nay (mặc định 90). include_expired mặc định BẬT: nhóm đã hết hạn mới là nhóm gấp nhất.

    Args:
        within_days (int | Unset):  Default: 90.
        include_expired (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HarvestProblemDetails | list[HarvestCertificationListDto]
     """


    return (await asyncio_detailed(
        client=client,
within_days=within_days,
include_expired=include_expired,

    )).parsed
