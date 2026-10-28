from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_quiz_answer_input import OfficeQuizAnswerInput





T = TypeVar("T", bound="OfficeSubmitQuizRequest")



@_attrs_define
class OfficeSubmitQuizRequest:
    

    answers: list[OfficeQuizAnswerInput] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_quiz_answer_input import OfficeQuizAnswerInput # noqa: PLC0415
        answers: list[dict[str, Any]] | None | Unset
        if isinstance(self.answers, Unset):
            answers = UNSET
        elif isinstance(self.answers, list):
            answers = []
            for answers_type_0_item_data in self.answers:
                answers_type_0_item = answers_type_0_item_data.to_dict()
                answers.append(answers_type_0_item)


        else:
            answers = self.answers


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if answers is not UNSET:
            field_dict["answers"] = answers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_quiz_answer_input import OfficeQuizAnswerInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_answers(data: object) -> list[OfficeQuizAnswerInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                answers_type_0 = []
                _answers_type_0 = data
                for answers_type_0_item_data in (_answers_type_0):
                    answers_type_0_item = OfficeQuizAnswerInput.from_dict(answers_type_0_item_data)



                    answers_type_0.append(answers_type_0_item)

                return answers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeQuizAnswerInput] | None | Unset, data)

        answers = _parse_answers(d.pop("answers", UNSET))


        office_submit_quiz_request = cls(
            answers=answers,
        )

        return office_submit_quiz_request

