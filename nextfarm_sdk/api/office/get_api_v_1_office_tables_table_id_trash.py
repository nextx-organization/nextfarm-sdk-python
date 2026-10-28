from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_trashed_record_dto_paged_result import OfficeTrashedRecordDtoPagedResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    table_id: UUID,
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/tables/{table_id}/trash".format(table_id=quote(str(table_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeTrashedRecordDtoPagedResult | None:
    if response.status_code == 200:
        response_200 = OfficeTrashedRecordDtoPagedResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeTrashedRecordDtoPagedResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[OfficeTrashedRecordDtoPagedResult]:
    """ Thùng rác — record đã xoá mềm của bảng (phân trang)

     Chỉ record của công ty hiện tại; dữ liệu còn nguyên, có thể khôi phục hoặc xoá cứng.

    Args:
        table_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeTrashedRecordDtoPagedResult]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
page=page,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    table_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> OfficeTrashedRecordDtoPagedResult | None:
    """ Thùng rác — record đã xoá mềm của bảng (phân trang)

     Chỉ record của công ty hiện tại; dữ liệu còn nguyên, có thể khôi phục hoặc xoá cứng.

    Args:
        table_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeTrashedRecordDtoPagedResult
     """


    return sync_detailed(
        table_id=table_id,
client=client,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    table_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[OfficeTrashedRecordDtoPagedResult]:
    """ Thùng rác — record đã xoá mềm của bảng (phân trang)

     Chỉ record của công ty hiện tại; dữ liệu còn nguyên, có thể khôi phục hoặc xoá cứng.

    Args:
        table_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeTrashedRecordDtoPagedResult]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
page=page,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    table_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> OfficeTrashedRecordDtoPagedResult | None:
    """ Thùng rác — record đã xoá mềm của bảng (phân trang)

     Chỉ record của công ty hiện tại; dữ liệu còn nguyên, có thể khôi phục hoặc xoá cứng.

    Args:
        table_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeTrashedRecordDtoPagedResult
     """


    return (await asyncio_detailed(
        table_id=table_id,
client=client,
page=page,
page_size=page_size,

    )).parsed
