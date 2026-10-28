from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_automation_merge_field_group_dto import OfficeAutomationMergeFieldGroupDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    table_id: UUID | Unset = UNSET,
    trigger_type: str | Unset = UNSET,
    automation_id: UUID | Unset = UNSET,
    step_id: UUID | Unset = UNSET,
    event_type: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_table_id: str | Unset = UNSET
    if not isinstance(table_id, Unset):
        json_table_id = str(table_id)
    params["tableId"] = json_table_id

    params["triggerType"] = trigger_type

    json_automation_id: str | Unset = UNSET
    if not isinstance(automation_id, Unset):
        json_automation_id = str(automation_id)
    params["automationId"] = json_automation_id

    json_step_id: str | Unset = UNSET
    if not isinstance(step_id, Unset):
        json_step_id = str(step_id)
    params["stepId"] = json_step_id

    params["eventType"] = event_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/automations/merge-fields",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[OfficeAutomationMergeFieldGroupDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = OfficeAutomationMergeFieldGroupDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[OfficeAutomationMergeFieldGroupDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    table_id: UUID | Unset = UNSET,
    trigger_type: str | Unset = UNSET,
    automation_id: UUID | Unset = UNSET,
    step_id: UUID | Unset = UNSET,
    event_type: str | Unset = UNSET,

) -> Response[list[OfficeAutomationMergeFieldGroupDto]]:
    """ Danh mục biến {{…}} chèn được vào cấu hình hành động

     Cho ô "chèn biến" của trình dựng luật. `triggerType` = mã kích hoạt của luật ⇒ thêm nhóm `system`
    (`now`, `today`, `createdBy`) và nhóm `trigger` theo mã (vd `before.<cột>`, `changedFields`,
    `trigger.runNumber`, `trigger.clickedByName`).`tableId` = bảng kích hoạt của luật; bỏ trống thì chỉ
    có nhóm dữ liệu kích hoạt. Mỗi mục có `token` — chữ đặt giữa `{{ }}`. Mọi ô chữ trong cấu hình của
    MỌI hành động đều điền được biến; biến không tra được lúc chạy thì nằm nguyên văn trong kết quả
    (Chạy thử liệt kê chúng ở `unresolved`). `automationId` + `stepId` ⇒ thêm nhóm `scope = "step"` (kèm
    `stepId`) cho MỖI bước Tìm dòng / Thêm dòng đứng trước bước đó: `steps.<mã bước>.recordIds` ·
    `.count` · `.<Tên cột>` · `.first.<Tên cột>`. `stepId` chưa có trong luật (bước sắp thêm) ⇒ coi như
    bước cuối. Đợt 4: `message_received` ⇒ `trigger.text` · `senderName` · `attachments` ·
    `mentionNames` · `channelName` · `link`…; `service_event` ⇒ `trigger.payload.<khoá>` theo danh mục
    của `eventType` (tham số, hoặc đọc từ cấu hình của `automationId`).

    Args:
        table_id (UUID | Unset):
        trigger_type (str | Unset):
        automation_id (UUID | Unset):
        step_id (UUID | Unset):
        event_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeAutomationMergeFieldGroupDto]]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
trigger_type=trigger_type,
automation_id=automation_id,
step_id=step_id,
event_type=event_type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    table_id: UUID | Unset = UNSET,
    trigger_type: str | Unset = UNSET,
    automation_id: UUID | Unset = UNSET,
    step_id: UUID | Unset = UNSET,
    event_type: str | Unset = UNSET,

) -> list[OfficeAutomationMergeFieldGroupDto] | None:
    """ Danh mục biến {{…}} chèn được vào cấu hình hành động

     Cho ô "chèn biến" của trình dựng luật. `triggerType` = mã kích hoạt của luật ⇒ thêm nhóm `system`
    (`now`, `today`, `createdBy`) và nhóm `trigger` theo mã (vd `before.<cột>`, `changedFields`,
    `trigger.runNumber`, `trigger.clickedByName`).`tableId` = bảng kích hoạt của luật; bỏ trống thì chỉ
    có nhóm dữ liệu kích hoạt. Mỗi mục có `token` — chữ đặt giữa `{{ }}`. Mọi ô chữ trong cấu hình của
    MỌI hành động đều điền được biến; biến không tra được lúc chạy thì nằm nguyên văn trong kết quả
    (Chạy thử liệt kê chúng ở `unresolved`). `automationId` + `stepId` ⇒ thêm nhóm `scope = "step"` (kèm
    `stepId`) cho MỖI bước Tìm dòng / Thêm dòng đứng trước bước đó: `steps.<mã bước>.recordIds` ·
    `.count` · `.<Tên cột>` · `.first.<Tên cột>`. `stepId` chưa có trong luật (bước sắp thêm) ⇒ coi như
    bước cuối. Đợt 4: `message_received` ⇒ `trigger.text` · `senderName` · `attachments` ·
    `mentionNames` · `channelName` · `link`…; `service_event` ⇒ `trigger.payload.<khoá>` theo danh mục
    của `eventType` (tham số, hoặc đọc từ cấu hình của `automationId`).

    Args:
        table_id (UUID | Unset):
        trigger_type (str | Unset):
        automation_id (UUID | Unset):
        step_id (UUID | Unset):
        event_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeAutomationMergeFieldGroupDto]
     """


    return sync_detailed(
        client=client,
table_id=table_id,
trigger_type=trigger_type,
automation_id=automation_id,
step_id=step_id,
event_type=event_type,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    table_id: UUID | Unset = UNSET,
    trigger_type: str | Unset = UNSET,
    automation_id: UUID | Unset = UNSET,
    step_id: UUID | Unset = UNSET,
    event_type: str | Unset = UNSET,

) -> Response[list[OfficeAutomationMergeFieldGroupDto]]:
    """ Danh mục biến {{…}} chèn được vào cấu hình hành động

     Cho ô "chèn biến" của trình dựng luật. `triggerType` = mã kích hoạt của luật ⇒ thêm nhóm `system`
    (`now`, `today`, `createdBy`) và nhóm `trigger` theo mã (vd `before.<cột>`, `changedFields`,
    `trigger.runNumber`, `trigger.clickedByName`).`tableId` = bảng kích hoạt của luật; bỏ trống thì chỉ
    có nhóm dữ liệu kích hoạt. Mỗi mục có `token` — chữ đặt giữa `{{ }}`. Mọi ô chữ trong cấu hình của
    MỌI hành động đều điền được biến; biến không tra được lúc chạy thì nằm nguyên văn trong kết quả
    (Chạy thử liệt kê chúng ở `unresolved`). `automationId` + `stepId` ⇒ thêm nhóm `scope = "step"` (kèm
    `stepId`) cho MỖI bước Tìm dòng / Thêm dòng đứng trước bước đó: `steps.<mã bước>.recordIds` ·
    `.count` · `.<Tên cột>` · `.first.<Tên cột>`. `stepId` chưa có trong luật (bước sắp thêm) ⇒ coi như
    bước cuối. Đợt 4: `message_received` ⇒ `trigger.text` · `senderName` · `attachments` ·
    `mentionNames` · `channelName` · `link`…; `service_event` ⇒ `trigger.payload.<khoá>` theo danh mục
    của `eventType` (tham số, hoặc đọc từ cấu hình của `automationId`).

    Args:
        table_id (UUID | Unset):
        trigger_type (str | Unset):
        automation_id (UUID | Unset):
        step_id (UUID | Unset):
        event_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeAutomationMergeFieldGroupDto]]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
