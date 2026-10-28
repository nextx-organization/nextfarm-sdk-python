from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.harvest_harvest_record_list_item_dto_paged_result import HarvestHarvestRecordListItemDtoPagedResult
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    filter_rules: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["status"] = status

    params["page"] = page

    params["pageSize"] = page_size

    params["filter_rules"] = filter_rules


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/harvest/harvest-records",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HarvestHarvestRecordListItemDtoPagedResult | None:
    if response.status_code == 200:
        response_200 = HarvestHarvestRecordListItemDtoPagedResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HarvestHarvestRecordListItemDtoPagedResult]:
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
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    filter_rules: str | Unset = UNSET,

) -> Response[HarvestHarvestRecordListItemDtoPagedResult]:
    """ Danh sách bản ghi thu hoạch

     Lọc theo status. Phân trang.

    Args:
        status (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        filter_rules (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HarvestHarvestRecordListItemDtoPagedResult]
     """


    kwargs = _get_kwargs(
        status=status,
page=page,
page_size=page_size,
filter_rules=filter_rules,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    filter_rules: str | Unset = UNSET,

) -> HarvestHarvestRecordListItemDtoPagedResult | None:
    """ Danh sách bản ghi thu hoạch

     Lọc theo status. Phân trang.

    Args:
        status (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        filter_rules (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HarvestHarvestRecordListItemDtoPagedResult
     """


    return sync_detailed(
        client=client,
status=status,
page=page,
page_size=page_size,
filter_rules=filter_rules,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    filter_rules: str | Unset = UNSET,

) -> Response[HarvestHarvestRecordListItemDtoPagedResult]:
    """ Danh sách bản ghi thu hoạch

     Lọc theo status. Phân trang.

    Args:
        status (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        filter_rules (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HarvestHarvestRecordListItemDtoPagedResult]
     """


    kwargs = _get_kwargs(
        status=status,
page=page,
page_size=page_size,
filter_rules=filter_rules,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    filter_rules: str | Unset = UNSET,

) -> HarvestHarvestRecordListItemDtoPagedResult | None:
    """ Danh sách bản ghi thu hoạch

     Lọc theo status. Phân trang.

    Args:
        status (str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        filter_rules (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HarvestHarvestRecordListItemDtoPagedResult
     """


    return (await asyncio_detailed(
        client=client,
status=status,
page=page,
page_size=page_size,
filter_rules=filter_rules,

    )).parsed
