from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_event_dto import OfficeEventDto
from ...models.office_problem_details import OfficeProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    id: UUID,
    *,
    occurrence_start: datetime.datetime | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_occurrence_start: str | Unset = UNSET
    if not isinstance(occurrence_start, Unset):
        json_occurrence_start = occurrence_start.isoformat()
    params["occurrenceStart"] = json_occurrence_start


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/events/{id}".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeEventDto | OfficeProblemDetails | None:
    if response.status_code == 200:
        response_200 = OfficeEventDto.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = OfficeProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeEventDto | OfficeProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    occurrence_start: datetime.datetime | Unset = UNSET,

) -> Response[OfficeEventDto | OfficeProblemDetails]:
    """ Chi tiết một sự kiện kèm người dự và phòng đã giữ

     occurrenceStart là mốc GỐC của một lần trong chuỗi lặp — có kèm thì tiêu đề, giờ, mô tả, địa điểm
    trả về là bản ĐÃ ÁP ngoại lệ của đúng lần đó, không phải bản chung của cả chuỗi. Bỏ trống khi sự
    kiện không lặp, hoặc khi cần xem/sửa cả chuỗi (scope=all).

    Args:
        id (UUID):
        occurrence_start (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeEventDto | OfficeProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,
occurrence_start=occurrence_start,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    occurrence_start: datetime.datetime | Unset = UNSET,

) -> OfficeEventDto | OfficeProblemDetails | None:
    """ Chi tiết một sự kiện kèm người dự và phòng đã giữ

     occurrenceStart là mốc GỐC của một lần trong chuỗi lặp — có kèm thì tiêu đề, giờ, mô tả, địa điểm
    trả về là bản ĐÃ ÁP ngoại lệ của đúng lần đó, không phải bản chung của cả chuỗi. Bỏ trống khi sự
    kiện không lặp, hoặc khi cần xem/sửa cả chuỗi (scope=all).

    Args:
        id (UUID):
        occurrence_start (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeEventDto | OfficeProblemDetails
     """


    return sync_detailed(
        id=id,
client=client,
occurrence_start=occurrence_start,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    occurrence_start: datetime.datetime | Unset = UNSET,

) -> Response[OfficeEventDto | OfficeProblemDetails]:
    """ Chi tiết một sự kiện kèm người dự và phòng đã giữ

     occurrenceStart là mốc GỐC của một lần trong chuỗi lặp — có kèm thì tiêu đề, giờ, mô tả, địa điểm
    trả về là bản ĐÃ ÁP ngoại lệ của đúng lần đó, không phải bản chung của cả chuỗi. Bỏ trống khi sự
    kiện không lặp, hoặc khi cần xem/sửa cả chuỗi (scope=all).

    Args:
        id (UUID):
        occurrence_start (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeEventDto | OfficeProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,
occurrence_start=occurrence_start,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    occurrence_start: datetime.datetime | Unset = UNSET,

) -> OfficeEventDto | OfficeProblemDetails | None:
    """ Chi tiết một sự kiện kèm người dự và phòng đã giữ

     occurrenceStart là mốc GỐC của một lần trong chuỗi lặp — có kèm thì tiêu đề, giờ, mô tả, địa điểm
    trả về là bản ĐÃ ÁP ngoại lệ của đúng lần đó, không phải bản chung của cả chuỗi. Bỏ trống khi sự
    kiện không lặp, hoặc khi cần xem/sửa cả chuỗi (scope=all).

    Args:
        id (UUID):
        occurrence_start (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeEventDto | OfficeProblemDetails
     """


    return (await asyncio_detailed(
        id=id,
client=client,
occurrence_start=occurrence_start,

    )).parsed
