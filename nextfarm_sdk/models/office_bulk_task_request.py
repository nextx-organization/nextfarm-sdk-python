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






T = TypeVar("T", bound="OfficeBulkTaskRequest")



@_attrs_define
class OfficeBulkTaskRequest:
    

    action: None | str | Unset = UNSET
    assignee_id: None | Unset | UUID = UNSET
    due_at: datetime.datetime | None | Unset = UNSET
    priority: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    task_group_id: None | Unset | UUID = UNSET
    task_ids: list[UUID] | None | Unset = UNSET
    task_list_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        else:
            action = self.action

        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        elif isinstance(self.assignee_id, UUID):
            assignee_id = str(self.assignee_id)
        else:
            assignee_id = self.assignee_id

        due_at: None | str | Unset
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        priority: None | str | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        task_group_id: None | str | Unset
        if isinstance(self.task_group_id, Unset):
            task_group_id = UNSET
        elif isinstance(self.task_group_id, UUID):
            task_group_id = str(self.task_group_id)
        else:
            task_group_id = self.task_group_id

        task_ids: list[str] | None | Unset
        if isinstance(self.task_ids, Unset):
            task_ids = UNSET
        elif isinstance(self.task_ids, list):
            task_ids = []
            for task_ids_type_0_item_data in self.task_ids:
                task_ids_type_0_item = str(task_ids_type_0_item_data)
                task_ids.append(task_ids_type_0_item)


        else:
            task_ids = self.task_ids

        task_list_id: None | str | Unset
        if isinstance(self.task_list_id, Unset):
            task_list_id = UNSET
        elif isinstance(self.task_list_id, UUID):
            task_list_id = str(self.task_list_id)
        else:
            task_list_id = self.task_list_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if action is not UNSET:
            field_dict["action"] = action
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if priority is not UNSET:
            field_dict["priority"] = priority
        if status is not UNSET:
            field_dict["status"] = status
        if task_group_id is not UNSET:
            field_dict["taskGroupId"] = task_group_id
        if task_ids is not UNSET:
            field_dict["taskIds"] = task_ids
        if task_list_id is not UNSET:
            field_dict["taskListId"] = task_list_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action = _parse_action(d.pop("action", UNSET))


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


        def _parse_due_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = datetime.datetime.fromisoformat(data)



                return due_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        due_at = _parse_due_at(d.pop("dueAt", UNSET))


        def _parse_priority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_task_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                task_group_id_type_0 = UUID(data)



                return task_group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        task_group_id = _parse_task_group_id(d.pop("taskGroupId", UNSET))


        def _parse_task_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                task_ids_type_0 = []
                _task_ids_type_0 = data
                for task_ids_type_0_item_data in (_task_ids_type_0):
                    task_ids_type_0_item = UUID(task_ids_type_0_item_data)



                    task_ids_type_0.append(task_ids_type_0_item)

                return task_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        task_ids = _parse_task_ids(d.pop("taskIds", UNSET))


        def _parse_task_list_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                task_list_id_type_0 = UUID(data)



                return task_list_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        task_list_id = _parse_task_list_id(d.pop("taskListId", UNSET))


        office_bulk_task_request = cls(
            action=action,
            assignee_id=assignee_id,
            due_at=due_at,
            priority=priority,
            status=status,
            task_group_id=task_group_id,
            task_ids=task_ids,
            task_list_id=task_list_id,
        )

        return office_bulk_task_request

