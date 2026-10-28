from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_automation_run_stats_dto import OfficeAutomationRunStatsDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    automation_id: UUID | Unset = UNSET,
    days: int | Unset = 7,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_automation_id: str | Unset = UNSET
    if not isinstance(automation_id, Unset):
        json_automation_id = str(automation_id)
    params["automationId"] = json_automation_id

    params["days"] = days


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/automation-logs/stats",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> OfficeAutomationRunStatsDto | None:
    if response.status_code == 200:
        response_200 = OfficeAutomationRunStatsDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[OfficeAutomationRunStatsDto]:
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
    days: int | Unset = 7,

) -> Response[OfficeAutomationRunStatsDto]:
    """ Bốn ô số liệu trên đầu màn nhật ký

     Đếm theo từng MÃ kết quả trong `days` ngày gần nhất (1–90).

    Args:
        automation_id (UUID | Unset):
        days (int | Unset):  Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeAutomationRunStatsDto]
     """


    kwargs = _get_kwargs(
        automation_id=automation_id,
days=days,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    automation_id: UUID | Unset = UNSET,
    days: int | Unset = 7,

) -> OfficeAutomationRunStatsDto | None:
    """ Bốn ô số liệu trên đầu màn nhật ký

     Đếm theo từng MÃ kết quả trong `days` ngày gần nhất (1–90).

    Args:
        automation_id (UUID | Unset):
        days (int | Unset):  Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeAutomationRunStatsDto
     """


    return sync_detailed(
        client=client,
automation_id=automation_id,
days=days,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    automation_id: UUID | Unset = UNSET,
    days: int | Unset = 7,

) -> Response[OfficeAutomationRunStatsDto]:
    """ Bốn ô số liệu trên đầu màn nhật ký

     Đếm theo từng MÃ kết quả trong `days` ngày gần nhất (1–90).

    Args:
        automation_id (UUID | Unset):
        days (int | Unset):  Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OfficeAutomationRunStatsDto]
     """


    kwargs = _get_kwargs(
        automation_id=automation_id,
days=days,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    automation_id: UUID | Unset = UNSET,
    days: int | Unset = 7,

) -> OfficeAutomationRunStatsDto | None:
    """ Bốn ô số liệu trên đầu màn nhật ký

     Đếm theo từng MÃ kết quả trong `days` ngày gần nhất (1–90).

    Args:
        automation_id (UUID | Unset):
        days (int | Unset):  Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OfficeAutomationRunStatsDto
     """


    return (await asyncio_detailed(
        client=client,
automation_id=automation_id,
days=days,

    )).parsed
