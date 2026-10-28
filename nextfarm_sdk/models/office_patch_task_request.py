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






T = TypeVar("T", bound="OfficePatchTaskRequest")



@_attrs_define
class OfficePatchTaskRequest:
    

    description: None | str | Unset = UNSET
    due_at: datetime.datetime | None | Unset = UNSET
    fields: list[str] | None | Unset = UNSET
    parent_task_id: None | Unset | UUID = UNSET
    priority: None | str | Unset = UNSET
    progress: int | None | Unset = UNSET
    requires_review: bool | None | Unset = UNSET
    rev: int | None | Unset = UNSET
    reviewer_id: None | Unset | UUID = UNSET
    start_at: datetime.datetime | None | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    task_group_id: None | Unset | UUID = UNSET
    task_list_id: None | Unset | UUID = UNSET
    title: None | str | Unset = UNSET
    watcher_ids: list[UUID] | None | Unset = UNSET
    workload: float | None | Unset = UNSET
    workload_unit: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        due_at: None | str | Unset
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        fields: list[str] | None | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = self.fields


        else:
            fields = self.fields

        parent_task_id: None | str | Unset
        if isinstance(self.parent_task_id, Unset):
            parent_task_id = UNSET
        elif isinstance(self.parent_task_id, UUID):
            parent_task_id = str(self.parent_task_id)
        else:
            parent_task_id = self.parent_task_id

        priority: None | str | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        progress: int | None | Unset
        if isinstance(self.progress, Unset):
            progress = UNSET
        else:
            progress = self.progress

        requires_review: bool | None | Unset
        if isinstance(self.requires_review, Unset):
            requires_review = UNSET
        else:
            requires_review = self.requires_review

        rev: int | None | Unset
        if isinstance(self.rev, Unset):
            rev = UNSET
        else:
            rev = self.rev

        reviewer_id: None | str | Unset
        if isinstance(self.reviewer_id, Unset):
            reviewer_id = UNSET
        elif isinstance(self.reviewer_id, UUID):
            reviewer_id = str(self.reviewer_id)
        else:
            reviewer_id = self.reviewer_id

        start_at: None | str | Unset
        if isinstance(self.start_at, Unset):
            start_at = UNSET
        elif isinstance(self.start_at, datetime.datetime):
            start_at = self.start_at.isoformat()
        else:
            start_at = self.start_at

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags


        else:
            tags = self.tags

        task_group_id: None | str | Unset
        if isinstance(self.task_group_id, Unset):
            task_group_id = UNSET
        elif isinstance(self.task_group_id, UUID):
            task_group_id = str(self.task_group_id)
        else:
            task_group_id = self.task_group_id

        task_list_id: None | str | Unset
        if isinstance(self.task_list_id, Unset):
            task_list_id = UNSET
        elif isinstance(self.task_list_id, UUID):
            task_list_id = str(self.task_list_id)
        else:
            task_list_id = self.task_list_id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        watcher_ids: list[str] | None | Unset
        if isinstance(self.watcher_ids, Unset):
            watcher_ids = UNSET
        elif isinstance(self.watcher_ids, list):
            watcher_ids = []
            for watcher_ids_type_0_item_data in self.watcher_ids:
                watcher_ids_type_0_item = str(watcher_ids_type_0_item_data)
                watcher_ids.append(watcher_ids_type_0_item)


        else:
            watcher_ids = self.watcher_ids

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
        if description is not UNSET:
            field_dict["description"] = description
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if fields is not UNSET:
            field_dict["fields"] = fields
        if parent_task_id is not UNSET:
            field_dict["parentTaskId"] = parent_task_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if progress is not UNSET:
            field_dict["progress"] = progress
        if requires_review is not UNSET:
            field_dict["requiresReview"] = requires_review
        if rev is not UNSET:
            field_dict["rev"] = rev
        if reviewer_id is not UNSET:
            field_dict["reviewerId"] = reviewer_id
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if tags is not UNSET:
            field_dict["tags"] = tags
        if task_group_id is not UNSET:
            field_dict["taskGroupId"] = task_group_id
        if task_list_id is not UNSET:
            field_dict["taskListId"] = task_list_id
        if title is not UNSET:
            field_dict["title"] = title
        if watcher_ids is not UNSET:
            field_dict["watcherIds"] = watcher_ids
        if workload is not UNSET:
            field_dict["workload"] = workload
        if workload_unit is not UNSET:
            field_dict["workloadUnit"] = workload_unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


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


        def _parse_fields(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_0 = cast(list[str], data)

                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        fields = _parse_fields(d.pop("fields", UNSET))


        def _parse_parent_task_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_task_id_type_0 = UUID(data)



                return parent_task_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_task_id = _parse_parent_task_id(d.pop("parentTaskId", UNSET))


        def _parse_priority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))


        def _parse_progress(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        progress = _parse_progress(d.pop("progress", UNSET))


        def _parse_requires_review(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        requires_review = _parse_requires_review(d.pop("requiresReview", UNSET))


        def _parse_rev(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rev = _parse_rev(d.pop("rev", UNSET))


        def _parse_reviewer_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewer_id_type_0 = UUID(data)



                return reviewer_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reviewer_id = _parse_reviewer_id(d.pop("reviewerId", UNSET))


        def _parse_start_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_at_type_0 = datetime.datetime.fromisoformat(data)



                return start_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_at = _parse_start_at(d.pop("startAt", UNSET))


        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))


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


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_watcher_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                watcher_ids_type_0 = []
                _watcher_ids_type_0 = data
                for watcher_ids_type_0_item_data in (_watcher_ids_type_0):
                    watcher_ids_type_0_item = UUID(watcher_ids_type_0_item_data)



                    watcher_ids_type_0.append(watcher_ids_type_0_item)

                return watcher_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        watcher_ids = _parse_watcher_ids(d.pop("watcherIds", UNSET))


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


        office_patch_task_request = cls(
            description=description,
            due_at=due_at,
            fields=fields,
            parent_task_id=parent_task_id,
            priority=priority,
            progress=progress,
            requires_review=requires_review,
            rev=rev,
            reviewer_id=reviewer_id,
            start_at=start_at,
            tags=tags,
            task_group_id=task_group_id,
            task_list_id=task_list_id,
            title=title,
            watcher_ids=watcher_ids,
            workload=workload,
            workload_unit=workload_unit,
        )

        return office_patch_task_request

