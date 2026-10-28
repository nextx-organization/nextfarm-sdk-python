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






T = TypeVar("T", bound="OfficeRoomBusySlotDto")



@_attrs_define
class OfficeRoomBusySlotDto:
    

    booked_by: UUID | Unset = UNSET
    end_at: datetime.datetime | Unset = UNSET
    event_id: UUID | Unset = UNSET
    event_title: None | str | Unset = UNSET
    start_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        booked_by: str | Unset = UNSET
        if not isinstance(self.booked_by, Unset):
            booked_by = str(self.booked_by)

        end_at: str | Unset = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        event_id: str | Unset = UNSET
        if not isinstance(self.event_id, Unset):
            event_id = str(self.event_id)

        event_title: None | str | Unset
        if isinstance(self.event_title, Unset):
            event_title = UNSET
        else:
            event_title = self.event_title

        start_at: str | Unset = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if booked_by is not UNSET:
            field_dict["bookedBy"] = booked_by
        if end_at is not UNSET:
            field_dict["endAt"] = end_at
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if event_title is not UNSET:
            field_dict["eventTitle"] = event_title
        if start_at is not UNSET:
            field_dict["startAt"] = start_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _booked_by = d.pop("bookedBy", UNSET)
        booked_by: UUID | Unset
        if isinstance(_booked_by,  Unset):
            booked_by = UNSET
        else:
            booked_by = UUID(_booked_by)




        _end_at = d.pop("endAt", UNSET)
        end_at: datetime.datetime | Unset
        if isinstance(_end_at,  Unset):
            end_at = UNSET
        else:
            end_at = datetime.datetime.fromisoformat(_end_at)




        _event_id = d.pop("eventId", UNSET)
        event_id: UUID | Unset
        if isinstance(_event_id,  Unset):
            event_id = UNSET
        else:
            event_id = UUID(_event_id)




        def _parse_event_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_title = _parse_event_title(d.pop("eventTitle", UNSET))


        _start_at = d.pop("startAt", UNSET)
        start_at: datetime.datetime | Unset
        if isinstance(_start_at,  Unset):
            start_at = UNSET
        else:
            start_at = datetime.datetime.fromisoformat(_start_at)




        office_room_busy_slot_dto = cls(
            booked_by=booked_by,
            end_at=end_at,
            event_id=event_id,
            event_title=event_title,
            start_at=start_at,
        )

        return office_room_busy_slot_dto

