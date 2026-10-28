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






T = TypeVar("T", bound="OfficeFarmEmergencyStopDto")



@_attrs_define
class OfficeFarmEmergencyStopDto:
    

    can_change: bool | Unset = UNSET
    changed_at: datetime.datetime | None | Unset = UNSET
    changed_by: None | Unset | UUID = UNSET
    stopped: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        can_change = self.can_change

        changed_at: None | str | Unset
        if isinstance(self.changed_at, Unset):
            changed_at = UNSET
        elif isinstance(self.changed_at, datetime.datetime):
            changed_at = self.changed_at.isoformat()
        else:
            changed_at = self.changed_at

        changed_by: None | str | Unset
        if isinstance(self.changed_by, Unset):
            changed_by = UNSET
        elif isinstance(self.changed_by, UUID):
            changed_by = str(self.changed_by)
        else:
            changed_by = self.changed_by

        stopped = self.stopped


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if can_change is not UNSET:
            field_dict["canChange"] = can_change
        if changed_at is not UNSET:
            field_dict["changedAt"] = changed_at
        if changed_by is not UNSET:
            field_dict["changedBy"] = changed_by
        if stopped is not UNSET:
            field_dict["stopped"] = stopped

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_change = d.pop("canChange", UNSET)

        def _parse_changed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changed_at_type_0 = datetime.datetime.fromisoformat(data)



                return changed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        changed_at = _parse_changed_at(d.pop("changedAt", UNSET))


        def _parse_changed_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changed_by_type_0 = UUID(data)



                return changed_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        changed_by = _parse_changed_by(d.pop("changedBy", UNSET))


        stopped = d.pop("stopped", UNSET)

        office_farm_emergency_stop_dto = cls(
            can_change=can_change,
            changed_at=changed_at,
            changed_by=changed_by,
            stopped=stopped,
        )

        return office_farm_emergency_stop_dto

