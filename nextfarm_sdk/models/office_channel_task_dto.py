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






T = TypeVar("T", bound="OfficeChannelTaskDto")



@_attrs_define
class OfficeChannelTaskDto:
    

    assignee_id: None | Unset | UUID = UNSET
    assigner_id: UUID | Unset = UNSET
    card_id: UUID | Unset = UNSET
    card_message_id: UUID | Unset = UNSET
    due_at: datetime.datetime | None | Unset = UNSET
    is_overdue: bool | Unset = UNSET
    message_id: UUID | Unset = UNSET
    origin: None | str | Unset = UNSET
    priority: None | str | Unset = UNSET
    reviewer_id: None | Unset | UUID = UNSET
    shared_at: datetime.datetime | Unset = UNSET
    shared_by: UUID | Unset = UNSET
    source_at: datetime.datetime | None | Unset = UNSET
    source_author_id: None | Unset | UUID = UNSET
    source_message_id: None | Unset | UUID = UNSET
    status: None | str | Unset = UNSET
    subtask_done: int | Unset = UNSET
    subtask_total: int | Unset = UNSET
    task_id: UUID | Unset = UNSET
    title: None | str | Unset = UNSET





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

        card_id: str | Unset = UNSET
        if not isinstance(self.card_id, Unset):
            card_id = str(self.card_id)

        card_message_id: str | Unset = UNSET
        if not isinstance(self.card_message_id, Unset):
            card_message_id = str(self.card_message_id)

        due_at: None | str | Unset
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        is_overdue = self.is_overdue

        message_id: str | Unset = UNSET
        if not isinstance(self.message_id, Unset):
            message_id = str(self.message_id)

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        else:
            origin = self.origin

        priority: None | str | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        reviewer_id: None | str | Unset
        if isinstance(self.reviewer_id, Unset):
            reviewer_id = UNSET
        elif isinstance(self.reviewer_id, UUID):
            reviewer_id = str(self.reviewer_id)
        else:
            reviewer_id = self.reviewer_id

        shared_at: str | Unset = UNSET
        if not isinstance(self.shared_at, Unset):
            shared_at = self.shared_at.isoformat()

        shared_by: str | Unset = UNSET
        if not isinstance(self.shared_by, Unset):
            shared_by = str(self.shared_by)

        source_at: None | str | Unset
        if isinstance(self.source_at, Unset):
            source_at = UNSET
        elif isinstance(self.source_at, datetime.datetime):
            source_at = self.source_at.isoformat()
        else:
            source_at = self.source_at

        source_author_id: None | str | Unset
        if isinstance(self.source_author_id, Unset):
            source_author_id = UNSET
        elif isinstance(self.source_author_id, UUID):
            source_author_id = str(self.source_author_id)
        else:
            source_author_id = self.source_author_id

        source_message_id: None | str | Unset
        if isinstance(self.source_message_id, Unset):
            source_message_id = UNSET
        elif isinstance(self.source_message_id, UUID):
            source_message_id = str(self.source_message_id)
        else:
            source_message_id = self.source_message_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        subtask_done = self.subtask_done

        subtask_total = self.subtask_total

        task_id: str | Unset = UNSET
        if not isinstance(self.task_id, Unset):
            task_id = str(self.task_id)

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if assigner_id is not UNSET:
            field_dict["assignerId"] = assigner_id
        if card_id is not UNSET:
            field_dict["cardId"] = card_id
        if card_message_id is not UNSET:
            field_dict["cardMessageId"] = card_message_id
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if is_overdue is not UNSET:
            field_dict["isOverdue"] = is_overdue
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if origin is not UNSET:
            field_dict["origin"] = origin
        if priority is not UNSET:
            field_dict["priority"] = priority
        if reviewer_id is not UNSET:
            field_dict["reviewerId"] = reviewer_id
        if shared_at is not UNSET:
            field_dict["sharedAt"] = shared_at
        if shared_by is not UNSET:
            field_dict["sharedBy"] = shared_by
        if source_at is not UNSET:
            field_dict["sourceAt"] = source_at
        if source_author_id is not UNSET:
            field_dict["sourceAuthorId"] = source_author_id
        if source_message_id is not UNSET:
            field_dict["sourceMessageId"] = source_message_id
        if status is not UNSET:
            field_dict["status"] = status
        if subtask_done is not UNSET:
            field_dict["subtaskDone"] = subtask_done
        if subtask_total is not UNSET:
            field_dict["subtaskTotal"] = subtask_total
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if title is not UNSET:
            field_dict["title"] = title

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




        _card_id = d.pop("cardId", UNSET)
        card_id: UUID | Unset
        if isinstance(_card_id,  Unset):
            card_id = UNSET
        else:
            card_id = UUID(_card_id)




        _card_message_id = d.pop("cardMessageId", UNSET)
        card_message_id: UUID | Unset
        if isinstance(_card_message_id,  Unset):
            card_message_id = UNSET
        else:
            card_message_id = UUID(_card_message_id)




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


        is_overdue = d.pop("isOverdue", UNSET)

        _message_id = d.pop("messageId", UNSET)
        message_id: UUID | Unset
        if isinstance(_message_id,  Unset):
            message_id = UNSET
        else:
            message_id = UUID(_message_id)




        def _parse_origin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin = _parse_origin(d.pop("origin", UNSET))


        def _parse_priority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))


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


        _shared_at = d.pop("sharedAt", UNSET)
        shared_at: datetime.datetime | Unset
        if isinstance(_shared_at,  Unset):
            shared_at = UNSET
        else:
            shared_at = datetime.datetime.fromisoformat(_shared_at)




        _shared_by = d.pop("sharedBy", UNSET)
        shared_by: UUID | Unset
        if isinstance(_shared_by,  Unset):
            shared_by = UNSET
        else:
            shared_by = UUID(_shared_by)




        def _parse_source_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_at_type_0 = datetime.datetime.fromisoformat(data)



                return source_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        source_at = _parse_source_at(d.pop("sourceAt", UNSET))


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


        def _parse_source_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_message_id_type_0 = UUID(data)



                return source_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_message_id = _parse_source_message_id(d.pop("sourceMessageId", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        subtask_done = d.pop("subtaskDone", UNSET)

        subtask_total = d.pop("subtaskTotal", UNSET)

        _task_id = d.pop("taskId", UNSET)
        task_id: UUID | Unset
        if isinstance(_task_id,  Unset):
            task_id = UNSET
        else:
            task_id = UUID(_task_id)




        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        office_channel_task_dto = cls(
            assignee_id=assignee_id,
            assigner_id=assigner_id,
            card_id=card_id,
            card_message_id=card_message_id,
            due_at=due_at,
            is_overdue=is_overdue,
            message_id=message_id,
            origin=origin,
            priority=priority,
            reviewer_id=reviewer_id,
            shared_at=shared_at,
            shared_by=shared_by,
            source_at=source_at,
            source_author_id=source_author_id,
            source_message_id=source_message_id,
            status=status,
            subtask_done=subtask_done,
            subtask_total=subtask_total,
            task_id=task_id,
            title=title,
        )

        return office_channel_task_dto

