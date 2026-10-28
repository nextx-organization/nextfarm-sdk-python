from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_aggregate_records_request import OfficeAggregateRecordsRequest
from ...models.office_column_aggregate_dto import OfficeColumnAggregateDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    table_id: UUID,
    *,
    body: OfficeAggregateRecordsRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/office/tables/{table_id}/records/aggregate".format(table_id=quote(str(table_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[OfficeColumnAggregateDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = OfficeColumnAggregateDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[OfficeColumnAggregateDto]]:
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
    body: OfficeAggregateRecordsRequest | Unset = UNSET,

) -> Response[list[OfficeColumnAggregateDto]]:
    """ Cộng gộp theo cột (tổng · trung bình · nhỏ nhất · lớn nhất · đếm)

     Năm con số của thanh chân bảng, tính trên tập ĐANG LỌC — gửi kèm đúng bộ lọc mà lưới đang áp. Cộng ở
    máy chủ chứ không cộng trong lưới: lưới chỉ giữ vài trăm dòng quanh vùng cuộn, nên cộng những gì nó
    đang cầm sẽ cho ra con số NHẢY khi người dùng cuộn.

    Cột nằm ngoài phạm vi được xem bị loại khỏi kết quả. Không phải bộ máy công thức: không có cú pháp,
    không có vùng `A1:A10`, không lưu giá trị nào.

    Args:
        table_id (UUID):
        body (OfficeAggregateRecordsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeColumnAggregateDto]]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    table_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: OfficeAggregateRecordsRequest | Unset = UNSET,

) -> list[OfficeColumnAggregateDto] | None:
    """ Cộng gộp theo cột (tổng · trung bình · nhỏ nhất · lớn nhất · đếm)

     Năm con số của thanh chân bảng, tính trên tập ĐANG LỌC — gửi kèm đúng bộ lọc mà lưới đang áp. Cộng ở
    máy chủ chứ không cộng trong lưới: lưới chỉ giữ vài trăm dòng quanh vùng cuộn, nên cộng những gì nó
    đang cầm sẽ cho ra con số NHẢY khi người dùng cuộn.

    Cột nằm ngoài phạm vi được xem bị loại khỏi kết quả. Không phải bộ máy công thức: không có cú pháp,
    không có vùng `A1:A10`, không lưu giá trị nào.

    Args:
        table_id (UUID):
        body (OfficeAggregateRecordsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeColumnAggregateDto]
     """


    return sync_detailed(
        table_id=table_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    table_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: OfficeAggregateRecordsRequest | Unset = UNSET,

) -> Response[list[OfficeColumnAggregateDto]]:
    """ Cộng gộp theo cột (tổng · trung bình · nhỏ nhất · lớn nhất · đếm)

     Năm con số của thanh chân bảng, tính trên tập ĐANG LỌC — gửi kèm đúng bộ lọc mà lưới đang áp. Cộng ở
    máy chủ chứ không cộng trong lưới: lưới chỉ giữ vài trăm dòng quanh vùng cuộn, nên cộng những gì nó
    đang cầm sẽ cho ra con số NHẢY khi người dùng cuộn.

    Cột nằm ngoài phạm vi được xem bị loại khỏi kết quả. Không phải bộ máy công thức: không có cú pháp,
    không có vùng `A1:A10`, không lưu giá trị nào.

    Args:
        table_id (UUID):
        body (OfficeAggregateRecordsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeColumnAggregateDto]]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    table_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: OfficeAggregateRecordsRequest | Unset = UNSET,

) -> list[OfficeColumnAggregateDto] | None:
    """ Cộng gộp theo cột (tổng · trung bình · nhỏ nhất · lớn nhất · đếm)

     Năm con số của thanh chân bảng, tính trên tập ĐANG LỌC — gửi kèm đúng bộ lọc mà lưới đang áp. Cộng ở
    máy chủ chứ không cộng trong lưới: lưới chỉ giữ vài trăm dòng quanh vùng cuộn, nên cộng những gì nó
    đang cầm sẽ cho ra con số NHẢY khi người dùng cuộn.

    Cột nằm ngoài phạm vi được xem bị loại khỏi kết quả. Không phải bộ máy công thức: không có cú pháp,
    không có vùng `A1:A10`, không lưu giá trị nào.

    Args:
        table_id (UUID):
        body (OfficeAggregateRecordsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeColumnAggregateDto]
     """


    return (await asyncio_detailed(
        table_id=table_id,
client=client,
body=body,

    )).parsed
