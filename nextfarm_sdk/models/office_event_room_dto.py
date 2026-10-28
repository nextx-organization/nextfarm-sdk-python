from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeEventRoomDto")



@_attrs_define
class OfficeEventRoomDto:
    

    booking_id: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    room_id: UUID | Unset = UNSET
    status: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        booking_id: str | Unset = UNSET
        if not isinstance(self.booking_id, Unset):
            booking_id = str(self.booking_id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        room_id: str | Unset = UNSET
        if not isinstance(self.room_id, Unset):
            room_id = str(self.room_id)

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if booking_id is not UNSET:
            field_dict["bookingId"] = booking_id
        if name is not UNSET:
            field_dict["name"] = name
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _booking_id = d.pop("bookingId", UNSET)
        booking_id: UUID | Unset
        if isinstance(_booking_id,  Unset):
            booking_id = UNSET
        else:
            booking_id = UUID(_booking_id)




        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        _room_id = d.pop("roomId", UNSET)
        room_id: UUID | Unset
        if isinstance(_room_id,  Unset):
            room_id = UNSET
        else:
            room_id = UUID(_room_id)




        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        office_event_room_dto = cls(
            booking_id=booking_id,
            name=name,
            room_id=room_id,
            status=status,
        )

        return office_event_room_dto

