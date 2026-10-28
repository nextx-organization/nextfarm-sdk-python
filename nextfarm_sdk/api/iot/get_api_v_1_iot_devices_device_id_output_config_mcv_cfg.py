from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.iot_mcv_cfg_state_dto import IotMcvCfgStateDto
from ...models.iot_problem_details import IotProblemDetails
from typing import cast
from uuid import UUID



def _get_kwargs(
    device_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/iot/devices/{device_id}/output-config/mcv-cfg".format(device_id=quote(str(device_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IotMcvCfgStateDto | IotProblemDetails | None:
    if response.status_code == 200:
        response_200 = IotMcvCfgStateDto.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = IotProblemDetails.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[IotMcvCfgStateDto | IotProblemDetails]:
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

) -> Response[IotMcvCfgStateDto | IotProblemDetails]:
    """ Trạng thái đồng bộ cài đặt van Denso: giá trị đã đặt (desired), bo đang giữ (reported, từ echo
    dev_cfg), ack và 1 trong 8 trạng thái

    Args:
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IotMcvCfgStateDto | IotProblemDetails]
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

) -> IotMcvCfgStateDto | IotProblemDetails | None:
    """ Trạng thái đồng bộ cài đặt van Denso: giá trị đã đặt (desired), bo đang giữ (reported, từ echo
    dev_cfg), ack và 1 trong 8 trạng thái

    Args:
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IotMcvCfgStateDto | IotProblemDetails
     """


    return sync_detailed(
        device_id=device_id,
client=client,

    ).parsed

async def asyncio_detailed(
    device_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[IotMcvCfgStateDto | IotProblemDetails]:
    """ Trạng thái đồng bộ cài đặt van Denso: giá trị đã đặt (desired), bo đang giữ (reported, từ echo
    dev_cfg), ack và 1 trong 8 trạng thái

    Args:
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IotMcvCfgStateDto | IotProblemDetails]
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

) -> IotMcvCfgStateDto | IotProblemDetails | None:
    """ Trạng thái đồng bộ cài đặt van Denso: giá trị đã đặt (desired), bo đang giữ (reported, từ echo
    dev_cfg), ack và 1 trong 8 trạng thái

    Args:
        device_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IotMcvCfgStateDto | IotProblemDetails
     """


    return (await asyncio_detailed(
        device_id=device_id,
client=client,

    )).parsed
