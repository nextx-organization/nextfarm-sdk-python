from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gis_map_points_result import GisMapPointsResult
from ...models.gis_problem_details import GisProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    bbox: str | Unset = UNSET,
    zoom: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    kind: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["bbox"] = bbox

    params["zoom"] = zoom

    params["limit"] = limit

    params["kind"] = kind

    json_zone_id: str | Unset = UNSET
    if not isinstance(zone_id, Unset):
        json_zone_id = str(zone_id)
    params["zoneId"] = json_zone_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/gis/map/points",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GisMapPointsResult | GisProblemDetails | None:
    if response.status_code == 200:
        response_200 = GisMapPointsResult.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GisProblemDetails.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = GisProblemDetails.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GisMapPointsResult | GisProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    bbox: str | Unset = UNSET,
    zoom: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    kind: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,

) -> Response[GisMapPointsResult | GisProblemDetails]:
    """ Điểm nhẹ theo bbox: nhà hộ dân + tâm thửa

     bbox=minLon,minLat,maxLon,maxLat (bắt buộc, tối đa 10°×10°). zoom 0..22 (tuỳ chọn): dưới 13 mà nhiều
    hơn limit thì trả mode=clusters (ô gom). limit mặc định 2000, trần 5000; vượt thì cắt và
    truncated=true (KHÔNG báo lỗi). kind=all|farmer|parcel. Điểm hộ dân chỉ có khi người gọi có thêm
    gis.farmers.view và không bị giới hạn theo thửa sở hữu.

    Args:
        bbox (str | Unset):
        zoom (int | Unset):
        limit (int | Unset):
        kind (str | Unset):
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisMapPointsResult | GisProblemDetails]
     """


    kwargs = _get_kwargs(
        bbox=bbox,
zoom=zoom,
limit=limit,
kind=kind,
zone_id=zone_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    bbox: str | Unset = UNSET,
    zoom: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    kind: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,

) -> GisMapPointsResult | GisProblemDetails | None:
    """ Điểm nhẹ theo bbox: nhà hộ dân + tâm thửa

     bbox=minLon,minLat,maxLon,maxLat (bắt buộc, tối đa 10°×10°). zoom 0..22 (tuỳ chọn): dưới 13 mà nhiều
    hơn limit thì trả mode=clusters (ô gom). limit mặc định 2000, trần 5000; vượt thì cắt và
    truncated=true (KHÔNG báo lỗi). kind=all|farmer|parcel. Điểm hộ dân chỉ có khi người gọi có thêm
    gis.farmers.view và không bị giới hạn theo thửa sở hữu.

    Args:
        bbox (str | Unset):
        zoom (int | Unset):
        limit (int | Unset):
        kind (str | Unset):
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisMapPointsResult | GisProblemDetails
     """


    return sync_detailed(
        client=client,
bbox=bbox,
zoom=zoom,
limit=limit,
kind=kind,
zone_id=zone_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    bbox: str | Unset = UNSET,
    zoom: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    kind: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,

) -> Response[GisMapPointsResult | GisProblemDetails]:
    """ Điểm nhẹ theo bbox: nhà hộ dân + tâm thửa

     bbox=minLon,minLat,maxLon,maxLat (bắt buộc, tối đa 10°×10°). zoom 0..22 (tuỳ chọn): dưới 13 mà nhiều
    hơn limit thì trả mode=clusters (ô gom). limit mặc định 2000, trần 5000; vượt thì cắt và
    truncated=true (KHÔNG báo lỗi). kind=all|farmer|parcel. Điểm hộ dân chỉ có khi người gọi có thêm
    gis.farmers.view và không bị giới hạn theo thửa sở hữu.

    Args:
        bbox (str | Unset):
        zoom (int | Unset):
        limit (int | Unset):
        kind (str | Unset):
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisMapPointsResult | GisProblemDetails]
     """


    kwargs = _get_kwargs(
        bbox=bbox,
zoom=zoom,
limit=limit,
kind=kind,
zone_id=zone_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    bbox: str | Unset = UNSET,
    zoom: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    kind: str | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,

) -> GisMapPointsResult | GisProblemDetails | None:
    """ Điểm nhẹ theo bbox: nhà hộ dân + tâm thửa

     bbox=minLon,minLat,maxLon,maxLat (bắt buộc, tối đa 10°×10°). zoom 0..22 (tuỳ chọn): dưới 13 mà nhiều
    hơn limit thì trả mode=clusters (ô gom). limit mặc định 2000, trần 5000; vượt thì cắt và
    truncated=true (KHÔNG báo lỗi). kind=all|farmer|parcel. Điểm hộ dân chỉ có khi người gọi có thêm
    gis.farmers.view và không bị giới hạn theo thửa sở hữu.

    Args:
        bbox (str | Unset):
        zoom (int | Unset):
        limit (int | Unset):
        kind (str | Unset):
        zone_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisMapPointsResult | GisProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
bbox=bbox,
zoom=zoom,
limit=limit,
kind=kind,
zone_id=zone_id,

    )).parsed
