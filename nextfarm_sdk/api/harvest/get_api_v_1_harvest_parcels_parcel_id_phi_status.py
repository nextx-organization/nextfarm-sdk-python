from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.harvest_phi_status_dto import HarvestPhiStatusDto
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    parcel_id: UUID,
    *,
    on: datetime.date | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_on: str | Unset = UNSET
    if not isinstance(on, Unset):
        json_on = on.isoformat()
    params["on"] = json_on


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/harvest/parcels/{parcel_id}/phi-status".format(parcel_id=quote(str(parcel_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HarvestPhiStatusDto | None:
    if response.status_code == 200:
        response_200 = HarvestPhiStatusDto.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HarvestPhiStatusDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    parcel_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    on: datetime.date | Unset = UNSET,

) -> Response[HarvestPhiStatusDto]:
    """ Thửa có đang trong thời gian cách ly không

     Tính từ các lần phun thuốc BVTV (và thuốc thú y ở sổ đàn/ao) có ghi số ngày cách ly. on = ngày định
    thu (yyyy-MM-dd, mặc định hôm nay giờ VN). active=true ⇒ khai thu hoạch ngày đó sẽ bị chặn trừ khi
    ghi lý do; safe_from = ngày sớm nhất được thu.

    Args:
        parcel_id (UUID):
        on (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HarvestPhiStatusDto]
     """


    kwargs = _get_kwargs(
        parcel_id=parcel_id,
on=on,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    parcel_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    on: datetime.date | Unset = UNSET,

) -> HarvestPhiStatusDto | None:
    """ Thửa có đang trong thời gian cách ly không

     Tính từ các lần phun thuốc BVTV (và thuốc thú y ở sổ đàn/ao) có ghi số ngày cách ly. on = ngày định
    thu (yyyy-MM-dd, mặc định hôm nay giờ VN). active=true ⇒ khai thu hoạch ngày đó sẽ bị chặn trừ khi
    ghi lý do; safe_from = ngày sớm nhất được thu.

    Args:
        parcel_id (UUID):
        on (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HarvestPhiStatusDto
     """


    return sync_detailed(
        parcel_id=parcel_id,
client=client,
on=on,

    ).parsed

async def asyncio_detailed(
    parcel_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    on: datetime.date | Unset = UNSET,

) -> Response[HarvestPhiStatusDto]:
    """ Thửa có đang trong thời gian cách ly không

     Tính từ các lần phun thuốc BVTV (và thuốc thú y ở sổ đàn/ao) có ghi số ngày cách ly. on = ngày định
    thu (yyyy-MM-dd, mặc định hôm nay giờ VN). active=true ⇒ khai thu hoạch ngày đó sẽ bị chặn trừ khi
    ghi lý do; safe_from = ngày sớm nhất được thu.

    Args:
        parcel_id (UUID):
        on (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HarvestPhiStatusDto]
     """


    kwargs = _get_kwargs(
        parcel_id=parcel_id,
on=on,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    parcel_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    on: datetime.date | Unset = UNSET,

) -> HarvestPhiStatusDto | None:
    """ Thửa có đang trong thời gian cách ly không

     Tính từ các lần phun thuốc BVTV (và thuốc thú y ở sổ đàn/ao) có ghi số ngày cách ly. on = ngày định
    thu (yyyy-MM-dd, mặc định hôm nay giờ VN). active=true ⇒ khai thu hoạch ngày đó sẽ bị chặn trừ khi
    ghi lý do; safe_from = ngày sớm nhất được thu.

    Args:
        parcel_id (UUID):
        on (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HarvestPhiStatusDto
     """


    return (await asyncio_detailed(
        parcel_id=parcel_id,
client=client,
on=on,

    )).parsed
