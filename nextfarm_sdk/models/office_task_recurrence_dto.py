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






T = TypeVar("T", bound="OfficeTaskRecurrenceDto")



@_attrs_define
class OfficeTaskRecurrenceDto:
    

    assignee_id: None | Unset | UUID = UNSET
    assigner_id: UUID | Unset = UNSET
    auto_remind_overdue: bool | Unset = UNSET
    description: None | str | Unset = UNSET
    due_offset_minutes: int | None | Unset = UNSET
    id: UUID | Unset = UNSET
    is_active: bool | Unset = UNSET
    next_occurrence_at: datetime.datetime | None | Unset = UNSET
    priority: None | str | Unset = UNSET
    recurrence_rule: None | str | Unset = UNSET
    remind_before_minutes: int | None | Unset = UNSET
    start_at: datetime.datetime | Unset = UNSET
    title: None | str | Unset = UNSET
    until_at: datetime.datetime | None | Unset = UNSET
    workload: float | None | Unset = UNSET
    workload_unit: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        elif isinstance(self.assignee_id, UUID):
            assignee_id = str(self.assignee_id)
        else:
            assignee_id = self.assignee_id

        assigner_id: str | Unset = UNSET
        if not isinstance(self.assigner_id, Unset):
            assigner_id = str(self.assigner_id)

        auto_remind_overdue = self.auto_remind_overdue

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        due_offset_minutes: int | None | Unset
        if isinstance(self.due_offset_minutes, Unset):
            due_offset_minutes = UNSET
        else:
            due_offset_minutes = self.due_offset_minutes

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_active = self.is_active

        next_occurrence_at: None | str | Unset
        if isinstance(self.next_occurrence_at, Unset):
            next_occurrence_at = UNSET
        elif isinstance(self.next_occurrence_at, datetime.datetime):
            next_occurrence_at = self.next_occurrence_at.isoformat()
        else:
            next_occurrence_at = self.next_occurrence_at

        priority: None | str | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        recurrence_rule: None | str | Unset
        if isinstance(self.recurrence_rule, Unset):
            recurrence_rule = UNSET
        else:
            recurrence_rule = self.recurrence_rule

        remind_before_minutes: int | None | Unset
        if isinstance(self.remind_before_minutes, Unset):
            remind_before_minutes = UNSET
        else:
            remind_before_minutes = self.remind_before_minutes

        start_at: str | Unset = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        until_at: None | str | Unset
        if isinstance(self.until_at, Unset):
            until_at = UNSET
        elif isinstance(self.until_at, datetime.datetime):
            until_at = self.until_at.isoformat()
        else:
            until_at = self.until_at

        workload: float | None | Unset
        if isinstance(self.workload, Unset):
            workload = UNSET
        else:
            workload = self.workload

        workload_unit: None | str | Unset
        if isinstance(self.workload_unit, Unset):
            workload_unit = UNSET
        else:
            workload_unit = self.workload_unit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if assigner_id is not UNSET:
            field_dict["assignerId"] = assigner_id
        if auto_remind_overdue is not UNSET:
            field_dict["autoRemindOverdue"] = auto_remind_overdue
        if description is not UNSET:
            field_dict["description"] = description
        if due_offset_minutes is not UNSET:
            field_dict["dueOffsetMinutes"] = due_offset_minutes
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if next_occurrence_at is not UNSET:
            field_dict["nextOccurrenceAt"] = next_occurrence_at
        if priority is not UNSET:
            field_dict["priority"] = priority
        if recurrence_rule is not UNSET:
            field_dict["recurrenceRule"] = recurrence_rule
        if remind_before_minutes is not UNSET:
            field_dict["remindBeforeMinutes"] = remind_before_minutes
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if title is not UNSET:
            field_dict["title"] = title
        if until_at is not UNSET:
            field_dict["untilAt"] = until_at
        if workload is not UNSET:
            field_dict["workload"] = workload
        if workload_unit is not UNSET:
            field_dict["workloadUnit"] = workload_unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_assignee_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assignee_id_type_0 = UUID(data)



                return assignee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        assignee_id = _parse_assignee_id(d.pop("assigneeId", UNSET))


        _assigner_id = d.pop("assignerId", UNSET)
        assigner_id: UUID | Unset
        if isinstance(_assigner_id,  Unset):
            assigner_id = UNSET
        else:
            assigner_id = UUID(_assigner_id)




        auto_remind_overdue = d.pop("autoRemindOverdue", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_due_offset_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        due_offset_minutes = _parse_due_offset_minutes(d.pop("dueOffsetMinutes", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_active = d.pop("isActive", UNSET)

        def _parse_next_occurrence_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_occurrence_at_type_0 = datetime.datetime.fromisoformat(data)



                return next_occurrence_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_occurrence_at = _parse_next_occurrence_at(d.pop("nextOccurrenceAt", UNSET))


        def _parse_priority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))


        def _parse_recurrence_rule(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recurrence_rule = _parse_recurrence_rule(d.pop("recurrenceRule", UNSET))


        def _parse_remind_before_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        remind_before_minutes = _parse_remind_before_minutes(d.pop("remindBeforeMinutes", UNSET))


        _start_at = d.pop("startAt", UNSET)
        start_at: datetime.datetime | Unset
        if isinstance(_start_at,  Unset):
            start_at = UNSET
        else:
            start_at = datetime.datetime.fromisoformat(_start_at)




        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_until_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                until_at_type_0 = datetime.datetime.fromisoformat(data)



                return until_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        until_at = _parse_until_at(d.pop("untilAt", UNSET))


        def _parse_workload(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        workload = _parse_workload(d.pop("workload", UNSET))


        def _parse_workload_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workload_unit = _parse_workload_unit(d.pop("workloadUnit", UNSET))


        office_task_recurrence_dto = cls(
            assignee_id=assignee_id,
            assigner_id=assigner_id,
            auto_remind_overdue=auto_remind_overdue,
            description=description,
            due_offset_minutes=due_offset_minutes,
            id=id,
            is_active=is_active,
            next_occurrence_at=next_occurrence_at,
            priority=priority,
            recurrence_rule=recurrence_rule,
            remind_before_minutes=remind_before_minutes,
            start_at=start_at,
            title=title,
            until_at=until_at,
            workload=workload,
            workload_unit=workload_unit,
        )

        return office_task_recurrence_dto

