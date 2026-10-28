from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatControllerSaveQuickMessageRequest")



@_attrs_define
class OfficeChatControllerSaveQuickMessageRequest:
    

    content: None | str | Unset = UNSET
    shortcut: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        shortcut: None | str | Unset
        if isinstance(self.shortcut, Unset):
            shortcut = UNSET
        else:
            shortcut = self.shortcut


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if content is not UNSET:
            field_dict["content"] = content
        if shortcut is not UNSET:
            field_dict["shortcut"] = shortcut

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


        def _parse_shortcut(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shortcut = _parse_shortcut(d.pop("shortcut", UNSET))


        office_chat_controller_save_quick_message_request = cls(
            content=content,
            shortcut=shortcut,
        )

        return office_chat_controller_save_quick_message_request

