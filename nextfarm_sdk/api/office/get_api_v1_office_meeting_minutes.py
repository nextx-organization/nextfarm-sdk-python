from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_meeting_minute_dto import OfficeMeetingMinuteDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    event_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_event_id: str | Unset = UNSET
    if not isinstance(event_id, Unset):
        json_event_id = str(event_id)
    params["eventId"] = json_event_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/meeting-minutes",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeMeetingMinuteDto | None:
    if response.status_code == 200:
        response_200 = OfficeMeetingMinuteDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeMeetingMinuteDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    event_id: UUID | Unset = UNSET,

) -> Response[OfficeMeetingMinuteDto]:
    """ Biên bản của một cuộc họp

    Args:
        event_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeMeetingMinuteDto]
     """


    kwargs = _get_kwargs(
        event_id=event_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    event_id: UUID | Unset = UNSET,

) -> OfficeMeetingMinuteDto | None:
    """ Biên bản của một cuộc họp

    Args:
        event_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeMeetingMinuteDto
     """


    return sync_detailed(
        client=client,
event_id=event_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    event_id: UUID | Unset = UNSET,

) -> Response[OfficeMeetingMinuteDto]:
    """ Biên bản của một cuộc họp

    Args:
        event_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeMeetingMinuteDto]
     """


    kwargs = _get_kwargs(
        event_id=event_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    event_id: UUID | Unset = UNSET,

) -> OfficeMeetingMinuteDto | None:
    """ Biên bản của một cuộc họp

    Args:
        event_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeMeetingMinuteDto
     """


    return (await asyncio_detailed(
        client=client,
event_id=event_id,

    )).parsed
