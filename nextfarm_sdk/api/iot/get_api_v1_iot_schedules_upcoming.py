from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.iot_upcoming_slot_dto_i_read_only_list_items_response import IotUpcomingSlotDtoIReadOnlyListItemsResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    from_: datetime.date | Unset = UNSET,
    days: int | Unset = 1,
    device_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    params["days"] = days

    json_device_id: str | Unset = UNSET
    if not isinstance(device_id, Unset):
        json_device_id = str(device_id)
    params["device_id"] = json_device_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/iot/schedules/upcoming",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IotUpcomingSlotDtoIReadOnlyListItemsResponse | None:
    if response.status_code == 200:
        response_200 = IotUpcomingSlotDtoIReadOnlyListItemsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[IotUpcomingSlotDtoIReadOnlyListItemsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    days: int | Unset = 1,
    device_id: UUID | Unset = UNSET,

) -> Response[IotUpcomingSlotDtoIReadOnlyListItemsResponse]:
    """ Các cữ tưới sắp chạy của cả trại (gộp theo cữ)

     from (yyyy-MM-dd, mặc định hôm nay giờ VN), days 1–7, device_id tuỳ chọn.

    Args:
        from_ (datetime.date | Unset):
        days (int | Unset):  Default: 1.
        device_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IotUpcomingSlotDtoIReadOnlyListItemsResponse]
     """


    kwargs = _get_kwargs(
        from_=from_,
days=days,
device_id=device_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    days: int | Unset = 1,
    device_id: UUID | Unset = UNSET,

) -> IotUpcomingSlotDtoIReadOnlyListItemsResponse | None:
    """ Các cữ tưới sắp chạy của cả trại (gộp theo cữ)

     from (yyyy-MM-dd, mặc định hôm nay giờ VN), days 1–7, device_id tuỳ chọn.

    Args:
        from_ (datetime.date | Unset):
        days (int | Unset):  Default: 1.
        device_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IotUpcomingSlotDtoIReadOnlyListItemsResponse
     """


    return sync_detailed(
        client=client,
from_=from_,
days=days,
device_id=device_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    days: int | Unset = 1,
    device_id: UUID | Unset = UNSET,

) -> Response[IotUpcomingSlotDtoIReadOnlyListItemsResponse]:
    """ Các cữ tưới sắp chạy của cả trại (gộp theo cữ)

     from (yyyy-MM-dd, mặc định hôm nay giờ VN), days 1–7, device_id tuỳ chọn.

    Args:
        from_ (datetime.date | Unset):
        days (int | Unset):  Default: 1.
        device_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IotUpcomingSlotDtoIReadOnlyListItemsResponse]
     """


    kwargs = _get_kwargs(
        from_=from_,
days=days,
device_id=device_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date | Unset = UNSET,
    days: int | Unset = 1,
    device_id: UUID | Unset = UNSET,

) -> IotUpcomingSlotDtoIReadOnlyListItemsResponse | None:
    """ Các cữ tưới sắp chạy của cả trại (gộp theo cữ)

     from (yyyy-MM-dd, mặc định hôm nay giờ VN), days 1–7, device_id tuỳ chọn.

    Args:
        from_ (datetime.date | Unset):
        days (int | Unset):  Default: 1.
        device_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IotUpcomingSlotDtoIReadOnlyListItemsResponse
     """


    return (await asyncio_detailed(
        client=client,
from_=from_,
days=days,
device_id=device_id,

    )).parsed
