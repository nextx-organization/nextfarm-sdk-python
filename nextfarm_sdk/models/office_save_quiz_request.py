from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_quiz_question_input import OfficeQuizQuestionInput





T = TypeVar("T", bound="OfficeSaveQuizRequest")



@_attrs_define
class OfficeSaveQuizRequest:
    

    questions: list[OfficeQuizQuestionInput] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_quiz_question_input import OfficeQuizQuestionInput # noqa: PLC0415
        questions: list[dict[str, Any]] | None | Unset
        if isinstance(self.questions, Unset):
            questions = UNSET
        elif isinstance(self.questions, list):
            questions = []
            for questions_type_0_item_data in self.questions:
                questions_type_0_item = questions_type_0_item_data.to_dict()
                questions.append(questions_type_0_item)


        else:
            questions = self.questions


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if questions is not UNSET:
            field_dict["questions"] = questions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_quiz_question_input import OfficeQuizQuestionInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_questions(data: object) -> list[OfficeQuizQuestionInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                questions_type_0 = []
                _questions_type_0 = data
                for questions_type_0_item_data in (_questions_type_0):
                    questions_type_0_item = OfficeQuizQuestionInput.from_dict(questions_type_0_item_data)



                    questions_type_0.append(questions_type_0_item)

                return questions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeQuizQuestionInput] | None | Unset, data)

        questions = _parse_questions(d.pop("questions", UNSET))


        office_save_quiz_request = cls(
            questions=questions,
        )

        return office_save_quiz_request

