from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeTimesheetWeekRowDto")



@_attrs_define
class OfficeTimesheetWeekRowDto:
    

    hours: list[float] | None | Unset = UNSET
    task_id: None | Unset | UUID = UNSET
    task_title: None | str | Unset = UNSET
    total: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        hours: list[float] | None | Unset
        if isinstance(self.hours, Unset):
            hours = UNSET
        elif isinstance(self.hours, list):
            hours = self.hours


        else:
            hours = self.hours

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

        total = self.total


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if hours is not UNSET:
            field_dict["hours"] = hours
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if task_title is not UNSET:
            field_dict["taskTitle"] = task_title
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_hours(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hours_type_0 = cast(list[float], data)

                return hours_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        hours = _parse_hours(d.pop("hours", UNSET))


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


        total = d.pop("total", UNSET)

        office_timesheet_week_row_dto = cls(
            hours=hours,
            task_id=task_id,
            task_title=task_title,
            total=total,
        )

        return office_timesheet_week_row_dto

