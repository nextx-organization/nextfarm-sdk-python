from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.report_trace_graph_result import ReportTraceGraphResult
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    kind: str | Unset = UNSET,
    id: str | Unset = UNSET,
    key: str | Unset = UNSET,
    depth: int | Unset = 6,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["kind"] = kind

    params["id"] = id

    params["key"] = key

    params["depth"] = depth


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/reports/trace",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ReportTraceGraphResult | None:
    if response.status_code == 200:
        response_200 = ReportTraceGraphResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ReportTraceGraphResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    kind: str | Unset = UNSET,
    id: str | Unset = UNSET,
    key: str | Unset = UNSET,
    depth: int | Unset = 6,

) -> Response[ReportTraceGraphResult]:
    """ Truy xuất ngược nhiều tầng từ một nút (phiếu thu hoạch, phiếu khoán, chứng từ, phiếu lương, phiếu
    bán…)

     kind: harvest_record · piecework_sheet · qr_code · trace_bundle · cash_document · payout_batch ·
    produce_sale · payroll_line · payroll_period. id hoặc key (số phiếu). level âm = phía lên (gốc),
    dương = phía xuống. Bước thiếu quyền ⇒ restricted (không tên/số), chuỗi dừng ở đó.

    Args:
        kind (str | Unset):
        id (str | Unset):
        key (str | Unset):
        depth (int | Unset):  Default: 6.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReportTraceGraphResult]
     """


    kwargs = _get_kwargs(
        kind=kind,
id=id,
key=key,
depth=depth,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    kind: str | Unset = UNSET,
    id: str | Unset = UNSET,
    key: str | Unset = UNSET,
    depth: int | Unset = 6,

) -> ReportTraceGraphResult | None:
    """ Truy xuất ngược nhiều tầng từ một nút (phiếu thu hoạch, phiếu khoán, chứng từ, phiếu lương, phiếu
    bán…)

     kind: harvest_record · piecework_sheet · qr_code · trace_bundle · cash_document · payout_batch ·
    produce_sale · payroll_line · payroll_period. id hoặc key (số phiếu). level âm = phía lên (gốc),
    dương = phía xuống. Bước thiếu quyền ⇒ restricted (không tên/số), chuỗi dừng ở đó.

    Args:
        kind (str | Unset):
        id (str | Unset):
        key (str | Unset):
        depth (int | Unset):  Default: 6.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReportTraceGraphResult
     """


    return sync_detailed(
        client=client,
kind=kind,
id=id,
key=key,
depth=depth,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    kind: str | Unset = UNSET,
    id: str | Unset = UNSET,
    key: str | Unset = UNSET,
    depth: int | Unset = 6,

) -> Response[ReportTraceGraphResult]:
    """ Truy xuất ngược nhiều tầng từ một nút (phiếu thu hoạch, phiếu khoán, chứng từ, phiếu lương, phiếu
    bán…)

     kind: harvest_record · piecework_sheet · qr_code · trace_bundle · cash_document · payout_batch ·
    produce_sale · payroll_line · payroll_period. id hoặc key (số phiếu). level âm = phía lên (gốc),
    dương = phía xuống. Bước thiếu quyền ⇒ restricted (không tên/số), chuỗi dừng ở đó.

    Args:
        kind (str | Unset):
        id (str | Unset):
        key (str | Unset):
        depth (int | Unset):  Default: 6.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReportTraceGraphResult]
     """


    kwargs = _get_kwargs(
        kind=kind,
id=id,
key=key,
depth=depth,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    kind: str | Unset = UNSET,
    id: str | Unset = UNSET,
    key: str | Unset = UNSET,
    depth: int | Unset = 6,

) -> ReportTraceGraphResult | None:
    """ Truy xuất ngược nhiều tầng từ một nút (phiếu thu hoạch, phiếu khoán, chứng từ, phiếu lương, phiếu
    bán…)

     kind: harvest_record · piecework_sheet · qr_code · trace_bundle · cash_document · payout_batch ·
    produce_sale · payroll_line · payroll_period. id hoặc key (số phiếu). level âm = phía lên (gốc),
    dương = phía xuống. Bước thiếu quyền ⇒ restricted (không tên/số), chuỗi dừng ở đó.

    Args:
        kind (str | Unset):
        id (str | Unset):
        key (str | Unset):
        depth (int | Unset):  Default: 6.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReportTraceGraphResult
     """


    return (await asyncio_detailed(
        client=client,
kind=kind,
id=id,
key=key,
depth=depth,

    )).parsed
