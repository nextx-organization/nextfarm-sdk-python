from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.iot_device_control_state_dto import IotDeviceControlStateDto
from ...models.iot_problem_details import IotProblemDetails
from typing import cast
from uuid import UUID



def _get_kwargs(
    device_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/iot/devices/{device_id}/control-state".format(device_id=quote(str(device_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IotDeviceControlStateDto | IotProblemDetails | None:
    if response.status_code == 200:
        response_200 = IotDeviceControlStateDto.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = IotProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[IotDeviceControlStateDto | IotProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    device_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[IotDeviceControlStateDto | IotProblemDetails]:
    """ Trạng thái điều khiển thực tế của 1 thiết bị

     Giải mã từ outputs bitmask + pump/winch/shade/flow (status mỗi 5s). FE poll ~5s.

    Args:
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IotDeviceControlStateDto | IotProblemDetails]
     """


    kwargs = _get_kwargs(
        device_id=device_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    device_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> IotDeviceControlStateDto | IotProblemDetails | None:
    """ Trạng thái điều khiển thực tế của 1 thiết bị

     Giải mã từ outputs bitmask + pump/winch/shade/flow (status mỗi 5s). FE poll ~5s.

    Args:
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IotDeviceControlStateDto | IotProblemDetails
     """


    return sync_detailed(
        device_id=device_id,
client=client,

    ).parsed

async def asyncio_detailed(
    device_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[IotDeviceControlStateDto | IotProblemDetails]:
    """ Trạng thái điều khiển thực tế của 1 thiết bị

     Giải mã từ outputs bitmask + pump/winch/shade/flow (status mỗi 5s). FE poll ~5s.

    Args:
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IotDeviceControlStateDto | IotProblemDetails]
     """


    kwargs = _get_kwargs(
        device_id=device_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    device_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> IotDeviceControlStateDto | IotProblemDetails | None:
    """ Trạng thái điều khiển thực tế của 1 thiết bị

     Giải mã từ outputs bitmask + pump/winch/shade/flow (status mỗi 5s). FE poll ~5s.

    Args:
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IotDeviceControlStateDto | IotProblemDetails
     """


    return (await asyncio_detailed(
        device_id=device_id,
client=client,

    )).parsed
