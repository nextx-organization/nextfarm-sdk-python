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






T = TypeVar("T", bound="OfficeTimesheetLockDto")



@_attrs_define
class OfficeTimesheetLockDto:
    

    end_date: datetime.date | Unset = UNSET
    id: UUID | Unset = UNSET
    locked_at: datetime.datetime | Unset = UNSET
    locked_by: UUID | Unset = UNSET
    reason: None | str | Unset = UNSET
    start_date: datetime.date | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        locked_at: str | Unset = UNSET
        if not isinstance(self.locked_at, Unset):
            locked_at = self.locked_at.isoformat()

        locked_by: str | Unset = UNSET
        if not isinstance(self.locked_by, Unset):
            locked_by = str(self.locked_by)

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if id is not UNSET:
            field_dict["id"] = id
        if locked_at is not UNSET:
            field_dict["lockedAt"] = locked_at
        if locked_by is not UNSET:
            field_dict["lockedBy"] = locked_by
        if reason is not UNSET:
            field_dict["reason"] = reason
        if start_date is not UNSET:
            field_dict["startDate"] = start_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _end_date = d.pop("endDate", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _locked_at = d.pop("lockedAt", UNSET)
        locked_at: datetime.datetime | Unset
        if isinstance(_locked_at,  Unset):
            locked_at = UNSET
        else:
            locked_at = datetime.datetime.fromisoformat(_locked_at)




        _locked_by = d.pop("lockedBy", UNSET)
        locked_by: UUID | Unset
        if isinstance(_locked_by,  Unset):
            locked_by = UNSET
        else:
            locked_by = UUID(_locked_by)




        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        office_timesheet_lock_dto = cls(
            end_date=end_date,
            id=id,
            locked_at=locked_at,
            locked_by=locked_by,
            reason=reason,
            start_date=start_date,
        )

        return office_timesheet_lock_dto

