from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_farm_device_control_dto import OfficeFarmDeviceControlDto
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    status: str | Unset = UNSET,
    scope: str | Unset = 'mine',
    take: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["status"] = status

    params["scope"] = scope

    params["take"] = take


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/farm/device-controls",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[OfficeFarmDeviceControlDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = OfficeFarmDeviceControlDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[OfficeFarmDeviceControlDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    scope: str | Unset = 'mine',
    take: int | Unset = 50,

) -> Response[list[OfficeFarmDeviceControlDto]]:
    """ Danh sách phiếu lệnh

     status: pending · dispatched · rejected · expired. scope: mine (phiếu tôi được duyệt) · all.

    Args:
        status (str | Unset):
        scope (str | Unset):  Default: 'mine'.
        take (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeFarmDeviceControlDto]]
     """


    kwargs = _get_kwargs(
        status=status,
scope=scope,
take=take,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    scope: str | Unset = 'mine',
    take: int | Unset = 50,

) -> list[OfficeFarmDeviceControlDto] | None:
    """ Danh sách phiếu lệnh

     status: pending · dispatched · rejected · expired. scope: mine (phiếu tôi được duyệt) · all.

    Args:
        status (str | Unset):
        scope (str | Unset):  Default: 'mine'.
        take (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeFarmDeviceControlDto]
     """


    return sync_detailed(
        client=client,
status=status,
scope=scope,
take=take,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    scope: str | Unset = 'mine',
    take: int | Unset = 50,

) -> Response[list[OfficeFarmDeviceControlDto]]:
    """ Danh sách phiếu lệnh

     status: pending · dispatched · rejected · expired. scope: mine (phiếu tôi được duyệt) · all.

    Args:
        status (str | Unset):
        scope (str | Unset):  Default: 'mine'.
        take (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeFarmDeviceControlDto]]
     """


    kwargs = _get_kwargs(
        status=status,
scope=scope,
take=take,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    scope: str | Unset = 'mine',
    take: int | Unset = 50,

) -> list[OfficeFarmDeviceControlDto] | None:
    """ Danh sách phiếu lệnh

     status: pending · dispatched · rejected · expired. scope: mine (phiếu tôi được duyệt) · all.

    Args:
        status (str | Unset):
        scope (str | Unset):  Default: 'mine'.
        take (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeFarmDeviceControlDto]
     """


    return (await asyncio_detailed(
        client=client,
status=status,
scope=scope,
take=take,

    )).parsed
