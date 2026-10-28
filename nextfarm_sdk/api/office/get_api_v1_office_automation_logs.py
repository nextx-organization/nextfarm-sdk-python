from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_automation_run_log_dto_paged_result import OfficeAutomationRunLogDtoPagedResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    automation_id: UUID | Unset = UNSET,
    result: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    enrollment_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_automation_id: str | Unset = UNSET
    if not isinstance(automation_id, Unset):
        json_automation_id = str(automation_id)
    params["automationId"] = json_automation_id

    params["result"] = result

    params["page"] = page

    params["pageSize"] = page_size

    json_enrollment_id: str | Unset = UNSET
    if not isinstance(enrollment_id, Unset):
        json_enrollment_id = str(enrollment_id)
    params["enrollmentId"] = json_enrollment_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/automation-logs",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeAutomationRunLogDtoPagedResult | None:
    if response.status_code == 200:
        response_200 = OfficeAutomationRunLogDtoPagedResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeAutomationRunLogDtoPagedResult]:
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
    result: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    enrollment_id: UUID | Unset = UNSET,

) -> Response[OfficeAutomationRunLogDtoPagedResult]:
    """ Nhật ký chạy, mới nhất trước

     `result` lọc theo MÃ: success · skipped · failed. Bỏ trống thì trả về mọi kết quả.

    Args:
        automation_id (UUID | Unset):
        result (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        enrollment_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeAutomationRunLogDtoPagedResult]
     """


    kwargs = _get_kwargs(
        automation_id=automation_id,
result=result,
page=page,
page_size=page_size,
enrollment_id=enrollment_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    automation_id: UUID | Unset = UNSET,
    result: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    enrollment_id: UUID | Unset = UNSET,

) -> OfficeAutomationRunLogDtoPagedResult | None:
    """ Nhật ký chạy, mới nhất trước

     `result` lọc theo MÃ: success · skipped · failed. Bỏ trống thì trả về mọi kết quả.

    Args:
        automation_id (UUID | Unset):
        result (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        enrollment_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeAutomationRunLogDtoPagedResult
     """


    return sync_detailed(
        client=client,
automation_id=automation_id,
result=result,
page=page,
page_size=page_size,
enrollment_id=enrollment_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    automation_id: UUID | Unset = UNSET,
    result: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    enrollment_id: UUID | Unset = UNSET,

) -> Response[OfficeAutomationRunLogDtoPagedResult]:
    """ Nhật ký chạy, mới nhất trước

     `result` lọc theo MÃ: success · skipped · failed. Bỏ trống thì trả về mọi kết quả.

    Args:
        automation_id (UUID | Unset):
        result (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        enrollment_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeAutomationRunLogDtoPagedResult]
     """


    kwargs = _get_kwargs(
        automation_id=automation_id,
result=result,
page=page,
page_size=page_size,
enrollment_id=enrollment_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    automation_id: UUID | Unset = UNSET,
    result: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    enrollment_id: UUID | Unset = UNSET,

) -> OfficeAutomationRunLogDtoPagedResult | None:
    """ Nhật ký chạy, mới nhất trước

     `result` lọc theo MÃ: success · skipped · failed. Bỏ trống thì trả về mọi kết quả.

    Args:
        automation_id (UUID | Unset):
        result (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        enrollment_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeAutomationRunLogDtoPagedResult
     """


    return (await asyncio_detailed(
        client=client,
automation_id=automation_id,
result=result,
page=page,
page_size=page_size,
enrollment_id=enrollment_id,

    )).parsed
