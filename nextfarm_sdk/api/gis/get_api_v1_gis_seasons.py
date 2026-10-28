from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gis_season_dto import GisSeasonDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    parcel_id: UUID | Unset = UNSET,
    year: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_parcel_id: str | Unset = UNSET
    if not isinstance(parcel_id, Unset):
        json_parcel_id = str(parcel_id)
    params["parcelId"] = json_parcel_id

    params["year"] = year


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/gis/seasons",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[GisSeasonDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = GisSeasonDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[GisSeasonDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    parcel_id: UUID | Unset = UNSET,
    year: int | Unset = UNSET,

) -> Response[list[GisSeasonDto]]:
    """ Danh sách mùa vụ

     Cần ít nhất một trong hai: `parcelId` (lịch sử canh tác của một thửa) hoặc `year` (thanh 12 tháng).
    Với `year`, vụ được lấy khi nó **CHẠM** vào năm đó — vụ trồng 12/2025 thu 03/2026 hiện ở cả hai năm,
    nếu không thì tháng 1–2 của 2026 trông như không có vụ nào trong khi ngoài ruộng đang có cây.

    Args:
        parcel_id (UUID | Unset):
        year (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[GisSeasonDto]]
     """


    kwargs = _get_kwargs(
        parcel_id=parcel_id,
year=year,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    parcel_id: UUID | Unset = UNSET,
    year: int | Unset = UNSET,

) -> list[GisSeasonDto] | None:
    """ Danh sách mùa vụ

     Cần ít nhất một trong hai: `parcelId` (lịch sử canh tác của một thửa) hoặc `year` (thanh 12 tháng).
    Với `year`, vụ được lấy khi nó **CHẠM** vào năm đó — vụ trồng 12/2025 thu 03/2026 hiện ở cả hai năm,
    nếu không thì tháng 1–2 của 2026 trông như không có vụ nào trong khi ngoài ruộng đang có cây.

    Args:
        parcel_id (UUID | Unset):
        year (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[GisSeasonDto]
     """


    return sync_detailed(
        client=client,
parcel_id=parcel_id,
year=year,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parcel_id: UUID | Unset = UNSET,
    year: int | Unset = UNSET,

) -> Response[list[GisSeasonDto]]:
    """ Danh sách mùa vụ

     Cần ít nhất một trong hai: `parcelId` (lịch sử canh tác của một thửa) hoặc `year` (thanh 12 tháng).
    Với `year`, vụ được lấy khi nó **CHẠM** vào năm đó — vụ trồng 12/2025 thu 03/2026 hiện ở cả hai năm,
    nếu không thì tháng 1–2 của 2026 trông như không có vụ nào trong khi ngoài ruộng đang có cây.

    Args:
        parcel_id (UUID | Unset):
        year (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[GisSeasonDto]]
     """


    kwargs = _get_kwargs(
        parcel_id=parcel_id,
year=year,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parcel_id: UUID | Unset = UNSET,
    year: int | Unset = UNSET,

) -> list[GisSeasonDto] | None:
    """ Danh sách mùa vụ

     Cần ít nhất một trong hai: `parcelId` (lịch sử canh tác của một thửa) hoặc `year` (thanh 12 tháng).
    Với `year`, vụ được lấy khi nó **CHẠM** vào năm đó — vụ trồng 12/2025 thu 03/2026 hiện ở cả hai năm,
    nếu không thì tháng 1–2 của 2026 trông như không có vụ nào trong khi ngoài ruộng đang có cây.

    Args:
        parcel_id (UUID | Unset):
        year (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[GisSeasonDto]
     """


    return (await asyncio_detailed(
        client=client,
parcel_id=parcel_id,
year=year,

    )).parsed
