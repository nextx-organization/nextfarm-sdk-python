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
  from ..models.office_chat_subtask_input import OfficeChatSubtaskInput





T = TypeVar("T", bound="OfficeChatControllerCreateTaskFromMessageRequest")



@_attrs_define
class OfficeChatControllerCreateTaskFromMessageRequest:
    

    assignee_id: None | Unset | UUID = UNSET
    branch_id: None | Unset | UUID = UNSET
    client_request_id: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    due_at: datetime.datetime | None | Unset = UNSET
    parcel_id: None | Unset | UUID = UNSET
    post_card: bool | Unset = UNSET
    priority: None | str | Unset = UNSET
    start_at: datetime.datetime | None | Unset = UNSET
    subtasks: list[OfficeChatSubtaskInput] | None | Unset = UNSET
    task_group_id: None | Unset | UUID = UNSET
    task_list_id: None | Unset | UUID = UNSET
    title: None | str | Unset = UNSET
    watcher_ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_chat_subtask_input import OfficeChatSubtaskInput # noqa: PLC0415
        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        elif isinstance(self.assignee_id, UUID):
            assignee_id = str(self.assignee_id)
        else:
            assignee_id = self.assignee_id

        branch_id: None | str | Unset
        if isinstance(self.branch_id, Unset):
            branch_id = UNSET
        elif isinstance(self.branch_id, UUID):
            branch_id = str(self.branch_id)
        else:
            branch_id = self.branch_id

        client_request_id: None | str | Unset
        if isinstance(self.client_request_id, Unset):
            client_request_id = UNSET
        else:
            client_request_id = self.client_request_id

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

        parcel_id: None | str | Unset
        if isinstance(self.parcel_id, Unset):
            parcel_id = UNSET
        elif isinstance(self.parcel_id, UUID):
            parcel_id = str(self.parcel_id)
        else:
            parcel_id = self.parcel_id

        post_card = self.post_card

        priority: None | str | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        start_at: None | str | Unset
        if isinstance(self.start_at, Unset):
            start_at = UNSET
        elif isinstance(self.start_at, datetime.datetime):
            start_at = self.start_at.isoformat()
        else:
            start_at = self.start_at

        subtasks: list[dict[str, Any]] | None | Unset
        if isinstance(self.subtasks, Unset):
            subtasks = UNSET
        elif isinstance(self.subtasks, list):
            subtasks = []
            for subtasks_type_0_item_data in self.subtasks:
                subtasks_type_0_item = subtasks_type_0_item_data.to_dict()
                subtasks.append(subtasks_type_0_item)


        else:
            subtasks = self.subtasks

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if branch_id is not UNSET:
            field_dict["branchId"] = branch_id
        if client_request_id is not UNSET:
            field_dict["clientRequestId"] = client_request_id
        if description is not UNSET:
            field_dict["description"] = description
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if parcel_id is not UNSET:
            field_dict["parcelId"] = parcel_id
        if post_card is not UNSET:
            field_dict["postCard"] = post_card
        if priority is not UNSET:
            field_dict["priority"] = priority
        if start_at is not UNSET:
            field_dict["startAt"] = start_at
        if subtasks is not UNSET:
            field_dict["subtasks"] = subtasks
        if task_group_id is not UNSET:
            field_dict["taskGroupId"] = task_group_id
        if task_list_id is not UNSET:
            field_dict["taskListId"] = task_list_id
        if title is not UNSET:
            field_dict["title"] = title
        if watcher_ids is not UNSET:
            field_dict["watcherIds"] = watcher_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_chat_subtask_input import OfficeChatSubtaskInput # noqa: PLC0415
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


        def _parse_client_request_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_request_id = _parse_client_request_id(d.pop("clientRequestId", UNSET))


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


        post_card = d.pop("postCard", UNSET)

        def _parse_priority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))


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


        def _parse_subtasks(data: object) -> list[OfficeChatSubtaskInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subtasks_type_0 = []
                _subtasks_type_0 = data
                for subtasks_type_0_item_data in (_subtasks_type_0):
                    subtasks_type_0_item = OfficeChatSubtaskInput.from_dict(subtasks_type_0_item_data)



                    subtasks_type_0.append(subtasks_type_0_item)

                return subtasks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeChatSubtaskInput] | None | Unset, data)

        subtasks = _parse_subtasks(d.pop("subtasks", UNSET))


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


        office_chat_controller_create_task_from_message_request = cls(
            assignee_id=assignee_id,
            branch_id=branch_id,
            client_request_id=client_request_id,
            description=description,
            due_at=due_at,
            parcel_id=parcel_id,
            post_card=post_card,
            priority=priority,
            start_at=start_at,
            subtasks=subtasks,
            task_group_id=task_group_id,
            task_list_id=task_list_id,
            title=title,
            watcher_ids=watcher_ids,
        )

        return office_chat_controller_create_task_from_message_request

