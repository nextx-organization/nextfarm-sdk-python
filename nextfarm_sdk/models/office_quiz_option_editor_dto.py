from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeQuizOptionEditorDto")



@_attrs_define
class OfficeQuizOptionEditorDto:
    

    id: UUID | Unset = UNSET
    is_correct: bool | Unset = UNSET
    sort_order: int | Unset = UNSET
    text: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_correct = self.is_correct

        sort_order = self.sort_order

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if is_correct is not UNSET:
            field_dict["isCorrect"] = is_correct
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_correct = d.pop("isCorrect", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))


        office_quiz_option_editor_dto = cls(
            id=id,
            is_correct=is_correct,
            sort_order=sort_order,
            text=text,
        )

        return office_quiz_option_editor_dto

