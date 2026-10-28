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






T = TypeVar("T", bound="OfficeUpdateTimesheetEntryRequest")



@_attrs_define
class OfficeUpdateTimesheetEntryRequest:
    

    ended_at: None | str | Unset = UNSET
    hours: float | None | Unset = UNSET
    note: None | str | Unset = UNSET
    started_at: None | str | Unset = UNSET
    task_id: None | Unset | UUID = UNSET
    work_date: datetime.date | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ended_at: None | str | Unset
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        else:
            ended_at = self.ended_at

        hours: float | None | Unset
        if isinstance(self.hours, Unset):
            hours = UNSET
        else:
            hours = self.hours

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        task_id: None | str | Unset
        if isinstance(self.task_id, Unset):
            task_id = UNSET
        elif isinstance(self.task_id, UUID):
            task_id = str(self.task_id)
        else:
            task_id = self.task_id

        work_date: str | Unset = UNSET
        if not isinstance(self.work_date, Unset):
            work_date = self.work_date.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if hours is not UNSET:
            field_dict["hours"] = hours
        if note is not UNSET:
            field_dict["note"] = note
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if work_date is not UNSET:
            field_dict["workDate"] = work_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_ended_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ended_at = _parse_ended_at(d.pop("endedAt", UNSET))


        def _parse_hours(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hours = _parse_hours(d.pop("hours", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_started_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        started_at = _parse_started_at(d.pop("startedAt", UNSET))


        def _parse_task_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                task_id_type_0 = UUID(data)



                return task_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        task_id = _parse_task_id(d.pop("taskId", UNSET))


        _work_date = d.pop("workDate", UNSET)
        work_date: datetime.date | Unset
        if isinstance(_work_date,  Unset):
            work_date = UNSET
        else:
            work_date = datetime.date.fromisoformat(_work_date)




        office_update_timesheet_entry_request = cls(
            ended_at=ended_at,
            hours=hours,
            note=note,
            started_at=started_at,
            task_id=task_id,
            work_date=work_date,
        )

        return office_update_timesheet_entry_request

