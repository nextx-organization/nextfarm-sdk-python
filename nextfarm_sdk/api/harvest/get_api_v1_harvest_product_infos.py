from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.harvest_product_info_admin_dto import HarvestProductInfoAdminDto
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/harvest/product-infos",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[HarvestProductInfoAdminDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = HarvestProductInfoAdminDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[HarvestProductInfoAdminDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[HarvestProductInfoAdminDto]]:
    """ Danh sách hồ sơ sản phẩm

     Gồm hồ sơ riêng của workspace và các hồ sơ dùng chung (workspace_id rỗng).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[HarvestProductInfoAdminDto]]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> list[HarvestProductInfoAdminDto] | None:
    """ Danh sách hồ sơ sản phẩm

     Gồm hồ sơ riêng của workspace và các hồ sơ dùng chung (workspace_id rỗng).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[HarvestProductInfoAdminDto]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[HarvestProductInfoAdminDto]]:
    """ Danh sách hồ sơ sản phẩm

     Gồm hồ sơ riêng của workspace và các hồ sơ dùng chung (workspace_id rỗng).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[HarvestProductInfoAdminDto]]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> list[HarvestProductInfoAdminDto] | None:
    """ Danh sách hồ sơ sản phẩm

     Gồm hồ sơ riêng của workspace và các hồ sơ dùng chung (workspace_id rỗng).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[HarvestProductInfoAdminDto]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
