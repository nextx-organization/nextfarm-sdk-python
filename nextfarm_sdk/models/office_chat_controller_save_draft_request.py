from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeChatControllerSaveDraftRequest")



@_attrs_define
class OfficeChatControllerSaveDraftRequest:
    

    content: None | str | Unset = UNSET
    quoted_message_id: None | Unset | UUID = UNSET





    def to_dict(self) -> dict[str, Any]:
        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        quoted_message_id: None | str | Unset
        if isinstance(self.quoted_message_id, Unset):
            quoted_message_id = UNSET
        elif isinstance(self.quoted_message_id, UUID):
            quoted_message_id = str(self.quoted_message_id)
        else:
            quoted_message_id = self.quoted_message_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content is not UNSET:
            field_dict["content"] = content
        if quoted_message_id is not UNSET:
            field_dict["quotedMessageId"] = quoted_message_id

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


        def _parse_quoted_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                quoted_message_id_type_0 = UUID(data)



                return quoted_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        quoted_message_id = _parse_quoted_message_id(d.pop("quotedMessageId", UNSET))


        office_chat_controller_save_draft_request = cls(
            content=content,
            quoted_message_id=quoted_message_id,
        )

        return office_chat_controller_save_draft_request

