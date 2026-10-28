from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficeBusySlotDto")



@_attrs_define
class OfficeBusySlotDto:
    

    end_at: datetime.datetime | Unset = UNSET
    start_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        end_at: str | Unset = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        start_at: str | Unset = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if end_at is not UNSET:
            field_dict["endAt"] = end_at
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




        _start_at = d.pop("startAt", UNSET)
        start_at: datetime.datetime | Unset
        if isinstance(_start_at,  Unset):
            start_at = UNSET
        else:
            start_at = datetime.datetime.fromisoformat(_start_at)




        office_busy_slot_dto = cls(
            end_at=end_at,
            start_at=start_at,
        )

        return office_busy_slot_dto

