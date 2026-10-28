from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="OfficeSurveyAnswerInput")



@_attrs_define
class OfficeSurveyAnswerInput:
    

    question_id: UUID | Unset = UNSET
    rating: int | None | Unset = UNSET
    selected_options: list[str] | None | Unset = UNSET
    text: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        question_id: str | Unset = UNSET
        if not isinstance(self.question_id, Unset):
            question_id = str(self.question_id)

        rating: int | None | Unset
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        selected_options: list[str] | None | Unset
        if isinstance(self.selected_options, Unset):
            selected_options = UNSET
        elif isinstance(self.selected_options, list):
            selected_options = self.selected_options


        else:
            selected_options = self.selected_options

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if question_id is not UNSET:
            field_dict["questionId"] = question_id
        if rating is not UNSET:
            field_dict["rating"] = rating
        if selected_options is not UNSET:
            field_dict["selectedOptions"] = selected_options
        if text is not UNSET:
            field_dict["text"] = text

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




        def _parse_rating(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rating = _parse_rating(d.pop("rating", UNSET))


        def _parse_selected_options(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                selected_options_type_0 = cast(list[str], data)

                return selected_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        selected_options = _parse_selected_options(d.pop("selectedOptions", UNSET))


        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))


        office_survey_answer_input = cls(
            question_id=question_id,
            rating=rating,
            selected_options=selected_options,
            text=text,
        )

        return office_survey_answer_input

