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
  from ..models.office_survey_question_result_dto import OfficeSurveyQuestionResultDto





T = TypeVar("T", bound="OfficeSurveyResultsDto")



@_attrs_define
class OfficeSurveyResultsDto:
    

    invited_count: int | None | Unset = UNSET
    is_anonymous: bool | Unset = UNSET
    questions: list[OfficeSurveyQuestionResultDto] | None | Unset = UNSET
    response_count: int | Unset = UNSET
    response_rate: float | None | Unset = UNSET
    status: None | str | Unset = UNSET
    survey_id: UUID | Unset = UNSET
    title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_survey_question_result_dto import OfficeSurveyQuestionResultDto # noqa: PLC0415
        invited_count: int | None | Unset
        if isinstance(self.invited_count, Unset):
            invited_count = UNSET
        else:
            invited_count = self.invited_count

        is_anonymous = self.is_anonymous

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

        response_count = self.response_count

        response_rate: float | None | Unset
        if isinstance(self.response_rate, Unset):
            response_rate = UNSET
        else:
            response_rate = self.response_rate

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        survey_id: str | Unset = UNSET
        if not isinstance(self.survey_id, Unset):
            survey_id = str(self.survey_id)

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if invited_count is not UNSET:
            field_dict["invitedCount"] = invited_count
        if is_anonymous is not UNSET:
            field_dict["isAnonymous"] = is_anonymous
        if questions is not UNSET:
            field_dict["questions"] = questions
        if response_count is not UNSET:
            field_dict["responseCount"] = response_count
        if response_rate is not UNSET:
            field_dict["responseRate"] = response_rate
        if status is not UNSET:
            field_dict["status"] = status
        if survey_id is not UNSET:
            field_dict["surveyId"] = survey_id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_survey_question_result_dto import OfficeSurveyQuestionResultDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_invited_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        invited_count = _parse_invited_count(d.pop("invitedCount", UNSET))


        is_anonymous = d.pop("isAnonymous", UNSET)

        def _parse_questions(data: object) -> list[OfficeSurveyQuestionResultDto] | None | Unset:
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
                    questions_type_0_item = OfficeSurveyQuestionResultDto.from_dict(questions_type_0_item_data)



                    questions_type_0.append(questions_type_0_item)

                return questions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeSurveyQuestionResultDto] | None | Unset, data)

        questions = _parse_questions(d.pop("questions", UNSET))


        response_count = d.pop("responseCount", UNSET)

        def _parse_response_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        response_rate = _parse_response_rate(d.pop("responseRate", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        _survey_id = d.pop("surveyId", UNSET)
        survey_id: UUID | Unset
        if isinstance(_survey_id,  Unset):
            survey_id = UNSET
        else:
            survey_id = UUID(_survey_id)




        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        office_survey_results_dto = cls(
            invited_count=invited_count,
            is_anonymous=is_anonymous,
            questions=questions,
            response_count=response_count,
            response_rate=response_rate,
            status=status,
            survey_id=survey_id,
            title=title,
        )

        return office_survey_results_dto

