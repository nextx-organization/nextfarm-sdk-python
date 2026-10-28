from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.report_report_result import ReportReportResult
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    code: str | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    grain: str | Unset = UNSET,
    compare: str | Unset = 'previous',
    include_sample: bool | Unset = True,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["code"] = code

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["grain"] = grain

    params["compare"] = compare

    params["includeSample"] = include_sample


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/reports/query",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ReportReportResult | None:
    if response.status_code == 200:
        response_200 = ReportReportResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ReportReportResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    code: str | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    grain: str | Unset = UNSET,
    compare: str | Unset = 'previous',
    include_sample: bool | Unset = True,

) -> Response[ReportReportResult]:
    """ Chạy báo cáo bằng GET; thiếu to = hôm nay UTC+7, thiếu from = to - 29 ngày

    Args:
        code (str | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        grain (str | Unset):
        compare (str | Unset):  Default: 'previous'.
        include_sample (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReportReportResult]
     """


    kwargs = _get_kwargs(
        code=code,
from_=from_,
to=to,
grain=grain,
compare=compare,
include_sample=include_sample,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    code: str | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    grain: str | Unset = UNSET,
    compare: str | Unset = 'previous',
    include_sample: bool | Unset = True,

) -> ReportReportResult | None:
    """ Chạy báo cáo bằng GET; thiếu to = hôm nay UTC+7, thiếu from = to - 29 ngày

    Args:
        code (str | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        grain (str | Unset):
        compare (str | Unset):  Default: 'previous'.
        include_sample (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReportReportResult
     """


    return sync_detailed(
        client=client,
code=code,
from_=from_,
to=to,
grain=grain,
compare=compare,
include_sample=include_sample,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    code: str | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    grain: str | Unset = UNSET,
    compare: str | Unset = 'previous',
    include_sample: bool | Unset = True,

) -> Response[ReportReportResult]:
    """ Chạy báo cáo bằng GET; thiếu to = hôm nay UTC+7, thiếu from = to - 29 ngày

    Args:
        code (str | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        grain (str | Unset):
        compare (str | Unset):  Default: 'previous'.
        include_sample (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReportReportResult]
     """


    kwargs = _get_kwargs(
        code=code,
from_=from_,
to=to,
grain=grain,
compare=compare,
include_sample=include_sample,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    code: str | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    grain: str | Unset = UNSET,
    compare: str | Unset = 'previous',
    include_sample: bool | Unset = True,

) -> ReportReportResult | None:
    """ Chạy báo cáo bằng GET; thiếu to = hôm nay UTC+7, thiếu from = to - 29 ngày

    Args:
        code (str | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        grain (str | Unset):
        compare (str | Unset):  Default: 'previous'.
        include_sample (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReportReportResult
     """


    return (await asyncio_detailed(
        client=client,
code=code,
from_=from_,
to=to,
grain=grain,
compare=compare,
include_sample=include_sample,

    )).parsed
