from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeMessageTranslationDto")



@_attrs_define
class OfficeMessageTranslationDto:
    

    message_id: UUID | Unset = UNSET
    target_language: None | str | Unset = UNSET
    text: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        message_id: str | Unset = UNSET
        if not isinstance(self.message_id, Unset):
            message_id = str(self.message_id)

        target_language: None | str | Unset
        if isinstance(self.target_language, Unset):
            target_language = UNSET
        else:
            target_language = self.target_language

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if target_language is not UNSET:
            field_dict["targetLanguage"] = target_language
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _message_id = d.pop("messageId", UNSET)
        message_id: UUID | Unset
        if isinstance(_message_id,  Unset):
            message_id = UNSET
        else:
            message_id = UUID(_message_id)




        def _parse_target_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_language = _parse_target_language(d.pop("targetLanguage", UNSET))


        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))


        office_message_translation_dto = cls(
            message_id=message_id,
            target_language=target_language,
            text=text,
        )

        return office_message_translation_dto

