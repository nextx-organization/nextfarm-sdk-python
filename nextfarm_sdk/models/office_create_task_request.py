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

if TYPE_CHECKING:
  from ..models.office_task_link_input import OfficeTaskLinkInput





T = TypeVar("T", bound="OfficeCreateTaskRequest")



@_attrs_define
class OfficeCreateTaskRequest:
    

    assignee_id: None | Unset | UUID = UNSET
    auto_remind_overdue: bool | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    due_at: datetime.datetime | None | Unset = UNSET
    links: list[OfficeTaskLinkInput] | None | Unset = UNSET
    parcel_id: None | Unset | UUID = UNSET
    parent_task_id: None | Unset | UUID = UNSET
    priority: None | str | Unset = UNSET
    progress: int | None | Unset = UNSET
    remind_before_minutes: int | None | Unset = UNSET
    source_id: None | Unset | UUID = UNSET
    source_type: None | str | Unset = UNSET
    start_at: datetime.datetime | None | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    task_group_id: None | Unset | UUID = UNSET
    task_list_id: None | Unset | UUID = UNSET
    title: None | str | Unset = UNSET
    watcher_ids: list[UUID] | None | Unset = UNSET
    workload: float | None | Unset = UNSET
    workload_unit: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_task_link_input import OfficeTaskLinkInput # noqa: PLC0415
        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        elif isinstance(self.assignee_id, UUID):
            assignee_id = str(self.assignee_id)
        else:
            assignee_id = self.assignee_id

        auto_remind_overdue = self.auto_remind_overdue

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

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

        links: list[dict[str, Any]] | None | Unset
        if isinstance(self.links, Unset):
            links = UNSET
        elif isinstance(self.links, list):
            links = []
            for links_type_0_item_data in self.links:
                links_type_0_item = links_type_0_item_data.to_dict()
                links.append(links_type_0_item)


        else:
            links = self.links

        parcel_id: None | str | Unset
        if isinstance(self.parcel_id, Unset):
            parcel_id = UNSET
        elif isinstance(self.parcel_id, UUID):
            parcel_id = str(self.parcel_id)
        else:
            parcel_id = self.parcel_id

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

        remind_before_minutes: int | None | Unset
        if isinstance(self.remind_before_minutes, Unset):
            remind_before_minutes = UNSET
        else:
            remind_before_minutes = self.remind_before_minutes

        source_id: None | str | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        elif isinstance(self.source_id, UUID):
            source_id = str(self.source_id)
        else:
            source_id = self.source_id

        source_type: None | str | Unset
        if isinstance(self.source_type, Unset):
            source_type = UNSET
        else:
            source_type = self.source_type

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
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if auto_remind_overdue is not UNSET:
            field_dict["autoRemindOverdue"] = auto_remind_overdue
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if description is not UNSET:
            field_dict["description"] = description
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if links is not UNSET:
            field_dict["links"] = links
        if parcel_id is not UNSET:
            field_dict["parcelId"] = parcel_id
        if parent_task_id is not UNSET:
            field_dict["parentTaskId"] = parent_task_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if progress is not UNSET:
            field_dict["progress"] = progress
        if remind_before_minutes is not UNSET:
            field_dict["remindBeforeMinutes"] = remind_before_minutes
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
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
        from ..models.office_task_link_input import OfficeTaskLinkInput # noqa: PLC0415
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


        auto_remind_overdue = d.pop("autoRemindOverdue", UNSET)

        def _parse_branch_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                branch_id_type_0 = UUID(data)



                return branch_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        branch_id = _parse_branch_id(d.pop("branchId", UNSET))


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


        def _parse_links(data: object) -> list[OfficeTaskLinkInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                links_type_0 = []
                _links_type_0 = data
                for links_type_0_item_data in (_links_type_0):
                    links_type_0_item = OfficeTaskLinkInput.from_dict(links_type_0_item_data)



                    links_type_0.append(links_type_0_item)

                return links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTaskLinkInput] | None | Unset, data)

        links = _parse_links(d.pop("links", UNSET))


        def _parse_parcel_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parcel_id_type_0 = UUID(data)



                return parcel_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parcel_id = _parse_parcel_id(d.pop("parcelId", UNSET))


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


        def _parse_remind_before_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        remind_before_minutes = _parse_remind_before_minutes(d.pop("remindBeforeMinutes", UNSET))


        def _parse_source_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_id_type_0 = UUID(data)



                return source_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_id = _parse_source_id(d.pop("sourceId", UNSET))


        def _parse_source_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_type = _parse_source_type(d.pop("sourceType", UNSET))


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


        office_create_task_request = cls(
            assignee_id=assignee_id,
            auto_remind_overdue=auto_remind_overdue,
            branch_id=branch_id,
            description=description,
            due_at=due_at,
            links=links,
            parcel_id=parcel_id,
            parent_task_id=parent_task_id,
            priority=priority,
            progress=progress,
            remind_before_minutes=remind_before_minutes,
            source_id=source_id,
            source_type=source_type,
            start_at=start_at,
            tags=tags,
            task_group_id=task_group_id,
            task_list_id=task_list_id,
            title=title,
            watcher_ids=watcher_ids,
            workload=workload,
            workload_unit=workload_unit,
        )

        return office_create_task_request

