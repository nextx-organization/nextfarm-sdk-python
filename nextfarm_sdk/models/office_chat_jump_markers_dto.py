from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeChatJumpMarkersDto")



@_attrs_define
class OfficeChatJumpMarkersDto:
    

    first_unread_message_id: None | Unset | UUID = UNSET
    mention_message_ids: list[UUID] | None | Unset = UNSET
    unread_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        first_unread_message_id: None | str | Unset
        if isinstance(self.first_unread_message_id, Unset):
            first_unread_message_id = UNSET
        elif isinstance(self.first_unread_message_id, UUID):
            first_unread_message_id = str(self.first_unread_message_id)
        else:
            first_unread_message_id = self.first_unread_message_id

        mention_message_ids: list[str] | None | Unset
        if isinstance(self.mention_message_ids, Unset):
            mention_message_ids = UNSET
        elif isinstance(self.mention_message_ids, list):
            mention_message_ids = []
            for mention_message_ids_type_0_item_data in self.mention_message_ids:
                mention_message_ids_type_0_item = str(mention_message_ids_type_0_item_data)
                mention_message_ids.append(mention_message_ids_type_0_item)


        else:
            mention_message_ids = self.mention_message_ids

        unread_count = self.unread_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if first_unread_message_id is not UNSET:
            field_dict["firstUnreadMessageId"] = first_unread_message_id
        if mention_message_ids is not UNSET:
            field_dict["mentionMessageIds"] = mention_message_ids
        if unread_count is not UNSET:
            field_dict["unreadCount"] = unread_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_first_unread_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_unread_message_id_type_0 = UUID(data)



                return first_unread_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        first_unread_message_id = _parse_first_unread_message_id(d.pop("firstUnreadMessageId", UNSET))


        def _parse_mention_message_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mention_message_ids_type_0 = []
                _mention_message_ids_type_0 = data
                for mention_message_ids_type_0_item_data in (_mention_message_ids_type_0):
                    mention_message_ids_type_0_item = UUID(mention_message_ids_type_0_item_data)



                    mention_message_ids_type_0.append(mention_message_ids_type_0_item)

                return mention_message_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        mention_message_ids = _parse_mention_message_ids(d.pop("mentionMessageIds", UNSET))


        unread_count = d.pop("unreadCount", UNSET)

        office_chat_jump_markers_dto = cls(
            first_unread_message_id=first_unread_message_id,
            mention_message_ids=mention_message_ids,
            unread_count=unread_count,
        )

        return office_chat_jump_markers_dto

