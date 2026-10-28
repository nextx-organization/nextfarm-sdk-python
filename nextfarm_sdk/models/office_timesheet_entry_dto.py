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






T = TypeVar("T", bound="OfficeTimesheetEntryDto")



@_attrs_define
class OfficeTimesheetEntryDto:
    

    created_at: datetime.datetime | Unset = UNSET
    ended_at: None | str | Unset = UNSET
    hours: float | Unset = UNSET
    id: UUID | Unset = UNSET
    is_editable: bool | Unset = UNSET
    note: None | str | Unset = UNSET
    started_at: None | str | Unset = UNSET
    task_id: None | Unset | UUID = UNSET
    task_title: None | str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    user_id: UUID | Unset = UNSET
    work_date: datetime.date | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        ended_at: None | str | Unset
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        else:
            ended_at = self.ended_at

        hours = self.hours

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_editable = self.is_editable

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

        task_title: None | str | Unset
        if isinstance(self.task_title, Unset):
            task_title = UNSET
        else:
            task_title = self.task_title

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        work_date: str | Unset = UNSET
        if not isinstance(self.work_date, Unset):
            work_date = self.work_date.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if hours is not UNSET:
            field_dict["hours"] = hours
        if id is not UNSET:
            field_dict["id"] = id
        if is_editable is not UNSET:
            field_dict["isEditable"] = is_editable
        if note is not UNSET:
            field_dict["note"] = note
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if task_title is not UNSET:
            field_dict["taskTitle"] = task_title
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if work_date is not UNSET:
            field_dict["workDate"] = work_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_ended_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ended_at = _parse_ended_at(d.pop("endedAt", UNSET))


        hours = d.pop("hours", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_editable = d.pop("isEditable", UNSET)

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


        def _parse_task_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_title = _parse_task_title(d.pop("taskTitle", UNSET))


        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        _work_date = d.pop("workDate", UNSET)
        work_date: datetime.date | Unset
        if isinstance(_work_date,  Unset):
            work_date = UNSET
        else:
            work_date = datetime.date.fromisoformat(_work_date)




        office_timesheet_entry_dto = cls(
            created_at=created_at,
            ended_at=ended_at,
            hours=hours,
            id=id,
            is_editable=is_editable,
            note=note,
            started_at=started_at,
            task_id=task_id,
            task_title=task_title,
            updated_at=updated_at,
            user_id=user_id,
            work_date=work_date,
        )

        return office_timesheet_entry_dto

