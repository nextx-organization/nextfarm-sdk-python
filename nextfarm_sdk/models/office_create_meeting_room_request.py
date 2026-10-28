from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeCreateMeetingRoomRequest")



@_attrs_define
class OfficeCreateMeetingRoomRequest:
    

    auto_release_minutes: int | None | Unset = UNSET
    building: None | str | Unset = UNSET
    capacity: int | Unset = UNSET
    equipment: list[str] | None | Unset = UNSET
    floor: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    max_booking_minutes: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    requires_approval: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        auto_release_minutes: int | None | Unset
        if isinstance(self.auto_release_minutes, Unset):
            auto_release_minutes = UNSET
        else:
            auto_release_minutes = self.auto_release_minutes

        building: None | str | Unset
        if isinstance(self.building, Unset):
            building = UNSET
        else:
            building = self.building

        capacity = self.capacity

        equipment: list[str] | None | Unset
        if isinstance(self.equipment, Unset):
            equipment = UNSET
        elif isinstance(self.equipment, list):
            equipment = self.equipment


        else:
            equipment = self.equipment

        floor: None | str | Unset
        if isinstance(self.floor, Unset):
            floor = UNSET
        else:
            floor = self.floor

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        max_booking_minutes: int | None | Unset
        if isinstance(self.max_booking_minutes, Unset):
            max_booking_minutes = UNSET
        else:
            max_booking_minutes = self.max_booking_minutes

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        requires_approval = self.requires_approval


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if auto_release_minutes is not UNSET:
            field_dict["autoReleaseMinutes"] = auto_release_minutes
        if building is not UNSET:
            field_dict["building"] = building
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if floor is not UNSET:
            field_dict["floor"] = floor
        if location is not UNSET:
            field_dict["location"] = location
        if max_booking_minutes is not UNSET:
            field_dict["maxBookingMinutes"] = max_booking_minutes
        if name is not UNSET:
            field_dict["name"] = name
        if requires_approval is not UNSET:
            field_dict["requiresApproval"] = requires_approval

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_auto_release_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_release_minutes = _parse_auto_release_minutes(d.pop("autoReleaseMinutes", UNSET))


        def _parse_building(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building = _parse_building(d.pop("building", UNSET))


        capacity = d.pop("capacity", UNSET)

        def _parse_equipment(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                equipment_type_0 = cast(list[str], data)

                return equipment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        equipment = _parse_equipment(d.pop("equipment", UNSET))


        def _parse_floor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        floor = _parse_floor(d.pop("floor", UNSET))


        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))


        def _parse_max_booking_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_booking_minutes = _parse_max_booking_minutes(d.pop("maxBookingMinutes", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        requires_approval = d.pop("requiresApproval", UNSET)

        office_create_meeting_room_request = cls(
            auto_release_minutes=auto_release_minutes,
            building=building,
            capacity=capacity,
            equipment=equipment,
            floor=floor,
            location=location,
            max_booking_minutes=max_booking_minutes,
            name=name,
            requires_approval=requires_approval,
        )

        return office_create_meeting_room_request

