from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="OfficeTimesheetUserTotalDto")



@_attrs_define
class OfficeTimesheetUserTotalDto:
    

    entry_count: int | Unset = UNSET
    hours: float | Unset = UNSET
    user_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        entry_count = self.entry_count

        hours = self.hours

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if entry_count is not UNSET:
            field_dict["entryCount"] = entry_count
        if hours is not UNSET:
            field_dict["hours"] = hours
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entry_count = d.pop("entryCount", UNSET)

        hours = d.pop("hours", UNSET)

        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        office_timesheet_user_total_dto = cls(
            entry_count=entry_count,
            hours=hours,
            user_id=user_id,
        )

        return office_timesheet_user_total_dto

