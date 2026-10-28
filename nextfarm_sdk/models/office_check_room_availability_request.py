from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="OfficeCheckRoomAvailabilityRequest")



@_attrs_define
class OfficeCheckRoomAvailabilityRequest:
    

    end_at: datetime.datetime | Unset = UNSET
    exclude_event_id: None | Unset | UUID = UNSET
    room_ids: list[UUID] | None | Unset = UNSET
    start_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        end_at: str | Unset = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        exclude_event_id: None | str | Unset
        if isinstance(self.exclude_event_id, Unset):
            exclude_event_id = UNSET
        elif isinstance(self.exclude_event_id, UUID):
            exclude_event_id = str(self.exclude_event_id)
        else:
            exclude_event_id = self.exclude_event_id

        room_ids: list[str] | None | Unset
        if isinstance(self.room_ids, Unset):
            room_ids = UNSET
        elif isinstance(self.room_ids, list):
            room_ids = []
            for room_ids_type_0_item_data in self.room_ids:
                room_ids_type_0_item = str(room_ids_type_0_item_data)
                room_ids.append(room_ids_type_0_item)


        else:
            room_ids = self.room_ids

        start_at: str | Unset = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if end_at is not UNSET:
            field_dict["endAt"] = end_at
        if exclude_event_id is not UNSET:
            field_dict["excludeEventId"] = exclude_event_id
        if room_ids is not UNSET:
            field_dict["roomIds"] = room_ids
        if start_at is not UNSET:
            field_dict["startAt"] = start_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _end_at = d.pop("endAt", UNSET)
        end_at: datetime.datetime | Unset
        if isinstance(_end_at,  Unset):
            end_at = UNSET
        else:
            end_at = datetime.datetime.fromisoformat(_end_at)




        def _parse_exclude_event_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                exclude_event_id_type_0 = UUID(data)



                return exclude_event_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        exclude_event_id = _parse_exclude_event_id(d.pop("excludeEventId", UNSET))


        def _parse_room_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                room_ids_type_0 = []
                _room_ids_type_0 = data
                for room_ids_type_0_item_data in (_room_ids_type_0):
                    room_ids_type_0_item = UUID(room_ids_type_0_item_data)



                    room_ids_type_0.append(room_ids_type_0_item)

                return room_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        room_ids = _parse_room_ids(d.pop("roomIds", UNSET))


        _start_at = d.pop("startAt", UNSET)
        start_at: datetime.datetime | Unset
        if isinstance(_start_at,  Unset):
            start_at = UNSET
        else:
            start_at = datetime.datetime.fromisoformat(_start_at)




        office_check_room_availability_request = cls(
            end_at=end_at,
            exclude_event_id=exclude_event_id,
            room_ids=room_ids,
            start_at=start_at,
        )

        return office_check_room_availability_request

