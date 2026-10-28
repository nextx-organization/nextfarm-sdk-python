from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_automation_metrics_dto import OfficeAutomationMetricsDto
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    days: int | Unset = 7,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["days"] = days


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/automation-logs/metrics",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeAutomationMetricsDto | None:
    if response.status_code == 200:
        response_200 = OfficeAutomationMetricsDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeAutomationMetricsDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 7,

) -> Response[OfficeAutomationMetricsDto]:
    """ Chỉ số vận hành của Tự động hoá trong công ty

     Trong `days` ngày (1–90): số dòng theo kết quả, `failureRate`, `quotaBlocked` (số lần bị bỏ qua vì
    hết lượt chạy tháng), hạn mức tháng, và hàng đợi: `activeRuns`, `dueRuns` (đã tới hạn mà bộ chạy
    chưa lấy), `oldestDueSeconds` (lượt tới hạn cũ nhất đã đợi bao lâu).

    Args:
        days (int | Unset):  Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeAutomationMetricsDto]
     """


    kwargs = _get_kwargs(
        days=days,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 7,

) -> OfficeAutomationMetricsDto | None:
    """ Chỉ số vận hành của Tự động hoá trong công ty

     Trong `days` ngày (1–90): số dòng theo kết quả, `failureRate`, `quotaBlocked` (số lần bị bỏ qua vì
    hết lượt chạy tháng), hạn mức tháng, và hàng đợi: `activeRuns`, `dueRuns` (đã tới hạn mà bộ chạy
    chưa lấy), `oldestDueSeconds` (lượt tới hạn cũ nhất đã đợi bao lâu).

    Args:
        days (int | Unset):  Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeAutomationMetricsDto
     """


    return sync_detailed(
        client=client,
days=days,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 7,

) -> Response[OfficeAutomationMetricsDto]:
    """ Chỉ số vận hành của Tự động hoá trong công ty

     Trong `days` ngày (1–90): số dòng theo kết quả, `failureRate`, `quotaBlocked` (số lần bị bỏ qua vì
    hết lượt chạy tháng), hạn mức tháng, và hàng đợi: `activeRuns`, `dueRuns` (đã tới hạn mà bộ chạy
    chưa lấy), `oldestDueSeconds` (lượt tới hạn cũ nhất đã đợi bao lâu).

    Args:
        days (int | Unset):  Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeAutomationMetricsDto]
     """


    kwargs = _get_kwargs(
        days=days,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 7,

) -> OfficeAutomationMetricsDto | None:
    """ Chỉ số vận hành của Tự động hoá trong công ty

     Trong `days` ngày (1–90): số dòng theo kết quả, `failureRate`, `quotaBlocked` (số lần bị bỏ qua vì
    hết lượt chạy tháng), hạn mức tháng, và hàng đợi: `activeRuns`, `dueRuns` (đã tới hạn mà bộ chạy
    chưa lấy), `oldestDueSeconds` (lượt tới hạn cũ nhất đã đợi bao lâu).

    Args:
        days (int | Unset):  Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeAutomationMetricsDto
     """


    return (await asyncio_detailed(
        client=client,
days=days,

    )).parsed
