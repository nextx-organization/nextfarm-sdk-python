from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.iot_emergency_stop_dto import IotEmergencyStopDto
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    active_only: bool | Unset = True,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["activeOnly"] = active_only


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/iot/emergency-stop",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[IotEmergencyStopDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = IotEmergencyStopDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[IotEmergencyStopDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    active_only: bool | Unset = True,

) -> Response[list[IotEmergencyStopDto]]:
    """ Khoá dừng khẩn đang hiệu lực (activeOnly=true, mặc định) hoặc 20 lần gần nhất

    Args:
        active_only (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[IotEmergencyStopDto]]
     """


    kwargs = _get_kwargs(
        active_only=active_only,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    active_only: bool | Unset = True,

) -> list[IotEmergencyStopDto] | None:
    """ Khoá dừng khẩn đang hiệu lực (activeOnly=true, mặc định) hoặc 20 lần gần nhất

    Args:
        active_only (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[IotEmergencyStopDto]
     """


    return sync_detailed(
        client=client,
active_only=active_only,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    active_only: bool | Unset = True,

) -> Response[list[IotEmergencyStopDto]]:
    """ Khoá dừng khẩn đang hiệu lực (activeOnly=true, mặc định) hoặc 20 lần gần nhất

    Args:
        active_only (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[IotEmergencyStopDto]]
     """


    kwargs = _get_kwargs(
        active_only=active_only,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    active_only: bool | Unset = True,

) -> list[IotEmergencyStopDto] | None:
    """ Khoá dừng khẩn đang hiệu lực (activeOnly=true, mặc định) hoặc 20 lần gần nhất

    Args:
        active_only (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[IotEmergencyStopDto]
     """


    return (await asyncio_detailed(
        client=client,
active_only=active_only,

    )).parsed
