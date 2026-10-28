from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.office_chat_task_item_input import OfficeChatTaskItemInput





T = TypeVar("T", bound="OfficeChatControllerCreateTasksRequest")



@_attrs_define
class OfficeChatControllerCreateTasksRequest:
    

    client_request_id: None | str | Unset = UNSET
    items: list[OfficeChatTaskItemInput] | None | Unset = UNSET
    mode: None | str | Unset = UNSET
    parent_message_id: None | Unset | UUID = UNSET
    parent_title: None | str | Unset = UNSET
    post_card: bool | Unset = UNSET
    task_group_id: None | Unset | UUID = UNSET
    task_list_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_chat_task_item_input import OfficeChatTaskItemInput # noqa: PLC0415
        client_request_id: None | str | Unset
        if isinstance(self.client_request_id, Unset):
            client_request_id = UNSET
        else:
            client_request_id = self.client_request_id

        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)


        else:
            items = self.items

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        else:
            mode = self.mode

        parent_message_id: None | str | Unset
        if isinstance(self.parent_message_id, Unset):
            parent_message_id = UNSET
        elif isinstance(self.parent_message_id, UUID):
            parent_message_id = str(self.parent_message_id)
        else:
            parent_message_id = self.parent_message_id

        parent_title: None | str | Unset
        if isinstance(self.parent_title, Unset):
            parent_title = UNSET
        else:
            parent_title = self.parent_title

        post_card = self.post_card

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if client_request_id is not UNSET:
            field_dict["clientRequestId"] = client_request_id
        if items is not UNSET:
            field_dict["items"] = items
        if mode is not UNSET:
            field_dict["mode"] = mode
        if parent_message_id is not UNSET:
            field_dict["parentMessageId"] = parent_message_id
        if parent_title is not UNSET:
            field_dict["parentTitle"] = parent_title
        if post_card is not UNSET:
            field_dict["postCard"] = post_card
        if task_group_id is not UNSET:
            field_dict["taskGroupId"] = task_group_id
        if task_list_id is not UNSET:
            field_dict["taskListId"] = task_list_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_chat_task_item_input import OfficeChatTaskItemInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_client_request_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_request_id = _parse_client_request_id(d.pop("clientRequestId", UNSET))


        def _parse_items(data: object) -> list[OfficeChatTaskItemInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in (_items_type_0):
                    items_type_0_item = OfficeChatTaskItemInput.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeChatTaskItemInput] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        def _parse_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))


        def _parse_parent_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_message_id_type_0 = UUID(data)



                return parent_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_message_id = _parse_parent_message_id(d.pop("parentMessageId", UNSET))


        def _parse_parent_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_title = _parse_parent_title(d.pop("parentTitle", UNSET))


        post_card = d.pop("postCard", UNSET)

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


        office_chat_controller_create_tasks_request = cls(
            client_request_id=client_request_id,
            items=items,
            mode=mode,
            parent_message_id=parent_message_id,
            parent_title=parent_title,
            post_card=post_card,
            task_group_id=task_group_id,
            task_list_id=task_list_id,
        )

        return office_chat_controller_create_tasks_request

