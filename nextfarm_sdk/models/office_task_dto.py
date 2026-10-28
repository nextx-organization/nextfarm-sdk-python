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
  from ..models.office_task_dto_custom_fields_type_0 import OfficeTaskDtoCustomFieldsType0
  from ..models.office_task_link_dto import OfficeTaskLinkDto





T = TypeVar("T", bound="OfficeTaskDto")



@_attrs_define
class OfficeTaskDto:
    

    assignee_id: None | Unset | UUID = UNSET
    assigner_id: UUID | Unset = UNSET
    attachment_count: int | Unset = UNSET
    auto_remind_overdue: bool | Unset = UNSET
    blocked_by_count: int | Unset = UNSET
    branch_id: None | Unset | UUID = UNSET
    can_edit: bool | None | Unset = UNSET
    checklist_done: int | Unset = UNSET
    checklist_total: int | Unset = UNSET
    code: None | str | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    custom_fields: None | OfficeTaskDtoCustomFieldsType0 | Unset = UNSET
    description: None | str | Unset = UNSET
    due_at: datetime.datetime | None | Unset = UNSET
    effective_due_at: datetime.datetime | None | Unset = UNSET
    id: UUID | Unset = UNSET
    is_overdue: bool | Unset = UNSET
    links: list[OfficeTaskLinkDto] | None | Unset = UNSET
    parcel_id: None | Unset | UUID = UNSET
    parent_task_id: None | Unset | UUID = UNSET
    parent_title: None | str | Unset = UNSET
    priority: None | str | Unset = UNSET
    progress: int | None | Unset = UNSET
    remind_before_minutes: int | None | Unset = UNSET
    requires_review: bool | Unset = UNSET
    result_note: None | str | Unset = UNSET
    return_reason: None | str | Unset = UNSET
    rev: int | Unset = UNSET
    reviewer_id: None | Unset | UUID = UNSET
    sort_order: int | Unset = UNSET
    source_author_id: None | Unset | UUID = UNSET
    source_channel_accessible: bool | None | Unset = UNSET
    source_channel_id: None | Unset | UUID = UNSET
    source_channel_name: None | str | Unset = UNSET
    source_id: None | Unset | UUID = UNSET
    source_message_at: datetime.datetime | None | Unset = UNSET
    source_type: None | str | Unset = UNSET
    start_at: datetime.datetime | None | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    status: None | str | Unset = UNSET
    subtask_assignee_ids: list[UUID] | None | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    task_group_id: None | Unset | UUID = UNSET
    task_list_id: None | Unset | UUID = UNSET
    task_status_color: None | str | Unset = UNSET
    task_status_id: None | Unset | UUID = UNSET
    task_status_name: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    watcher_ids: list[UUID] | None | Unset = UNSET
    workload: float | None | Unset = UNSET
    workload_unit: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_task_dto_custom_fields_type_0 import OfficeTaskDtoCustomFieldsType0 # noqa: PLC0415
        from ..models.office_task_link_dto import OfficeTaskLinkDto # noqa: PLC0415
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

        attachment_count = self.attachment_count

        auto_remind_overdue = self.auto_remind_overdue

        blocked_by_count = self.blocked_by_count

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        can_edit: bool | None | Unset
        if isinstance(self.can_edit, Unset):
            can_edit = UNSET
        else:
            can_edit = self.can_edit

        checklist_done = self.checklist_done

        checklist_total = self.checklist_total

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        custom_fields: dict[str, Any] | None | Unset
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, OfficeTaskDtoCustomFieldsType0):
            custom_fields = self.custom_fields.to_dict()
        else:
            custom_fields = self.custom_fields

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

        effective_due_at: None | str | Unset
        if isinstance(self.effective_due_at, Unset):
            effective_due_at = UNSET
        elif isinstance(self.effective_due_at, datetime.datetime):
            effective_due_at = self.effective_due_at.isoformat()
        else:
            effective_due_at = self.effective_due_at

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_overdue = self.is_overdue

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

        parent_title: None | str | Unset
        if isinstance(self.parent_title, Unset):
            parent_title = UNSET
        else:
            parent_title = self.parent_title

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

        requires_review = self.requires_review

        result_note: None | str | Unset
        if isinstance(self.result_note, Unset):
            result_note = UNSET
        else:
            result_note = self.result_note

        return_reason: None | str | Unset
        if isinstance(self.return_reason, Unset):
            return_reason = UNSET
        else:
            return_reason = self.return_reason

        rev = self.rev

        reviewer_id: None | str | Unset
        if isinstance(self.reviewer_id, Unset):
            reviewer_id = UNSET
        elif isinstance(self.reviewer_id, UUID):
            reviewer_id = str(self.reviewer_id)
        else:
            reviewer_id = self.reviewer_id

        sort_order = self.sort_order

        source_author_id: None | str | Unset
        if isinstance(self.source_author_id, Unset):
            source_author_id = UNSET
        elif isinstance(self.source_author_id, UUID):
            source_author_id = str(self.source_author_id)
        else:
            source_author_id = self.source_author_id

        source_channel_accessible: bool | None | Unset
        if isinstance(self.source_channel_accessible, Unset):
            source_channel_accessible = UNSET
        else:
            source_channel_accessible = self.source_channel_accessible

        source_channel_id: None | str | Unset
        if isinstance(self.source_channel_id, Unset):
            source_channel_id = UNSET
        elif isinstance(self.source_channel_id, UUID):
            source_channel_id = str(self.source_channel_id)
        else:
            source_channel_id = self.source_channel_id

        source_channel_name: None | str | Unset
        if isinstance(self.source_channel_name, Unset):
            source_channel_name = UNSET
        else:
            source_channel_name = self.source_channel_name

        source_id: None | str | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        elif isinstance(self.source_id, UUID):
            source_id = str(self.source_id)
        else:
            source_id = self.source_id

        source_message_at: None | str | Unset
        if isinstance(self.source_message_at, Unset):
            source_message_at = UNSET
        elif isinstance(self.source_message_at, datetime.datetime):
            source_message_at = self.source_message_at.isoformat()
        else:
            source_message_at = self.source_message_at

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

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        subtask_assignee_ids: list[str] | None | Unset
        if isinstance(self.subtask_assignee_ids, Unset):
            subtask_assignee_ids = UNSET
        elif isinstance(self.subtask_assignee_ids, list):
            subtask_assignee_ids = []
            for subtask_assignee_ids_type_0_item_data in self.subtask_assignee_ids:
                subtask_assignee_ids_type_0_item = str(subtask_assignee_ids_type_0_item_data)
                subtask_assignee_ids.append(subtask_assignee_ids_type_0_item)


        else:
            subtask_assignee_ids = self.subtask_assignee_ids

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

        task_status_color: None | str | Unset
        if isinstance(self.task_status_color, Unset):
            task_status_color = UNSET
        else:
            task_status_color = self.task_status_color

        task_status_id: None | str | Unset
        if isinstance(self.task_status_id, Unset):
            task_status_id = UNSET
        elif isinstance(self.task_status_id, UUID):
            task_status_id = str(self.task_status_id)
        else:
            task_status_id = self.task_status_id

        task_status_name: None | str | Unset
        if isinstance(self.task_status_name, Unset):
            task_status_name = UNSET
        else:
            task_status_name = self.task_status_name

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

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
        if assigner_id is not UNSET:
            field_dict["assignerId"] = assigner_id
        if attachment_count is not UNSET:
            field_dict["attachmentCount"] = attachment_count
        if auto_remind_overdue is not UNSET:
            field_dict["autoRemindOverdue"] = auto_remind_overdue
        if blocked_by_count is not UNSET:
            field_dict["blockedByCount"] = blocked_by_count
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if can_edit is not UNSET:
            field_dict["canEdit"] = can_edit
        if checklist_done is not UNSET:
            field_dict["checklistDone"] = checklist_done
        if checklist_total is not UNSET:
            field_dict["checklistTotal"] = checklist_total
        if code is not UNSET:
            field_dict["code"] = code
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if description is not UNSET:
            field_dict["description"] = description
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if effective_due_at is not UNSET:
            field_dict["effectiveDueAt"] = effective_due_at
        if id is not UNSET:
            field_dict["id"] = id
        if is_overdue is not UNSET:
            field_dict["isOverdue"] = is_overdue
        if links is not UNSET:
            field_dict["links"] = links
        if parcel_id is not UNSET:
            field_dict["parcelId"] = parcel_id
        if parent_task_id is not UNSET:
            field_dict["parentTaskId"] = parent_task_id
        if parent_title is not UNSET:
            field_dict["parentTitle"] = parent_title
        if priority is not UNSET:
            field_dict["priority"] = priority
        if progress is not UNSET:
            field_dict["progress"] = progress
        if remind_before_minutes is not UNSET:
            field_dict["remindBeforeMinutes"] = remind_before_minutes
        if requires_review is not UNSET:
            field_dict["requiresReview"] = requires_review
        if result_note is not UNSET:
            field_dict["resultNote"] = result_note
        if return_reason is not UNSET:
            field_dict["returnReason"] = return_reason
        if rev is not UNSET:
            field_dict["rev"] = rev
        if reviewer_id is not UNSET:
            field_dict["reviewerId"] = reviewer_id
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if source_author_id is not UNSET:
            field_dict["sourceAuthorId"] = source_author_id
        if source_channel_accessible is not UNSET:
            field_dict["sourceChannelAccessible"] = source_channel_accessible
        if source_channel_id is not UNSET:
            field_dict["sourceChannelId"] = source_channel_id
        if source_channel_name is not UNSET:
            field_dict["sourceChannelName"] = source_channel_name
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if source_message_at is not UNSET:
            field_dict["sourceMessageAt"] = source_message_at
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if subtask_assignee_ids is not UNSET:
            field_dict["subtaskAssigneeIds"] = subtask_assignee_ids
        if tags is not UNSET:
            field_dict["tags"] = tags
        if task_group_id is not UNSET:
            field_dict["taskGroupId"] = task_group_id
        if task_list_id is not UNSET:
            field_dict["taskListId"] = task_list_id
        if task_status_color is not UNSET:
            field_dict["taskStatusColor"] = task_status_color
        if task_status_id is not UNSET:
            field_dict["taskStatusId"] = task_status_id
        if task_status_name is not UNSET:
            field_dict["taskStatusName"] = task_status_name
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if watcher_ids is not UNSET:
            field_dict["watcherIds"] = watcher_ids
        if workload is not UNSET:
            field_dict["workload"] = workload
        if workload_unit is not UNSET:
            field_dict["workloadUnit"] = workload_unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_task_dto_custom_fields_type_0 import OfficeTaskDtoCustomFieldsType0 # noqa: PLC0415
        from ..models.office_task_link_dto import OfficeTaskLinkDto # noqa: PLC0415
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




        attachment_count = d.pop("attachmentCount", UNSET)

        auto_remind_overdue = d.pop("autoRemindOverdue", UNSET)

        blocked_by_count = d.pop("blockedByCount", UNSET)

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


        def _parse_can_edit(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_edit = _parse_can_edit(d.pop("canEdit", UNSET))


        checklist_done = d.pop("checklistDone", UNSET)

        checklist_total = d.pop("checklistTotal", UNSET)

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)



                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_custom_fields(data: object) -> None | OfficeTaskDtoCustomFieldsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_fields_type_0 = OfficeTaskDtoCustomFieldsType0.from_dict(data)



                return custom_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OfficeTaskDtoCustomFieldsType0 | Unset, data)

        custom_fields = _parse_custom_fields(d.pop("customFields", UNSET))


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


        def _parse_effective_due_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_due_at_type_0 = datetime.datetime.fromisoformat(data)



                return effective_due_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        effective_due_at = _parse_effective_due_at(d.pop("effectiveDueAt", UNSET))


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_overdue = d.pop("isOverdue", UNSET)

        def _parse_links(data: object) -> list[OfficeTaskLinkDto] | None | Unset:
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
                    links_type_0_item = OfficeTaskLinkDto.from_dict(links_type_0_item_data)



                    links_type_0.append(links_type_0_item)

                return links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTaskLinkDto] | None | Unset, data)

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


        def _parse_parent_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_title = _parse_parent_title(d.pop("parentTitle", UNSET))


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


        requires_review = d.pop("requiresReview", UNSET)

        def _parse_result_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result_note = _parse_result_note(d.pop("resultNote", UNSET))


        def _parse_return_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        return_reason = _parse_return_reason(d.pop("returnReason", UNSET))


        rev = d.pop("rev", UNSET)

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


        sort_order = d.pop("sortOrder", UNSET)

        def _parse_source_author_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_author_id_type_0 = UUID(data)



                return source_author_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_author_id = _parse_source_author_id(d.pop("sourceAuthorId", UNSET))


        def _parse_source_channel_accessible(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        source_channel_accessible = _parse_source_channel_accessible(d.pop("sourceChannelAccessible", UNSET))


        def _parse_source_channel_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_channel_id_type_0 = UUID(data)



                return source_channel_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_channel_id = _parse_source_channel_id(d.pop("sourceChannelId", UNSET))


        def _parse_source_channel_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_channel_name = _parse_source_channel_name(d.pop("sourceChannelName", UNSET))


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


        def _parse_source_message_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_message_at_type_0 = datetime.datetime.fromisoformat(data)



                return source_message_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        source_message_at = _parse_source_message_at(d.pop("sourceMessageAt", UNSET))


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


        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)



                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("startedAt", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_subtask_assignee_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subtask_assignee_ids_type_0 = []
                _subtask_assignee_ids_type_0 = data
                for subtask_assignee_ids_type_0_item_data in (_subtask_assignee_ids_type_0):
                    subtask_assignee_ids_type_0_item = UUID(subtask_assignee_ids_type_0_item_data)



                    subtask_assignee_ids_type_0.append(subtask_assignee_ids_type_0_item)

                return subtask_assignee_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        subtask_assignee_ids = _parse_subtask_assignee_ids(d.pop("subtaskAssigneeIds", UNSET))


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


        def _parse_task_status_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_status_color = _parse_task_status_color(d.pop("taskStatusColor", UNSET))


        def _parse_task_status_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                task_status_id_type_0 = UUID(data)



                return task_status_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        task_status_id = _parse_task_status_id(d.pop("taskStatusId", UNSET))


        def _parse_task_status_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_status_name = _parse_task_status_name(d.pop("taskStatusName", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




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


        office_task_dto = cls(
            assignee_id=assignee_id,
            assigner_id=assigner_id,
            attachment_count=attachment_count,
            auto_remind_overdue=auto_remind_overdue,
            blocked_by_count=blocked_by_count,
            branch_id=branch_id,
            can_edit=can_edit,
            checklist_done=checklist_done,
            checklist_total=checklist_total,
            code=code,
            completed_at=completed_at,
            created_at=created_at,
            custom_fields=custom_fields,
            description=description,
            due_at=due_at,
            effective_due_at=effective_due_at,
            id=id,
            is_overdue=is_overdue,
            links=links,
            parcel_id=parcel_id,
            parent_task_id=parent_task_id,
            parent_title=parent_title,
            priority=priority,
            progress=progress,
            remind_before_minutes=remind_before_minutes,
            requires_review=requires_review,
            result_note=result_note,
            return_reason=return_reason,
            rev=rev,
            reviewer_id=reviewer_id,
            sort_order=sort_order,
            source_author_id=source_author_id,
            source_channel_accessible=source_channel_accessible,
            source_channel_id=source_channel_id,
            source_channel_name=source_channel_name,
            source_id=source_id,
            source_message_at=source_message_at,
            source_type=source_type,
            start_at=start_at,
            started_at=started_at,
            status=status,
            subtask_assignee_ids=subtask_assignee_ids,
            tags=tags,
            task_group_id=task_group_id,
            task_list_id=task_list_id,
            task_status_color=task_status_color,
            task_status_id=task_status_id,
            task_status_name=task_status_name,
            title=title,
            updated_at=updated_at,
            watcher_ids=watcher_ids,
            workload=workload,
            workload_unit=workload_unit,
        )

        return office_task_dto

