from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_calendar_list_result_dto import OfficeCalendarListResultDto
from ...models.office_problem_details import OfficeProblemDetails
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    event_type: str | Unset = UNSET,
    mine_only: bool | Unset = False,

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

    params["eventType"] = event_type

    params["mineOnly"] = mine_only


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/events",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeCalendarListResultDto | OfficeProblemDetails | None:
    if response.status_code == 200:
        response_200 = OfficeCalendarListResultDto.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = OfficeProblemDetails.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeCalendarListResultDto | OfficeProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    event_type: str | Unset = UNSET,
    mine_only: bool | Unset = False,

) -> Response[OfficeCalendarListResultDto | OfficeProblemDetails]:
    """ Sự kiện trong một khoảng thời gian

     Dùng cho lịch tuần và lịch tháng. Khoảng hỏi tối đa 120 ngày. eventType và status trả về là MÃ tiếng
    Anh. truncated=true nghĩa là danh sách bị cắt bởi trần an toàn (quá nhiều sự kiện hoặc quá nhiều lần
    lặp trong khung đang xem) — hẹp lại khoảng hỏi để xem đủ.

    Args:
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        event_type (str | Unset):
        mine_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeCalendarListResultDto | OfficeProblemDetails]
     """


    kwargs = _get_kwargs(
        from_=from_,
to=to,
event_type=event_type,
mine_only=mine_only,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    event_type: str | Unset = UNSET,
    mine_only: bool | Unset = False,

) -> OfficeCalendarListResultDto | OfficeProblemDetails | None:
    """ Sự kiện trong một khoảng thời gian

     Dùng cho lịch tuần và lịch tháng. Khoảng hỏi tối đa 120 ngày. eventType và status trả về là MÃ tiếng
    Anh. truncated=true nghĩa là danh sách bị cắt bởi trần an toàn (quá nhiều sự kiện hoặc quá nhiều lần
    lặp trong khung đang xem) — hẹp lại khoảng hỏi để xem đủ.

    Args:
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        event_type (str | Unset):
        mine_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeCalendarListResultDto | OfficeProblemDetails
     """


    return sync_detailed(
        client=client,
from_=from_,
to=to,
event_type=event_type,
mine_only=mine_only,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    event_type: str | Unset = UNSET,
    mine_only: bool | Unset = False,

) -> Response[OfficeCalendarListResultDto | OfficeProblemDetails]:
    """ Sự kiện trong một khoảng thời gian

     Dùng cho lịch tuần và lịch tháng. Khoảng hỏi tối đa 120 ngày. eventType và status trả về là MÃ tiếng
    Anh. truncated=true nghĩa là danh sách bị cắt bởi trần an toàn (quá nhiều sự kiện hoặc quá nhiều lần
    lặp trong khung đang xem) — hẹp lại khoảng hỏi để xem đủ.

    Args:
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        event_type (str | Unset):
        mine_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeCalendarListResultDto | OfficeProblemDetails]
     """


    kwargs = _get_kwargs(
        from_=from_,
to=to,
event_type=event_type,
mine_only=mine_only,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    event_type: str | Unset = UNSET,
    mine_only: bool | Unset = False,

) -> OfficeCalendarListResultDto | OfficeProblemDetails | None:
    """ Sự kiện trong một khoảng thời gian

     Dùng cho lịch tuần và lịch tháng. Khoảng hỏi tối đa 120 ngày. eventType và status trả về là MÃ tiếng
    Anh. truncated=true nghĩa là danh sách bị cắt bởi trần an toàn (quá nhiều sự kiện hoặc quá nhiều lần
    lặp trong khung đang xem) — hẹp lại khoảng hỏi để xem đủ.

    Args:
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        event_type (str | Unset):
        mine_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeCalendarListResultDto | OfficeProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
from_=from_,
to=to,
event_type=event_type,
mine_only=mine_only,

    )).parsed
