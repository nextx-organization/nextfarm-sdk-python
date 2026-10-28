from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.report_labor_cost_report_dto import ReportLaborCostReportDto
from ...models.report_problem_details import ReportProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    parcel_id: UUID | Unset = UNSET,
    season_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    json_parcel_id: str | Unset = UNSET
    if not isinstance(parcel_id, Unset):
        json_parcel_id = str(parcel_id)
    params["parcel_id"] = json_parcel_id

    json_season_id: str | Unset = UNSET
    if not isinstance(season_id, Unset):
        json_season_id = str(season_id)
    params["season_id"] = json_season_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/reports/labor-cost",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ReportLaborCostReportDto | ReportProblemDetails | None:
    if response.status_code == 200:
        response_200 = ReportLaborCostReportDto.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = ReportProblemDetails.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ReportLaborCostReportDto | ReportProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    parcel_id: UUID | Unset = UNSET,
    season_id: UUID | Unset = UNSET,

) -> Response[ReportLaborCostReportDto | ReportProblemDetails]:
    """ Chi phí nhân công theo thửa / mùa vụ

     Theo NGÀY LÀM trong [from, to] (yyyy-MM-dd, tối đa 731 ngày). Mỗi dòng = (thửa, mùa vụ): lương theo
    thời gian đã chia theo công + khoán đã chốt. parcel_id null = không gắn thửa; season_id null = ngoài
    mùa vụ. freshness = lần cuối nhận dữ liệu từ từng nguồn (null = nguồn CHƯA từng gửi, không phải 0đ).

    Args:
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        parcel_id (UUID | Unset):
        season_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReportLaborCostReportDto | ReportProblemDetails]
     """


    kwargs = _get_kwargs(
        from_=from_,
to=to,
parcel_id=parcel_id,
season_id=season_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    parcel_id: UUID | Unset = UNSET,
    season_id: UUID | Unset = UNSET,

) -> ReportLaborCostReportDto | ReportProblemDetails | None:
    """ Chi phí nhân công theo thửa / mùa vụ

     Theo NGÀY LÀM trong [from, to] (yyyy-MM-dd, tối đa 731 ngày). Mỗi dòng = (thửa, mùa vụ): lương theo
    thời gian đã chia theo công + khoán đã chốt. parcel_id null = không gắn thửa; season_id null = ngoài
    mùa vụ. freshness = lần cuối nhận dữ liệu từ từng nguồn (null = nguồn CHƯA từng gửi, không phải 0đ).

    Args:
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        parcel_id (UUID | Unset):
        season_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReportLaborCostReportDto | ReportProblemDetails
     """


    return sync_detailed(
        client=client,
from_=from_,
to=to,
parcel_id=parcel_id,
season_id=season_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    parcel_id: UUID | Unset = UNSET,
    season_id: UUID | Unset = UNSET,

) -> Response[ReportLaborCostReportDto | ReportProblemDetails]:
    """ Chi phí nhân công theo thửa / mùa vụ

     Theo NGÀY LÀM trong [from, to] (yyyy-MM-dd, tối đa 731 ngày). Mỗi dòng = (thửa, mùa vụ): lương theo
    thời gian đã chia theo công + khoán đã chốt. parcel_id null = không gắn thửa; season_id null = ngoài
    mùa vụ. freshness = lần cuối nhận dữ liệu từ từng nguồn (null = nguồn CHƯA từng gửi, không phải 0đ).

    Args:
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        parcel_id (UUID | Unset):
        season_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReportLaborCostReportDto | ReportProblemDetails]
     """


    kwargs = _get_kwargs(
        from_=from_,
to=to,
parcel_id=parcel_id,
season_id=season_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    parcel_id: UUID | Unset = UNSET,
    season_id: UUID | Unset = UNSET,

) -> ReportLaborCostReportDto | ReportProblemDetails | None:
    """ Chi phí nhân công theo thửa / mùa vụ

     Theo NGÀY LÀM trong [from, to] (yyyy-MM-dd, tối đa 731 ngày). Mỗi dòng = (thửa, mùa vụ): lương theo
    thời gian đã chia theo công + khoán đã chốt. parcel_id null = không gắn thửa; season_id null = ngoài
    mùa vụ. freshness = lần cuối nhận dữ liệu từ từng nguồn (null = nguồn CHƯA từng gửi, không phải 0đ).

    Args:
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        parcel_id (UUID | Unset):
        season_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReportLaborCostReportDto | ReportProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
from_=from_,
to=to,
parcel_id=parcel_id,
season_id=season_id,

    )).parsed
