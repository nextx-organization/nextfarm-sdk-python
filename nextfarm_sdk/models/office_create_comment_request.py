from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeCreateCommentRequest")



@_attrs_define
class OfficeCreateCommentRequest:
    

    anchor_id: None | str | Unset = UNSET
    anchor_quote: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    entity_id: UUID | Unset = UNSET
    entity_type: None | str | Unset = UNSET
    mentioned_user_ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        anchor_id: None | str | Unset
        if isinstance(self.anchor_id, Unset):
            anchor_id = UNSET
        else:
            anchor_id = self.anchor_id

        anchor_quote: None | str | Unset
        if isinstance(self.anchor_quote, Unset):
            anchor_quote = UNSET
        else:
            anchor_quote = self.anchor_quote

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        entity_id: str | Unset = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        entity_type: None | str | Unset
        if isinstance(self.entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = self.entity_type

        mentioned_user_ids: list[str] | None | Unset
        if isinstance(self.mentioned_user_ids, Unset):
            mentioned_user_ids = UNSET
        elif isinstance(self.mentioned_user_ids, list):
            mentioned_user_ids = []
            for mentioned_user_ids_type_0_item_data in self.mentioned_user_ids:
                mentioned_user_ids_type_0_item = str(mentioned_user_ids_type_0_item_data)
                mentioned_user_ids.append(mentioned_user_ids_type_0_item)


        else:
            mentioned_user_ids = self.mentioned_user_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if anchor_id is not UNSET:
            field_dict["anchorId"] = anchor_id
        if anchor_quote is not UNSET:
            field_dict["anchorQuote"] = anchor_quote
        if content is not UNSET:
            field_dict["content"] = content
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if mentioned_user_ids is not UNSET:
            field_dict["mentionedUserIds"] = mentioned_user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_anchor_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        anchor_id = _parse_anchor_id(d.pop("anchorId", UNSET))


        def _parse_anchor_quote(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        anchor_quote = _parse_anchor_quote(d.pop("anchorQuote", UNSET))


        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


        _entity_id = d.pop("entityId", UNSET)
        entity_id: UUID | Unset
        if isinstance(_entity_id,  Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)




        def _parse_entity_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_type = _parse_entity_type(d.pop("entityType", UNSET))


        def _parse_mentioned_user_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mentioned_user_ids_type_0 = []
                _mentioned_user_ids_type_0 = data
                for mentioned_user_ids_type_0_item_data in (_mentioned_user_ids_type_0):
                    mentioned_user_ids_type_0_item = UUID(mentioned_user_ids_type_0_item_data)



                    mentioned_user_ids_type_0.append(mentioned_user_ids_type_0_item)

                return mentioned_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        mentioned_user_ids = _parse_mentioned_user_ids(d.pop("mentionedUserIds", UNSET))


        office_create_comment_request = cls(
            anchor_id=anchor_id,
            anchor_quote=anchor_quote,
            content=content,
            entity_id=entity_id,
            entity_type=entity_type,
            mentioned_user_ids=mentioned_user_ids,
        )

        return office_create_comment_request