trigger_type=trigger_type,
automation_id=automation_id,
step_id=step_id,
event_type=event_type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    table_id: UUID | Unset = UNSET,
    trigger_type: str | Unset = UNSET,
    automation_id: UUID | Unset = UNSET,
    step_id: UUID | Unset = UNSET,
    event_type: str | Unset = UNSET,

) -> list[OfficeAutomationMergeFieldGroupDto] | None:
    """ Danh mục biến {{…}} chèn được vào cấu hình hành động

     Cho ô "chèn biến" của trình dựng luật. `triggerType` = mã kích hoạt của luật ⇒ thêm nhóm `system`
    (`now`, `today`, `createdBy`) và nhóm `trigger` theo mã (vd `before.<cột>`, `changedFields`,
    `trigger.runNumber`, `trigger.clickedByName`).`tableId` = bảng kích hoạt của luật; bỏ trống thì chỉ
    có nhóm dữ liệu kích hoạt. Mỗi mục có `token` — chữ đặt giữa `{{ }}`. Mọi ô chữ trong cấu hình của
    MỌI hành động đều điền được biến; biến không tra được lúc chạy thì nằm nguyên văn trong kết quả
    (Chạy thử liệt kê chúng ở `unresolved`). `automationId` + `stepId` ⇒ thêm nhóm `scope = "step"` (kèm
    `stepId`) cho MỖI bước Tìm dòng / Thêm dòng đứng trước bước đó: `steps.<mã bước>.recordIds` ·
    `.count` · `.<Tên cột>` · `.first.<Tên cột>`. `stepId` chưa có trong luật (bước sắp thêm) ⇒ coi như
    bước cuối. Đợt 4: `message_received` ⇒ `trigger.text` · `senderName` · `attachments` ·
    `mentionNames` · `channelName` · `link`…; `service_event` ⇒ `trigger.payload.<khoá>` theo danh mục
    của `eventType` (tham số, hoặc đọc từ cấu hình của `automationId`).

    Args:
        table_id (UUID | Unset):
        trigger_type (str | Unset):
        automation_id (UUID | Unset):
        step_id (UUID | Unset):
        event_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeAutomationMergeFieldGroupDto]
     """


    return (await asyncio_detailed(
        client=client,
table_id=table_id,
trigger_type=trigger_type,
automation_id=automation_id,
step_id=step_id,
event_type=event_type,

    )).parsed
