from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeUpdateCommentRequest")



@_attrs_define
class OfficeUpdateCommentRequest:
    

    content: None | str | Unset = UNSET
    mentioned_user_ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

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
        if content is not UNSET:
            field_dict["content"] = content
        if mentioned_user_ids is not UNSET:
            field_dict["mentionedUserIds"] = mentioned_user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


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


        office_update_comment_request = cls(
            content=content,
            mentioned_user_ids=mentioned_user_ids,
        )

        return office_update_comment_request

