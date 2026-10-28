from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_automation_run_dto_paged_result import OfficeAutomationRunDtoPagedResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    automation_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    result: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_automation_id: str | Unset = UNSET
    if not isinstance(automation_id, Unset):
        json_automation_id = str(automation_id)
    params["automationId"] = json_automation_id

    params["page"] = page

    params["pageSize"] = page_size

    params["result"] = result

    params["createdBy"] = created_by

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["search"] = search


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/automation-logs/runs",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeAutomationRunDtoPagedResult | None:
    if response.status_code == 200:
        response_200 = OfficeAutomationRunDtoPagedResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeAutomationRunDtoPagedResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    automation_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    result: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,

) -> Response[OfficeAutomationRunDtoPagedResult]:
    """ Lịch sử theo LƯỢT CHẠY, mới nhất trước

     Một lượt = một dòng dữ liệu đi qua luật một lần (gom theo `enrollmentId`). Mỗi lượt: bắt đầu/kết
    thúc, số bước, số hỏng/bỏ qua/xong và `result` tổng (failed > success > skipped). Mở chi tiết một
    lượt: `GET /automation-logs?enrollmentId=`. Lọc ở máy chủ: `result` (success|failed|skipped|running)
    · `createdBy` (me|mã người — người tạo luật) · `from`/`to` (mốc bắt đầu lượt, bao gồm) · `search`
    (tên luật, hoặc đúng mã lượt/dòng/luật).

    Args:
        automation_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        result (str | Unset):
        created_by (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeAutomationRunDtoPagedResult]
     """


    kwargs = _get_kwargs(
        automation_id=automation_id,
page=page,
page_size=page_size,
result=result,
created_by=created_by,
from_=from_,
to=to,
search=search,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    automation_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    result: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,

) -> OfficeAutomationRunDtoPagedResult | None:
    """ Lịch sử theo LƯỢT CHẠY, mới nhất trước

     Một lượt = một dòng dữ liệu đi qua luật một lần (gom theo `enrollmentId`). Mỗi lượt: bắt đầu/kết
    thúc, số bước, số hỏng/bỏ qua/xong và `result` tổng (failed > success > skipped). Mở chi tiết một
    lượt: `GET /automation-logs?enrollmentId=`. Lọc ở máy chủ: `result` (success|failed|skipped|running)
    · `createdBy` (me|mã người — người tạo luật) · `from`/`to` (mốc bắt đầu lượt, bao gồm) · `search`
    (tên luật, hoặc đúng mã lượt/dòng/luật).

    Args:
        automation_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        result (str | Unset):
        created_by (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeAutomationRunDtoPagedResult
     """


    return sync_detailed(
        client=client,
automation_id=automation_id,
page=page,
page_size=page_size,
result=result,
created_by=created_by,
from_=from_,
to=to,
search=search,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    automation_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    result: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,

) -> Response[OfficeAutomationRunDtoPagedResult]:
    """ Lịch sử theo LƯỢT CHẠY, mới nhất trước

     Một lượt = một dòng dữ liệu đi qua luật một lần (gom theo `enrollmentId`). Mỗi lượt: bắt đầu/kết
    thúc, số bước, số hỏng/bỏ qua/xong và `result` tổng (failed > success > skipped). Mở chi tiết một
    lượt: `GET /automation-logs?enrollmentId=`. Lọc ở máy chủ: `result` (success|failed|skipped|running)
    · `createdBy` (me|mã người — người tạo luật) · `from`/`to` (mốc bắt đầu lượt, bao gồm) · `search`
    (tên luật, hoặc đúng mã lượt/dòng/luật).

    Args:
        automation_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        result (str | Unset):
        created_by (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeAutomationRunDtoPagedResult]
     """


    kwargs = _get_kwargs(
        automation_id=automation_id,
page=page,
page_size=page_size,
result=result,
created_by=created_by,
from_=from_,
to=to,
search=search,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    automation_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    result: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    search: str | Unset = UNSET,

) -> OfficeAutomationRunDtoPagedResult | None:
    """ Lịch sử theo LƯỢT CHẠY, mới nhất trước

     Một lượt = một dòng dữ liệu đi qua luật một lần (gom theo `enrollmentId`). Mỗi lượt: bắt đầu/kết
    thúc, số bước, số hỏng/bỏ qua/xong và `result` tổng (failed > success > skipped). Mở chi tiết một
    lượt: `GET /automation-logs?enrollmentId=`. Lọc ở máy chủ: `result` (success|failed|skipped|running)
    · `createdBy` (me|mã người — người tạo luật) · `from`/`to` (mốc bắt đầu lượt, bao gồm) · `search`
    (tên luật, hoặc đúng mã lượt/dòng/luật).

    Args:
        automation_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        result (str | Unset):
        created_by (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeAutomationRunDtoPagedResult
     """


    return (await asyncio_detailed(
        client=client,
automation_id=automation_id,
page=page,
page_size=page_size,
result=result,
created_by=created_by,
from_=from_,
to=to,
search=search,

    )).parsed
