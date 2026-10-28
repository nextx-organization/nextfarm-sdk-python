from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.harvest_market_price_series_response_dto import HarvestMarketPriceSeriesResponseDto
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    commodity_code: list[str] | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    unit: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_commodity_code: list[str] | Unset = UNSET
    if not isinstance(commodity_code, Unset):
        json_commodity_code = commodity_code


    params["commodityCode"] = json_commodity_code

    json_from_date: str | Unset = UNSET
    if not isinstance(from_date, Unset):
        json_from_date = from_date.isoformat()
    params["fromDate"] = json_from_date

    json_to_date: str | Unset = UNSET
    if not isinstance(to_date, Unset):
        json_to_date = to_date.isoformat()
    params["toDate"] = json_to_date

    params["unit"] = unit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/harvest/market-prices/series",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HarvestMarketPriceSeriesResponseDto | None:
    if response.status_code == 200:
        response_200 = HarvestMarketPriceSeriesResponseDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HarvestMarketPriceSeriesResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    commodity_code: list[str] | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    unit: str | Unset = UNSET,

) -> Response[HarvestMarketPriceSeriesResponseDto]:
    """ Chuỗi giá theo thời gian để vẽ biểu đồ

     Mọi chuỗi trả về CÙNG MỘT đơn vị (trường `unit` ở cấp response). Biểu đồ bên FE chỉ có một trục y —
    mặt hàng lệch đơn vị bị bỏ qua chứ KHÔNG quy đổi, vì đoán sai hệ số quy đổi là sai số liệu âm thầm.
    Không truyền `unit` thì lấy đơn vị phổ biến nhất trong khoảng lọc.

    Args:
        commodity_code (list[str] | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        unit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HarvestMarketPriceSeriesResponseDto]
     """


    kwargs = _get_kwargs(
        commodity_code=commodity_code,
from_date=from_date,
to_date=to_date,
unit=unit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    commodity_code: list[str] | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    unit: str | Unset = UNSET,

) -> HarvestMarketPriceSeriesResponseDto | None:
    """ Chuỗi giá theo thời gian để vẽ biểu đồ

     Mọi chuỗi trả về CÙNG MỘT đơn vị (trường `unit` ở cấp response). Biểu đồ bên FE chỉ có một trục y —
    mặt hàng lệch đơn vị bị bỏ qua chứ KHÔNG quy đổi, vì đoán sai hệ số quy đổi là sai số liệu âm thầm.
    Không truyền `unit` thì lấy đơn vị phổ biến nhất trong khoảng lọc.

    Args:
        commodity_code (list[str] | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        unit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HarvestMarketPriceSeriesResponseDto
     """


    return sync_detailed(
        client=client,
commodity_code=commodity_code,
from_date=from_date,
to_date=to_date,
unit=unit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    commodity_code: list[str] | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    unit: str | Unset = UNSET,

) -> Response[HarvestMarketPriceSeriesResponseDto]:
    """ Chuỗi giá theo thời gian để vẽ biểu đồ

     Mọi chuỗi trả về CÙNG MỘT đơn vị (trường `unit` ở cấp response). Biểu đồ bên FE chỉ có một trục y —
    mặt hàng lệch đơn vị bị bỏ qua chứ KHÔNG quy đổi, vì đoán sai hệ số quy đổi là sai số liệu âm thầm.
    Không truyền `unit` thì lấy đơn vị phổ biến nhất trong khoảng lọc.

    Args:
        commodity_code (list[str] | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        unit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HarvestMarketPriceSeriesResponseDto]
     """


    kwargs = _get_kwargs(
        commodity_code=commodity_code,
from_date=from_date,
to_date=to_date,
unit=unit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    commodity_code: list[str] | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    unit: str | Unset = UNSET,

) -> HarvestMarketPriceSeriesResponseDto | None:
    """ Chuỗi giá theo thời gian để vẽ biểu đồ

     Mọi chuỗi trả về CÙNG MỘT đơn vị (trường `unit` ở cấp response). Biểu đồ bên FE chỉ có một trục y —
    mặt hàng lệch đơn vị bị bỏ qua chứ KHÔNG quy đổi, vì đoán sai hệ số quy đổi là sai số liệu âm thầm.
    Không truyền `unit` thì lấy đơn vị phổ biến nhất trong khoảng lọc.

    Args:
        commodity_code (list[str] | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        unit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HarvestMarketPriceSeriesResponseDto
     """


    return (await asyncio_detailed(
        client=client,
commodity_code=commodity_code,
from_date=from_date,
to_date=to_date,
unit=unit,

    )).parsed
