from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatControllerReactionRequest")



@_attrs_define
class OfficeChatControllerReactionRequest:
    

    emoji: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        emoji: None | str | Unset
        if isinstance(self.emoji, Unset):
            emoji = UNSET
        else:
            emoji = self.emoji


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if emoji is not UNSET:
            field_dict["emoji"] = emoji

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_emoji(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        emoji = _parse_emoji(d.pop("emoji", UNSET))


        office_chat_controller_reaction_request = cls(
            emoji=emoji,
        )

        return office_chat_controller_reaction_request

