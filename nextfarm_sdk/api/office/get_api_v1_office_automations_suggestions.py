from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_automation_suggestion_dto import OfficeAutomationSuggestionDto
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/automations/suggestions",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[OfficeAutomationSuggestionDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = OfficeAutomationSuggestionDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[OfficeAutomationSuggestionDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[OfficeAutomationSuggestionDto]]:
    """ Gợi ý tự động hoá riêng cho công ty (tab Gợi ý)

     Tối đa 3 thẻ `[{ kind, triggerType, actionType, tableId, tableName, fieldId, fieldName, offsetDays,
    evidenceCount, evidenceDays, existingAutomationId, existingAutomationName, existingStatus,
    existingRuns, existingFailed }]` dựng từ dữ liệu thật: `date_expiring` = cột Ngày tên kiểu "Ngày hết
    hạn" có dòng tới hạn trong 30 ngày tới (mời luật "Khi tới ngày", 30 ngày trước); `busy_table` = bảng
    nhiều dòng mới 30 ngày qua mà chưa luật nào nghe. Có `existingAutomationId` = công ty đã có luật này
    (kèm số lượt/số hỏng 30 ngày qua). Máy chủ chỉ trả mã + số, câu chữ do giao diện dịch. Chỉ đọc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeAutomationSuggestionDto]]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> list[OfficeAutomationSuggestionDto] | None:
    """ Gợi ý tự động hoá riêng cho công ty (tab Gợi ý)

     Tối đa 3 thẻ `[{ kind, triggerType, actionType, tableId, tableName, fieldId, fieldName, offsetDays,
    evidenceCount, evidenceDays, existingAutomationId, existingAutomationName, existingStatus,
    existingRuns, existingFailed }]` dựng từ dữ liệu thật: `date_expiring` = cột Ngày tên kiểu "Ngày hết
    hạn" có dòng tới hạn trong 30 ngày tới (mời luật "Khi tới ngày", 30 ngày trước); `busy_table` = bảng
    nhiều dòng mới 30 ngày qua mà chưa luật nào nghe. Có `existingAutomationId` = công ty đã có luật này
    (kèm số lượt/số hỏng 30 ngày qua). Máy chủ chỉ trả mã + số, câu chữ do giao diện dịch. Chỉ đọc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeAutomationSuggestionDto]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[OfficeAutomationSuggestionDto]]:
    """ Gợi ý tự động hoá riêng cho công ty (tab Gợi ý)

     Tối đa 3 thẻ `[{ kind, triggerType, actionType, tableId, tableName, fieldId, fieldName, offsetDays,
    evidenceCount, evidenceDays, existingAutomationId, existingAutomationName, existingStatus,
    existingRuns, existingFailed }]` dựng từ dữ liệu thật: `date_expiring` = cột Ngày tên kiểu "Ngày hết
    hạn" có dòng tới hạn trong 30 ngày tới (mời luật "Khi tới ngày", 30 ngày trước); `busy_table` = bảng
    nhiều dòng mới 30 ngày qua mà chưa luật nào nghe. Có `existingAutomationId` = công ty đã có luật này
    (kèm số lượt/số hỏng 30 ngày qua). Máy chủ chỉ trả mã + số, câu chữ do giao diện dịch. Chỉ đọc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeAutomationSuggestionDto]]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> list[OfficeAutomationSuggestionDto] | None:
    """ Gợi ý tự động hoá riêng cho công ty (tab Gợi ý)

     Tối đa 3 thẻ `[{ kind, triggerType, actionType, tableId, tableName, fieldId, fieldName, offsetDays,
    evidenceCount, evidenceDays, existingAutomationId, existingAutomationName, existingStatus,
    existingRuns, existingFailed }]` dựng từ dữ liệu thật: `date_expiring` = cột Ngày tên kiểu "Ngày hết
    hạn" có dòng tới hạn trong 30 ngày tới (mời luật "Khi tới ngày", 30 ngày trước); `busy_table` = bảng
    nhiều dòng mới 30 ngày qua mà chưa luật nào nghe. Có `existingAutomationId` = công ty đã có luật này
    (kèm số lượt/số hỏng 30 ngày qua). Máy chủ chỉ trả mã + số, câu chữ do giao diện dịch. Chỉ đọc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeAutomationSuggestionDto]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
