from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gis_facility_list_item_dto_paged_result import GisFacilityListItemDtoPagedResult
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    facility_type: str | Unset = UNSET,
    status: str | Unset = UNSET,
    source_parcel_id: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["facilityType"] = facility_type

    params["status"] = status

    json_source_parcel_id: str | Unset = UNSET
    if not isinstance(source_parcel_id, Unset):
        json_source_parcel_id = str(source_parcel_id)
    params["sourceParcelId"] = json_source_parcel_id

    json_branch_id: str | Unset = UNSET
    if not isinstance(branch_id, Unset):
        json_branch_id = str(branch_id)
    params["branchId"] = json_branch_id

    params["page"] = page

    params["pageSize"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/gis/facilities",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GisFacilityListItemDtoPagedResult | None:
    if response.status_code == 200:
        response_200 = GisFacilityListItemDtoPagedResult.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GisFacilityListItemDtoPagedResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    facility_type: str | Unset = UNSET,
    status: str | Unset = UNSET,
    source_parcel_id: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[GisFacilityListItemDtoPagedResult]:
    """ Danh sách chuồng trại

     Lọc theo facilityType (barn, pasture, feedlot, dairy, poultry_house, piggery, processing_plant,
    other), status (active, inactive, maintenance) và branchId. Phân trang.

    Args:
        facility_type (str | Unset):
        status (str | Unset):
        source_parcel_id (UUID | Unset):
        branch_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisFacilityListItemDtoPagedResult]
     """


    kwargs = _get_kwargs(
        facility_type=facility_type,
status=status,
source_parcel_id=source_parcel_id,
branch_id=branch_id,
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
    facility_type: str | Unset = UNSET,
    status: str | Unset = UNSET,
    source_parcel_id: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> GisFacilityListItemDtoPagedResult | None:
    """ Danh sách chuồng trại

     Lọc theo facilityType (barn, pasture, feedlot, dairy, poultry_house, piggery, processing_plant,
    other), status (active, inactive, maintenance) và branchId. Phân trang.

    Args:
        facility_type (str | Unset):
        status (str | Unset):
        source_parcel_id (UUID | Unset):
        branch_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisFacilityListItemDtoPagedResult
     """


    return sync_detailed(
        client=client,
facility_type=facility_type,
status=status,
source_parcel_id=source_parcel_id,
branch_id=branch_id,
page=page,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    facility_type: str | Unset = UNSET,
    status: str | Unset = UNSET,
    source_parcel_id: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> Response[GisFacilityListItemDtoPagedResult]:
    """ Danh sách chuồng trại

     Lọc theo facilityType (barn, pasture, feedlot, dairy, poultry_house, piggery, processing_plant,
    other), status (active, inactive, maintenance) và branchId. Phân trang.

    Args:
        facility_type (str | Unset):
        status (str | Unset):
        source_parcel_id (UUID | Unset):
        branch_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GisFacilityListItemDtoPagedResult]
     """


    kwargs = _get_kwargs(
        facility_type=facility_type,
status=status,
source_parcel_id=source_parcel_id,
branch_id=branch_id,
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
    facility_type: str | Unset = UNSET,
    status: str | Unset = UNSET,
    source_parcel_id: UUID | Unset = UNSET,
    branch_id: UUID | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,

) -> GisFacilityListItemDtoPagedResult | None:
    """ Danh sách chuồng trại

     Lọc theo facilityType (barn, pasture, feedlot, dairy, poultry_house, piggery, processing_plant,
    other), status (active, inactive, maintenance) và branchId. Phân trang.

    Args:
        facility_type (str | Unset):
        status (str | Unset):
        source_parcel_id (UUID | Unset):
        branch_id (UUID | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GisFacilityListItemDtoPagedResult
     """


    return (await asyncio_detailed(
        client=client,
facility_type=facility_type,
status=status,
source_parcel_id=source_parcel_id,
branch_id=branch_id,
page=page,
page_size=page_size,

    )).parsed
