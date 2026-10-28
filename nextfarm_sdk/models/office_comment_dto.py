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






T = TypeVar("T", bound="OfficeCommentDto")



@_attrs_define
class OfficeCommentDto:
    

    anchor_id: None | str | Unset = UNSET
    anchor_quote: None | str | Unset = UNSET
    author_id: UUID | Unset = UNSET
    content: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    edited: bool | Unset = UNSET
    entity_id: UUID | Unset = UNSET
    entity_type: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    mentioned_user_ids: list[UUID] | None | Unset = UNSET
    resolved_at: datetime.datetime | None | Unset = UNSET
    resolved_by: None | Unset | UUID = UNSET
    updated_at: datetime.datetime | Unset = UNSET





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

        author_id: str | Unset = UNSET
        if not isinstance(self.author_id, Unset):
            author_id = str(self.author_id)

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        edited = self.edited

        entity_id: str | Unset = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        entity_type: None | str | Unset
        if isinstance(self.entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = self.entity_type

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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

        resolved_at: None | str | Unset
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        elif isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        resolved_by: None | str | Unset
        if isinstance(self.resolved_by, Unset):
            resolved_by = UNSET
        elif isinstance(self.resolved_by, UUID):
            resolved_by = str(self.resolved_by)
        else:
            resolved_by = self.resolved_by

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if anchor_id is not UNSET:
            field_dict["anchorId"] = anchor_id
        if anchor_quote is not UNSET:
            field_dict["anchorQuote"] = anchor_quote
        if author_id is not UNSET:
            field_dict["authorId"] = author_id
        if content is not UNSET:
            field_dict["content"] = content
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if edited is not UNSET:
            field_dict["edited"] = edited
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if id is not UNSET:
            field_dict["id"] = id
        if mentioned_user_ids is not UNSET:
            field_dict["mentionedUserIds"] = mentioned_user_ids
        if resolved_at is not UNSET:
            field_dict["resolvedAt"] = resolved_at
        if resolved_by is not UNSET:
            field_dict["resolvedBy"] = resolved_by
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

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


        _author_id = d.pop("authorId", UNSET)
        author_id: UUID | Unset
        if isinstance(_author_id,  Unset):
            author_id = UNSET
        else:
            author_id = UUID(_author_id)




        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        edited = d.pop("edited", UNSET)

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


        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




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


        def _parse_resolved_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_at_type_0 = datetime.datetime.fromisoformat(data)



                return resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        resolved_at = _parse_resolved_at(d.pop("resolvedAt", UNSET))


        def _parse_resolved_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_by_type_0 = UUID(data)



                return resolved_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        resolved_by = _parse_resolved_by(d.pop("resolvedBy", UNSET))


        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        office_comment_dto = cls(
            anchor_id=anchor_id,
            anchor_quote=anchor_quote,
            author_id=author_id,
            content=content,
            created_at=created_at,
            edited=edited,
            entity_id=entity_id,
            entity_type=entity_type,
            id=id,
            mentioned_user_ids=mentioned_user_ids,
            resolved_at=resolved_at,
            resolved_by=resolved_by,
            updated_at=updated_at,
        )

        return office_comment_dto

