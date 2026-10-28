from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeQuizAnswerInput")



@_attrs_define
class OfficeQuizAnswerInput:
    

    question_id: UUID | Unset = UNSET
    selected_option_ids: list[UUID] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        question_id: str | Unset = UNSET
        if not isinstance(self.question_id, Unset):
            question_id = str(self.question_id)

        selected_option_ids: list[str] | None | Unset
        if isinstance(self.selected_option_ids, Unset):
            selected_option_ids = UNSET
        elif isinstance(self.selected_option_ids, list):
            selected_option_ids = []
            for selected_option_ids_type_0_item_data in self.selected_option_ids:
                selected_option_ids_type_0_item = str(selected_option_ids_type_0_item_data)
                selected_option_ids.append(selected_option_ids_type_0_item)


        else:
            selected_option_ids = self.selected_option_ids


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if question_id is not UNSET:
            field_dict["questionId"] = question_id
        if selected_option_ids is not UNSET:
            field_dict["selectedOptionIds"] = selected_option_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _question_id = d.pop("questionId", UNSET)
        question_id: UUID | Unset
        if isinstance(_question_id,  Unset):
            question_id = UNSET
        else:
            question_id = UUID(_question_id)




        def _parse_selected_option_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                selected_option_ids_type_0 = []
                _selected_option_ids_type_0 = data
                for selected_option_ids_type_0_item_data in (_selected_option_ids_type_0):
                    selected_option_ids_type_0_item = UUID(selected_option_ids_type_0_item_data)



                    selected_option_ids_type_0.append(selected_option_ids_type_0_item)

                return selected_option_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        selected_option_ids = _parse_selected_option_ids(d.pop("selectedOptionIds", UNSET))


        office_quiz_answer_input = cls(
            question_id=question_id,
            selected_option_ids=selected_option_ids,
        )

        return office_quiz_answer_input

