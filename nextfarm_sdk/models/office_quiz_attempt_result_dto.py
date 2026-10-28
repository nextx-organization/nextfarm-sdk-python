from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_quiz_question_outcome_dto import OfficeQuizQuestionOutcomeDto





T = TypeVar("T", bound="OfficeQuizAttemptResultDto")



@_attrs_define
class OfficeQuizAttemptResultDto:
    

    attempt_no: int | Unset = UNSET
    passed: bool | Unset = UNSET
    questions: list[OfficeQuizQuestionOutcomeDto] | None | Unset = UNSET
    score_percent: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_quiz_question_outcome_dto import OfficeQuizQuestionOutcomeDto # noqa: PLC0415
        attempt_no = self.attempt_no

        passed = self.passed

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

        score_percent = self.score_percent


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if attempt_no is not UNSET:
            field_dict["attemptNo"] = attempt_no
        if passed is not UNSET:
            field_dict["passed"] = passed
        if questions is not UNSET:
            field_dict["questions"] = questions
        if score_percent is not UNSET:
            field_dict["scorePercent"] = score_percent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_quiz_question_outcome_dto import OfficeQuizQuestionOutcomeDto # noqa: PLC0415
        d = dict(src_dict)
        attempt_no = d.pop("attemptNo", UNSET)

        passed = d.pop("passed", UNSET)

        def _parse_questions(data: object) -> list[OfficeQuizQuestionOutcomeDto] | None | Unset:
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
                    questions_type_0_item = OfficeQuizQuestionOutcomeDto.from_dict(questions_type_0_item_data)



                    questions_type_0.append(questions_type_0_item)

                return questions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeQuizQuestionOutcomeDto] | None | Unset, data)

        questions = _parse_questions(d.pop("questions", UNSET))


        score_percent = d.pop("scorePercent", UNSET)

        office_quiz_attempt_result_dto = cls(
            attempt_no=attempt_no,
            passed=passed,
            questions=questions,
            score_percent=score_percent,
        )

        return office_quiz_attempt_result_dto

