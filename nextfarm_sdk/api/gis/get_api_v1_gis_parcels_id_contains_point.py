from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gis_parcel_contains_point_dto import GisParcelContainsPointDto
from ...models.gis_problem_details import GisProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    lat: float | Unset = UNSET,
    lng: float | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["lat"] = lat

    params["lng"] = lng


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/gis/parcels/{id}/contains-point".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GisParcelContainsPointDto | GisProblemDetails | None:
    if response.status_code == 200:
        response_200 = GisParcelContainsPointDto.from_dict(response.json())



        return response_200

    if response.status_code == 403:
        response_403 = GisProblemDetails.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GisProblemDetails.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = GisProblemDetails.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GisParcelContainsPointDto | GisProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    lat: float | Unset = UNSET,
    lng: float | Unset = UNSET,

) -> Response[GisParcelContainsPointDto | GisProblemDetails]:
    """ Điểm GPS có nằm trong ranh thửa không

     Trả 200 kèm `{ parcel_id, inside }`. NGOÀI RANH LÀ MỘT CÂU TRẢ LỜI HỢP LỆ (`inside=false`), KHÔNG
    phải lỗi — endpoint này nói sự thật hình học, còn cảnh báo hay chặn là việc của NGƯỜI GỌI. Điểm nằm
    ĐÚNG TRÊN CẠNH tính là TRONG (Covers, không phải Contains): nông dân đứng ở bờ ruộng không được báo
    sai. 422 chỉ khi toạ độ ngoài miền hợp lệ. Không có GPS thì đừng gọi. Đây là CHẶNG TRƯỚC MẮT — đích
    đến là kiểm CỤC BỘ trên máy qua gói offline `GET /gis/sync/parcels` (đã có sẵn), vì chính lúc mất
    sóng mới là lúc người ta ở giữa ruộng.

    Args:
        id (UUID):
        lat (float | Unset):
        lng (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisParcelContainsPointDto | GisProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,
lat=lat,
lng=lng,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    lat: float | Unset = UNSET,
    lng: float | Unset = UNSET,

) -> GisParcelContainsPointDto | GisProblemDetails | None:
    """ Điểm GPS có nằm trong ranh thửa không

     Trả 200 kèm `{ parcel_id, inside }`. NGOÀI RANH LÀ MỘT CÂU TRẢ LỜI HỢP LỆ (`inside=false`), KHÔNG
    phải lỗi — endpoint này nói sự thật hình học, còn cảnh báo hay chặn là việc của NGƯỜI GỌI. Điểm nằm
    ĐÚNG TRÊN CẠNH tính là TRONG (Covers, không phải Contains): nông dân đứng ở bờ ruộng không được báo
    sai. 422 chỉ khi toạ độ ngoài miền hợp lệ. Không có GPS thì đừng gọi. Đây là CHẶNG TRƯỚC MẮT — đích
    đến là kiểm CỤC BỘ trên máy qua gói offline `GET /gis/sync/parcels` (đã có sẵn), vì chính lúc mất
    sóng mới là lúc người ta ở giữa ruộng.

    Args:
        id (UUID):
        lat (float | Unset):
        lng (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisParcelContainsPointDto | GisProblemDetails
     """


    return sync_detailed(
        id=id,
client=client,
lat=lat,
lng=lng,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    lat: float | Unset = UNSET,
    lng: float | Unset = UNSET,

) -> Response[GisParcelContainsPointDto | GisProblemDetails]:
    """ Điểm GPS có nằm trong ranh thửa không

     Trả 200 kèm `{ parcel_id, inside }`. NGOÀI RANH LÀ MỘT CÂU TRẢ LỜI HỢP LỆ (`inside=false`), KHÔNG
    phải lỗi — endpoint này nói sự thật hình học, còn cảnh báo hay chặn là việc của NGƯỜI GỌI. Điểm nằm
    ĐÚNG TRÊN CẠNH tính là TRONG (Covers, không phải Contains): nông dân đứng ở bờ ruộng không được báo
    sai. 422 chỉ khi toạ độ ngoài miền hợp lệ. Không có GPS thì đừng gọi. Đây là CHẶNG TRƯỚC MẮT — đích
    đến là kiểm CỤC BỘ trên máy qua gói offline `GET /gis/sync/parcels` (đã có sẵn), vì chính lúc mất
    sóng mới là lúc người ta ở giữa ruộng.

    Args:
        id (UUID):
        lat (float | Unset):
        lng (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisParcelContainsPointDto | GisProblemDetails]
     """


    kwargs = _get_kwargs(
        id=id,
lat=lat,
lng=lng,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    lat: float | Unset = UNSET,
    lng: float | Unset = UNSET,

) -> GisParcelContainsPointDto | GisProblemDetails | None:
    """ Điểm GPS có nằm trong ranh thửa không

     Trả 200 kèm `{ parcel_id, inside }`. NGOÀI RANH LÀ MỘT CÂU TRẢ LỜI HỢP LỆ (`inside=false`), KHÔNG
    phải lỗi — endpoint này nói sự thật hình học, còn cảnh báo hay chặn là việc của NGƯỜI GỌI. Điểm nằm
    ĐÚNG TRÊN CẠNH tính là TRONG (Covers, không phải Contains): nông dân đứng ở bờ ruộng không được báo
    sai. 422 chỉ khi toạ độ ngoài miền hợp lệ. Không có GPS thì đừng gọi. Đây là CHẶNG TRƯỚC MẮT — đích
    đến là kiểm CỤC BỘ trên máy qua gói offline `GET /gis/sync/parcels` (đã có sẵn), vì chính lúc mất
    sóng mới là lúc người ta ở giữa ruộng.

    Args:
        id (UUID):
        lat (float | Unset):
        lng (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisParcelContainsPointDto | GisProblemDetails
     """


    return (await asyncio_detailed(
        id=id,
client=client,
lat=lat,
lng=lng,

    )).parsed
