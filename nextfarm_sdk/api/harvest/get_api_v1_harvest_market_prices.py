from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.harvest_market_price_dto_paged_result import HarvestMarketPriceDtoPagedResult
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    commodity_code: list[str] | Unset = UNSET,
    market: str | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_commodity_code: list[str] | Unset = UNSET
    if not isinstance(commodity_code, Unset):
        json_commodity_code = commodity_code


    params["commodityCode"] = json_commodity_code

    params["market"] = market

    json_from_date: str | Unset = UNSET
    if not isinstance(from_date, Unset):
        json_from_date = from_date.isoformat()
    params["fromDate"] = json_from_date

    json_to_date: str | Unset = UNSET
    if not isinstance(to_date, Unset):
        json_to_date = to_date.isoformat()
    params["toDate"] = json_to_date

    params["page"] = page

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/harvest/market-prices",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HarvestMarketPriceDtoPagedResult | None:
    if response.status_code == 200:
        response_200 = HarvestMarketPriceDtoPagedResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HarvestMarketPriceDtoPagedResult]:
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
    market: str | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[HarvestMarketPriceDtoPagedResult]:
    """ Danh sách giá đã ghi nhận

     Lọc theo mặt hàng (nhiều mã), chợ/vùng và khoảng ngày. Phân trang.

    Args:
        commodity_code (list[str] | Unset):
        market (str | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HarvestMarketPriceDtoPagedResult]
     """


    kwargs = _get_kwargs(
        commodity_code=commodity_code,
market=market,
from_date=from_date,
to_date=to_date,
page=page,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    commodity_code: list[str] | Unset = UNSET,
    market: str | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> HarvestMarketPriceDtoPagedResult | None:
    """ Danh sách giá đã ghi nhận

     Lọc theo mặt hàng (nhiều mã), chợ/vùng và khoảng ngày. Phân trang.

    Args:
        commodity_code (list[str] | Unset):
        market (str | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HarvestMarketPriceDtoPagedResult
     """


    return sync_detailed(
        client=client,
commodity_code=commodity_code,
market=market,
from_date=from_date,
to_date=to_date,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    commodity_code: list[str] | Unset = UNSET,
    market: str | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[HarvestMarketPriceDtoPagedResult]:
    """ Danh sách giá đã ghi nhận

     Lọc theo mặt hàng (nhiều mã), chợ/vùng và khoảng ngày. Phân trang.

    Args:
        commodity_code (list[str] | Unset):
        market (str | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HarvestMarketPriceDtoPagedResult]
     """


    kwargs = _get_kwargs(
        commodity_code=commodity_code,
market=market,
from_date=from_date,
to_date=to_date,
page=page,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    commodity_code: list[str] | Unset = UNSET,
    market: str | Unset = UNSET,
    from_date: datetime.date | Unset = UNSET,
    to_date: datetime.date | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> HarvestMarketPriceDtoPagedResult | None:
    """ Danh sách giá đã ghi nhận

     Lọc theo mặt hàng (nhiều mã), chợ/vùng và khoảng ngày. Phân trang.

    Args:
        commodity_code (list[str] | Unset):
        market (str | Unset):
        from_date (datetime.date | Unset):
        to_date (datetime.date | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HarvestMarketPriceDtoPagedResult
     """


    return (await asyncio_detailed(
        client=client,
commodity_code=commodity_code,
market=market,
from_date=from_date,
to_date=to_date,
page=page,
page_size=page_size,

    )).parsed
