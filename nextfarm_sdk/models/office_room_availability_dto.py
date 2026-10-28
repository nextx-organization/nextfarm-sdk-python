from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.office_room_busy_slot_dto import OfficeRoomBusySlotDto





T = TypeVar("T", bound="OfficeRoomAvailabilityDto")



@_attrs_define
class OfficeRoomAvailabilityDto:
    

    available: bool | Unset = UNSET
    conflicts: list[OfficeRoomBusySlotDto] | None | Unset = UNSET
    room_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_room_busy_slot_dto import OfficeRoomBusySlotDto # noqa: PLC0415
        available = self.available

        conflicts: list[dict[str, Any]] | None | Unset
        if isinstance(self.conflicts, Unset):
            conflicts = UNSET
        elif isinstance(self.conflicts, list):
            conflicts = []
            for conflicts_type_0_item_data in self.conflicts:
                conflicts_type_0_item = conflicts_type_0_item_data.to_dict()
                conflicts.append(conflicts_type_0_item)


        else:
            conflicts = self.conflicts

        room_id: str | Unset = UNSET
        if not isinstance(self.room_id, Unset):
            room_id = str(self.room_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if available is not UNSET:
            field_dict["available"] = available
        if conflicts is not UNSET:
            field_dict["conflicts"] = conflicts
        if room_id is not UNSET:
            field_dict["roomId"] = room_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_room_busy_slot_dto import OfficeRoomBusySlotDto # noqa: PLC0415
        d = dict(src_dict)
        available = d.pop("available", UNSET)

        def _parse_conflicts(data: object) -> list[OfficeRoomBusySlotDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conflicts_type_0 = []
                _conflicts_type_0 = data
                for conflicts_type_0_item_data in (_conflicts_type_0):
                    conflicts_type_0_item = OfficeRoomBusySlotDto.from_dict(conflicts_type_0_item_data)



                    conflicts_type_0.append(conflicts_type_0_item)

                return conflicts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeRoomBusySlotDto] | None | Unset, data)

        conflicts = _parse_conflicts(d.pop("conflicts", UNSET))


        _room_id = d.pop("roomId", UNSET)
        room_id: UUID | Unset
        if isinstance(_room_id,  Unset):
            room_id = UNSET
        else:
            room_id = UUID(_room_id)




        office_room_availability_dto = cls(
            available=available,
            conflicts=conflicts,
            room_id=room_id,
        )

        return office_room_availability_dto

