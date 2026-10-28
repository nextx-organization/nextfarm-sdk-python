from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeChatControllerTranslateRequest")



@_attrs_define
class OfficeChatControllerTranslateRequest:
    

    target_language: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        target_language: None | str | Unset
        if isinstance(self.target_language, Unset):
            target_language = UNSET
        else:
            target_language = self.target_language


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if target_language is not UNSET:
            field_dict["targetLanguage"] = target_language

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_target_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_language = _parse_target_language(d.pop("targetLanguage", UNSET))


        office_chat_controller_translate_request = cls(
            target_language=target_language,
        )

        return office_chat_controller_translate_request

