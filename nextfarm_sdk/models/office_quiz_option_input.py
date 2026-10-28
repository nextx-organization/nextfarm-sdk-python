from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OfficeQuizOptionInput")



@_attrs_define
class OfficeQuizOptionInput:
    

    is_correct: bool | Unset = UNSET
    text: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        is_correct = self.is_correct

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if is_correct is not UNSET:
            field_dict["isCorrect"] = is_correct
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_correct = d.pop("isCorrect", UNSET)

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))


        office_quiz_option_input = cls(
            is_correct=is_correct,
            text=text,
        )

        return office_quiz_option_input

