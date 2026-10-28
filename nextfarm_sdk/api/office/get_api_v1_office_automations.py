from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_automation_dto_paged_result import OfficeAutomationDtoPagedResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    search: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trigger_type: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    table_id: UUID | Unset = UNSET,
    action_type: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    failing: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["search"] = search

    params["status"] = status

    params["triggerType"] = trigger_type

    params["createdBy"] = created_by

    json_table_id: str | Unset = UNSET
    if not isinstance(table_id, Unset):
        json_table_id = str(table_id)
    params["tableId"] = json_table_id

    params["actionType"] = action_type

    params["sort"] = sort

    params["failing"] = failing


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/automations",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeAutomationDtoPagedResult | None:
    if response.status_code == 200:
        response_200 = OfficeAutomationDtoPagedResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeAutomationDtoPagedResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    search: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trigger_type: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    table_id: UUID | Unset = UNSET,
    action_type: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    failing: bool | Unset = False,

) -> Response[OfficeAutomationDtoPagedResult]:
    """ Danh sách automation

     Phân trang ở cơ sở dữ liệu. Lọc: `status` (`active`·`inactive`·`draft`·`paused`·`archived`) ·
    `failing=true` (có lượt lỗi 7 ngày qua) · `triggerType` · `createdBy` (`me` hoặc mã người) ·
    `tableId` · `actionType`; sắp: `sort` (`updated`·`created`·`creator`·`name`, mặc định `created`).
    Mỗi dòng kèm `stepCount`, `lastRunAt`, `runs7d`, `failed7d`, `createdById`, `createdByName`,
    `updatedAt`, `triggerConfig`, `stepActionTypes[]` — `steps` để rỗng, mở chi tiết mới tải.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        search (str | Unset):
        status (str | Unset):
        trigger_type (str | Unset):
        created_by (str | Unset):
        table_id (UUID | Unset):
        action_type (str | Unset):
        sort (str | Unset):
        failing (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeAutomationDtoPagedResult]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
search=search,
status=status,
trigger_type=trigger_type,
created_by=created_by,
table_id=table_id,
action_type=action_type,
sort=sort,
failing=failing,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    search: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trigger_type: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    table_id: UUID | Unset = UNSET,
    action_type: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    failing: bool | Unset = False,

) -> OfficeAutomationDtoPagedResult | None:
    """ Danh sách automation

     Phân trang ở cơ sở dữ liệu. Lọc: `status` (`active`·`inactive`·`draft`·`paused`·`archived`) ·
    `failing=true` (có lượt lỗi 7 ngày qua) · `triggerType` · `createdBy` (`me` hoặc mã người) ·
    `tableId` · `actionType`; sắp: `sort` (`updated`·`created`·`creator`·`name`, mặc định `created`).
    Mỗi dòng kèm `stepCount`, `lastRunAt`, `runs7d`, `failed7d`, `createdById`, `createdByName`,
    `updatedAt`, `triggerConfig`, `stepActionTypes[]` — `steps` để rỗng, mở chi tiết mới tải.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        search (str | Unset):
        status (str | Unset):
        trigger_type (str | Unset):
        created_by (str | Unset):
        table_id (UUID | Unset):
        action_type (str | Unset):
        sort (str | Unset):
        failing (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeAutomationDtoPagedResult
     """


    return sync_detailed(
        client=client,
page=page,
page_size=page_size,
search=search,
status=status,
trigger_type=trigger_type,
created_by=created_by,
table_id=table_id,
action_type=action_type,
sort=sort,
failing=failing,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    search: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trigger_type: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    table_id: UUID | Unset = UNSET,
    action_type: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    failing: bool | Unset = False,

) -> Response[OfficeAutomationDtoPagedResult]:
    """ Danh sách automation

     Phân trang ở cơ sở dữ liệu. Lọc: `status` (`active`·`inactive`·`draft`·`paused`·`archived`) ·
    `failing=true` (có lượt lỗi 7 ngày qua) · `triggerType` · `createdBy` (`me` hoặc mã người) ·
    `tableId` · `actionType`; sắp: `sort` (`updated`·`created`·`creator`·`name`, mặc định `created`).
    Mỗi dòng kèm `stepCount`, `lastRunAt`, `runs7d`, `failed7d`, `createdById`, `createdByName`,
    `updatedAt`, `triggerConfig`, `stepActionTypes[]` — `steps` để rỗng, mở chi tiết mới tải.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        search (str | Unset):
        status (str | Unset):
        trigger_type (str | Unset):
        created_by (str | Unset):
        table_id (UUID | Unset):
        action_type (str | Unset):
        sort (str | Unset):
        failing (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeAutomationDtoPagedResult]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
search=search,
status=status,
trigger_type=trigger_type,
created_by=created_by,
table_id=table_id,
action_type=action_type,
sort=sort,
failing=failing,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    search: str | Unset = UNSET,
    status: str | Unset = UNSET,
    trigger_type: str | Unset = UNSET,
    created_by: str | Unset = UNSET,
    table_id: UUID | Unset = UNSET,
    action_type: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    failing: bool | Unset = False,

) -> OfficeAutomationDtoPagedResult | None:
    """ Danh sách automation

     Phân trang ở cơ sở dữ liệu. Lọc: `status` (`active`·`inactive`·`draft`·`paused`·`archived`) ·
    `failing=true` (có lượt lỗi 7 ngày qua) · `triggerType` · `createdBy` (`me` hoặc mã người) ·
    `tableId` · `actionType`; sắp: `sort` (`updated`·`created`·`creator`·`name`, mặc định `created`).
    Mỗi dòng kèm `stepCount`, `lastRunAt`, `runs7d`, `failed7d`, `createdById`, `createdByName`,
    `updatedAt`, `triggerConfig`, `stepActionTypes[]` — `steps` để rỗng, mở chi tiết mới tải.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        search (str | Unset):
        status (str | Unset):
        trigger_type (str | Unset):
        created_by (str | Unset):
        table_id (UUID | Unset):
        action_type (str | Unset):
        sort (str | Unset):
        failing (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeAutomationDtoPagedResult
     """


    return (await asyncio_detailed(
        client=client,
page=page,
page_size=page_size,
search=search,
status=status,
trigger_type=trigger_type,
created_by=created_by,
table_id=table_id,
action_type=action_type,
sort=sort,
failing=failing,

    )).parsed
