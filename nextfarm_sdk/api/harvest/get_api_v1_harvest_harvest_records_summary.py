from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.harvest_harvest_summary_row_dto_paged_result import HarvestHarvestSummaryRowDtoPagedResult
from ...models.harvest_problem_details import HarvestProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    group_by: str | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
    crop_type_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["group_by"] = group_by

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    json_zone_id: str | Unset = UNSET
    if not isinstance(zone_id, Unset):
        json_zone_id = str(zone_id)
    params["zoneId"] = json_zone_id

    json_crop_type_id: str | Unset = UNSET
    if not isinstance(crop_type_id, Unset):
        json_crop_type_id = str(crop_type_id)
    params["cropTypeId"] = json_crop_type_id

    params["page"] = page

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/harvest/harvest-records/summary",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HarvestHarvestSummaryRowDtoPagedResult | HarvestProblemDetails | None:
    if response.status_code == 200:
        response_200 = HarvestHarvestSummaryRowDtoPagedResult.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = HarvestProblemDetails.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HarvestHarvestSummaryRowDtoPagedResult | HarvestProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    group_by: str | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
    crop_type_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[HarvestHarvestSummaryRowDtoPagedResult | HarvestProblemDetails]:
    """ Tổng hợp sản lượng theo hộ / vùng / cây / thửa

     group_by = owner (theo hộ) | zone (theo vùng) | crop (theo cây) | parcel (theo thửa). Chỉ tính phiếu
    ĐÃ XÁC NHẬN (Confirmed · Verified · Collected); kg = cân thực tế nếu đã kiểm, ngược lại số khai.
    from/to lọc theo ngày thu hoạch (yyyy-MM-dd), zoneId/cropTypeId lọc thêm. Hộ và vùng lấy từ gis tại
    lúc đọc (gis không trả lời được ⇒ báo lỗi dịch vụ ngoài, KHÔNG trả số thiếu). Phân trang (tối đa 200
    dòng/trang), xếp theo tổng kg giảm dần.

    Args:
        group_by (str | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        zone_id (UUID | Unset):
        crop_type_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HarvestHarvestSummaryRowDtoPagedResult | HarvestProblemDetails]
     """


    kwargs = _get_kwargs(
        group_by=group_by,
from_=from_,
to=to,
zone_id=zone_id,
crop_type_id=crop_type_id,
page=page,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    group_by: str | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
    crop_type_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> HarvestHarvestSummaryRowDtoPagedResult | HarvestProblemDetails | None:
    """ Tổng hợp sản lượng theo hộ / vùng / cây / thửa

     group_by = owner (theo hộ) | zone (theo vùng) | crop (theo cây) | parcel (theo thửa). Chỉ tính phiếu
    ĐÃ XÁC NHẬN (Confirmed · Verified · Collected); kg = cân thực tế nếu đã kiểm, ngược lại số khai.
    from/to lọc theo ngày thu hoạch (yyyy-MM-dd), zoneId/cropTypeId lọc thêm. Hộ và vùng lấy từ gis tại
    lúc đọc (gis không trả lời được ⇒ báo lỗi dịch vụ ngoài, KHÔNG trả số thiếu). Phân trang (tối đa 200
    dòng/trang), xếp theo tổng kg giảm dần.

    Args:
        group_by (str | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        zone_id (UUID | Unset):
        crop_type_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HarvestHarvestSummaryRowDtoPagedResult | HarvestProblemDetails
     """


    return sync_detailed(
        client=client,
group_by=group_by,
from_=from_,
to=to,
zone_id=zone_id,
crop_type_id=crop_type_id,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    group_by: str | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
    crop_type_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[HarvestHarvestSummaryRowDtoPagedResult | HarvestProblemDetails]:
    """ Tổng hợp sản lượng theo hộ / vùng / cây / thửa

     group_by = owner (theo hộ) | zone (theo vùng) | crop (theo cây) | parcel (theo thửa). Chỉ tính phiếu
    ĐÃ XÁC NHẬN (Confirmed · Verified · Collected); kg = cân thực tế nếu đã kiểm, ngược lại số khai.
    from/to lọc theo ngày thu hoạch (yyyy-MM-dd), zoneId/cropTypeId lọc thêm. Hộ và vùng lấy từ gis tại
    lúc đọc (gis không trả lời được ⇒ báo lỗi dịch vụ ngoài, KHÔNG trả số thiếu). Phân trang (tối đa 200
    dòng/trang), xếp theo tổng kg giảm dần.

    Args:
        group_by (str | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        zone_id (UUID | Unset):
        crop_type_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HarvestHarvestSummaryRowDtoPagedResult | HarvestProblemDetails]
     """


    kwargs = _get_kwargs(
        group_by=group_by,
from_=from_,
to=to,
zone_id=zone_id,
crop_type_id=crop_type_id,
page=page,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    group_by: str | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    zone_id: UUID | Unset = UNSET,
    crop_type_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> HarvestHarvestSummaryRowDtoPagedResult | HarvestProblemDetails | None:
    """ Tổng hợp sản lượng theo hộ / vùng / cây / thửa

     group_by = owner (theo hộ) | zone (theo vùng) | crop (theo cây) | parcel (theo thửa). Chỉ tính phiếu
    ĐÃ XÁC NHẬN (Confirmed · Verified · Collected); kg = cân thực tế nếu đã kiểm, ngược lại số khai.
    from/to lọc theo ngày thu hoạch (yyyy-MM-dd), zoneId/cropTypeId lọc thêm. Hộ và vùng lấy từ gis tại
    lúc đọc (gis không trả lời được ⇒ báo lỗi dịch vụ ngoài, KHÔNG trả số thiếu). Phân trang (tối đa 200
    dòng/trang), xếp theo tổng kg giảm dần.

    Args:
        group_by (str | Unset):
        from_ (datetime.date | Unset):
        to (datetime.date | Unset):
        zone_id (UUID | Unset):
        crop_type_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HarvestHarvestSummaryRowDtoPagedResult | HarvestProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
group_by=group_by,
from_=from_,
to=to,
zone_id=zone_id,
crop_type_id=crop_type_id,
page=page,
page_size=page_size,

    )).parsed
