from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.office_quiz_question_dto import OfficeQuizQuestionDto





T = TypeVar("T", bound="OfficeCourseQuizDto")



@_attrs_define
class OfficeCourseQuizDto:
    

    allow_retake: bool | Unset = UNSET
    attempt_count: int | Unset = UNSET
    can_attempt: bool | Unset = UNSET
    course_id: UUID | Unset = UNSET
    passing_score: int | Unset = UNSET
    questions: list[OfficeQuizQuestionDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_quiz_question_dto import OfficeQuizQuestionDto # noqa: PLC0415
        allow_retake = self.allow_retake

        attempt_count = self.attempt_count

        can_attempt = self.can_attempt

        course_id: str | Unset = UNSET
        if not isinstance(self.course_id, Unset):
            course_id = str(self.course_id)

        passing_score = self.passing_score

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
        if allow_retake is not UNSET:
            field_dict["allowRetake"] = allow_retake
        if attempt_count is not UNSET:
            field_dict["attemptCount"] = attempt_count
        if can_attempt is not UNSET:
            field_dict["canAttempt"] = can_attempt
        if course_id is not UNSET:
            field_dict["courseId"] = course_id
        if passing_score is not UNSET:
            field_dict["passingScore"] = passing_score
        if questions is not UNSET:
            field_dict["questions"] = questions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_quiz_question_dto import OfficeQuizQuestionDto # noqa: PLC0415
        d = dict(src_dict)
        allow_retake = d.pop("allowRetake", UNSET)

        attempt_count = d.pop("attemptCount", UNSET)

        can_attempt = d.pop("canAttempt", UNSET)

        _course_id = d.pop("courseId", UNSET)
        course_id: UUID | Unset
        if isinstance(_course_id,  Unset):
            course_id = UNSET
        else:
            course_id = UUID(_course_id)




        passing_score = d.pop("passingScore", UNSET)

        def _parse_questions(data: object) -> list[OfficeQuizQuestionDto] | None | Unset:
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
                    questions_type_0_item = OfficeQuizQuestionDto.from_dict(questions_type_0_item_data)



                    questions_type_0.append(questions_type_0_item)

                return questions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeQuizQuestionDto] | None | Unset, data)

        questions = _parse_questions(d.pop("questions", UNSET))


        office_course_quiz_dto = cls(
            allow_retake=allow_retake,
            attempt_count=attempt_count,
            can_attempt=can_attempt,
            course_id=course_id,
            passing_score=passing_score,
            questions=questions,
        )

        return office_course_quiz_dto

