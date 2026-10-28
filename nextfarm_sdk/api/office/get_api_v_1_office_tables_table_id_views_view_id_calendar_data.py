from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_calendar_event_dto import OfficeCalendarEventDto
from ...models.office_problem_details import OfficeProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    table_id: UUID,
    view_id: UUID,
    *,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,

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


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/tables/{table_id}/views/{view_id}/calendar-data".format(table_id=quote(str(table_id), safe=""),view_id=quote(str(view_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeProblemDetails | list[OfficeCalendarEventDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = OfficeCalendarEventDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = OfficeProblemDetails.from_dict(response.json())



        return response_400

    if response.status_code == 404:
        response_404 = OfficeProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeProblemDetails | list[OfficeCalendarEventDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_id: UUID,
    view_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,

) -> Response[OfficeProblemDetails | list[OfficeCalendarEventDto]]:
    """ Record trong khoảng ngày của view kiểu Calendar

     Ánh xạ trường ngày (startField/endField) trong property; from/to lọc theo ngày bắt đầu.

    Args:
        table_id (UUID):
        view_id (UUID):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeProblemDetails | list[OfficeCalendarEventDto]]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
view_id=view_id,
from_=from_,
to=to,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    table_id: UUID,
    view_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,

) -> OfficeProblemDetails | list[OfficeCalendarEventDto] | None:
    """ Record trong khoảng ngày của view kiểu Calendar

     Ánh xạ trường ngày (startField/endField) trong property; from/to lọc theo ngày bắt đầu.

    Args:
        table_id (UUID):
        view_id (UUID):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeProblemDetails | list[OfficeCalendarEventDto]
     """


    return sync_detailed(
        table_id=table_id,
view_id=view_id,
client=client,
from_=from_,
to=to,

    ).parsed

async def asyncio_detailed(
    table_id: UUID,
    view_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,

) -> Response[OfficeProblemDetails | list[OfficeCalendarEventDto]]:
    """ Record trong khoảng ngày của view kiểu Calendar

     Ánh xạ trường ngày (startField/endField) trong property; from/to lọc theo ngày bắt đầu.

    Args:
        table_id (UUID):
        view_id (UUID):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeProblemDetails | list[OfficeCalendarEventDto]]
     """


    kwargs = _get_kwargs(
        table_id=table_id,
view_id=view_id,
from_=from_,
to=to,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    table_id: UUID,
    view_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,

) -> OfficeProblemDetails | list[OfficeCalendarEventDto] | None:
    """ Record trong khoảng ngày của view kiểu Calendar

     Ánh xạ trường ngày (startField/endField) trong property; from/to lọc theo ngày bắt đầu.

    Args:
        table_id (UUID):
        view_id (UUID):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeProblemDetails | list[OfficeCalendarEventDto]
     """


    return (await asyncio_detailed(
        table_id=table_id,
view_id=view_id,
client=client,
from_=from_,
to=to,

    )).parsed
