from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.harvest_phi_status_dto import HarvestPhiStatusDto
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    on: datetime.date | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_on: str | Unset = UNSET
    if not isinstance(on, Unset):
        json_on = on.isoformat()
    params["on"] = json_on


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/harvest/parcels/phi-active",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[HarvestPhiStatusDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = HarvestPhiStatusDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[HarvestPhiStatusDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    on: datetime.date | Unset = UNSET,

) -> Response[list[HarvestPhiStatusDto]]:
    """ Các thửa đang trong thời gian cách ly

     Gộp lần phun ghi nhật ký, phiếu xuất thuốc BVTV và thuốc thú y từ kho (GĐ4), thuốc thú y ở sổ đàn/ao
    — tức cả thửa vườn lẫn ao/chuồng đang cách ly hoặc ngưng thuốc. on = ngày xét (mặc định hôm nay giờ
    VN). Mỗi dòng: parcel_id, safe_from (ngày sớm nhất được thu), blocking (lần dùng thuốc đang giữ cách
    ly; kind = spray | inventory | inventory_vet | vet). Theo phạm vi thửa của người xem. Dùng cho màn
    Thu hoạch và Tổng quan nông trại.

    Args:
        on (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[HarvestPhiStatusDto]]
     """


    kwargs = _get_kwargs(
        on=on,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    on: datetime.date | Unset = UNSET,

) -> list[HarvestPhiStatusDto] | None:
    """ Các thửa đang trong thời gian cách ly

     Gộp lần phun ghi nhật ký, phiếu xuất thuốc BVTV và thuốc thú y từ kho (GĐ4), thuốc thú y ở sổ đàn/ao
    — tức cả thửa vườn lẫn ao/chuồng đang cách ly hoặc ngưng thuốc. on = ngày xét (mặc định hôm nay giờ
    VN). Mỗi dòng: parcel_id, safe_from (ngày sớm nhất được thu), blocking (lần dùng thuốc đang giữ cách
    ly; kind = spray | inventory | inventory_vet | vet). Theo phạm vi thửa của người xem. Dùng cho màn
    Thu hoạch và Tổng quan nông trại.

    Args:
        on (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[HarvestPhiStatusDto]
     """


    return sync_detailed(
        client=client,
on=on,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    on: datetime.date | Unset = UNSET,

) -> Response[list[HarvestPhiStatusDto]]:
    """ Các thửa đang trong thời gian cách ly

     Gộp lần phun ghi nhật ký, phiếu xuất thuốc BVTV và thuốc thú y từ kho (GĐ4), thuốc thú y ở sổ đàn/ao
    — tức cả thửa vườn lẫn ao/chuồng đang cách ly hoặc ngưng thuốc. on = ngày xét (mặc định hôm nay giờ
    VN). Mỗi dòng: parcel_id, safe_from (ngày sớm nhất được thu), blocking (lần dùng thuốc đang giữ cách
    ly; kind = spray | inventory | inventory_vet | vet). Theo phạm vi thửa của người xem. Dùng cho màn
    Thu hoạch và Tổng quan nông trại.

    Args:
        on (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[HarvestPhiStatusDto]]
     """


    kwargs = _get_kwargs(
        on=on,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    on: datetime.date | Unset = UNSET,

) -> list[HarvestPhiStatusDto] | None:
    """ Các thửa đang trong thời gian cách ly

     Gộp lần phun ghi nhật ký, phiếu xuất thuốc BVTV và thuốc thú y từ kho (GĐ4), thuốc thú y ở sổ đàn/ao
    — tức cả thửa vườn lẫn ao/chuồng đang cách ly hoặc ngưng thuốc. on = ngày xét (mặc định hôm nay giờ
    VN). Mỗi dòng: parcel_id, safe_from (ngày sớm nhất được thu), blocking (lần dùng thuốc đang giữ cách
    ly; kind = spray | inventory | inventory_vet | vet). Theo phạm vi thửa của người xem. Dùng cho màn
    Thu hoạch và Tổng quan nông trại.

    Args:
        on (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[HarvestPhiStatusDto]
     """


    return (await asyncio_detailed(
        client=client,
on=on,

    )).parsed
