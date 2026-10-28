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
  from ..models.office_chat_message_dto import OfficeChatMessageDto





T = TypeVar("T", bound="OfficeChatMessageAnchorPageDto")



@_attrs_define
class OfficeChatMessageAnchorPageDto:
    

    anchor_message_id: UUID | Unset = UNSET
    distance_from_latest: int | Unset = UNSET
    items: list[OfficeChatMessageDto] | None | Unset = UNSET
    newer_cursor: None | str | Unset = UNSET
    older_cursor: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_chat_message_dto import OfficeChatMessageDto # noqa: PLC0415
        anchor_message_id: str | Unset = UNSET
        if not isinstance(self.anchor_message_id, Unset):
            anchor_message_id = str(self.anchor_message_id)

        distance_from_latest = self.distance_from_latest

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

        newer_cursor: None | str | Unset
        if isinstance(self.newer_cursor, Unset):
            newer_cursor = UNSET
        else:
            newer_cursor = self.newer_cursor

        older_cursor: None | str | Unset
        if isinstance(self.older_cursor, Unset):
            older_cursor = UNSET
        else:
            older_cursor = self.older_cursor


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if anchor_message_id is not UNSET:
            field_dict["anchorMessageId"] = anchor_message_id
        if distance_from_latest is not UNSET:
            field_dict["distanceFromLatest"] = distance_from_latest
        if items is not UNSET:
            field_dict["items"] = items
        if newer_cursor is not UNSET:
            field_dict["newerCursor"] = newer_cursor
        if older_cursor is not UNSET:
            field_dict["olderCursor"] = older_cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_chat_message_dto import OfficeChatMessageDto # noqa: PLC0415
        d = dict(src_dict)
        _anchor_message_id = d.pop("anchorMessageId", UNSET)
        anchor_message_id: UUID | Unset
        if isinstance(_anchor_message_id,  Unset):
            anchor_message_id = UNSET
        else:
            anchor_message_id = UUID(_anchor_message_id)




        distance_from_latest = d.pop("distanceFromLatest", UNSET)

        def _parse_items(data: object) -> list[OfficeChatMessageDto] | None | Unset:
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
                    items_type_0_item = OfficeChatMessageDto.from_dict(items_type_0_item_data)



                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeChatMessageDto] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))


        def _parse_newer_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        newer_cursor = _parse_newer_cursor(d.pop("newerCursor", UNSET))


        def _parse_older_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        older_cursor = _parse_older_cursor(d.pop("olderCursor", UNSET))


        office_chat_message_anchor_page_dto = cls(
            anchor_message_id=anchor_message_id,
            distance_from_latest=distance_from_latest,
            items=items,
            newer_cursor=newer_cursor,
            older_cursor=older_cursor,
        )

        return office_chat_message_anchor_page_dto

