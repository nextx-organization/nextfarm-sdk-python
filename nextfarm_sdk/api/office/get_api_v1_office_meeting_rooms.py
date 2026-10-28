from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.office_meeting_room_dto import OfficeMeetingRoomDto
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    active_only: bool | Unset = True,
    min_capacity: int | Unset = UNSET,
    equipment: list[str] | Unset = UNSET,
    building: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["activeOnly"] = active_only

    params["minCapacity"] = min_capacity

    json_equipment: list[str] | Unset = UNSET
    if not isinstance(equipment, Unset):
        json_equipment = equipment


    params["equipment"] = json_equipment

    params["building"] = building


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/office/meeting-rooms",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[OfficeMeetingRoomDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = OfficeMeetingRoomDto.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[OfficeMeetingRoomDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    active_only: bool | Unset = True,
    min_capacity: int | Unset = UNSET,
    equipment: list[str] | Unset = UNSET,
    building: str | Unset = UNSET,

) -> Response[list[OfficeMeetingRoomDto]]:
    """ Danh sách phòng họp

     minCapacity/equipment/building lọc ngay trong màn chọn phòng — equipment yêu cầu phòng có ĐỦ mọi mã
    đã hỏi.

    Args:
        active_only (bool | Unset):  Default: True.
        min_capacity (int | Unset):
        equipment (list[str] | Unset):
        building (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeMeetingRoomDto]]
     """


    kwargs = _get_kwargs(
        active_only=active_only,
min_capacity=min_capacity,
equipment=equipment,
building=building,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    active_only: bool | Unset = True,
    min_capacity: int | Unset = UNSET,
    equipment: list[str] | Unset = UNSET,
    building: str | Unset = UNSET,

) -> list[OfficeMeetingRoomDto] | None:
    """ Danh sách phòng họp

     minCapacity/equipment/building lọc ngay trong màn chọn phòng — equipment yêu cầu phòng có ĐỦ mọi mã
    đã hỏi.

    Args:
        active_only (bool | Unset):  Default: True.
        min_capacity (int | Unset):
        equipment (list[str] | Unset):
        building (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeMeetingRoomDto]
     """


    return sync_detailed(
        client=client,
active_only=active_only,
min_capacity=min_capacity,
equipment=equipment,
building=building,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    active_only: bool | Unset = True,
    min_capacity: int | Unset = UNSET,
    equipment: list[str] | Unset = UNSET,
    building: str | Unset = UNSET,

) -> Response[list[OfficeMeetingRoomDto]]:
    """ Danh sách phòng họp

     minCapacity/equipment/building lọc ngay trong màn chọn phòng — equipment yêu cầu phòng có ĐỦ mọi mã
    đã hỏi.

    Args:
        active_only (bool | Unset):  Default: True.
        min_capacity (int | Unset):
        equipment (list[str] | Unset):
        building (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[OfficeMeetingRoomDto]]
     """


    kwargs = _get_kwargs(
        active_only=active_only,
min_capacity=min_capacity,
equipment=equipment,
building=building,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    active_only: bool | Unset = True,
    min_capacity: int | Unset = UNSET,
    equipment: list[str] | Unset = UNSET,
    building: str | Unset = UNSET,

) -> list[OfficeMeetingRoomDto] | None:
    """ Danh sách phòng họp

     minCapacity/equipment/building lọc ngay trong màn chọn phòng — equipment yêu cầu phòng có ĐỦ mọi mã
    đã hỏi.

    Args:
        active_only (bool | Unset):  Default: True.
        min_capacity (int | Unset):
        equipment (list[str] | Unset):
        building (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[OfficeMeetingRoomDto]
     """


    return (await asyncio_detailed(
        client=client,
active_only=active_only,
min_capacity=min_capacity,
equipment=equipment,
building=building,

    )).parsed
