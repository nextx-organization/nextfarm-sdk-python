from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_survey_dto import OfficeSurveyDto
  from ..models.office_survey_question_dto import OfficeSurveyQuestionDto





T = TypeVar("T", bound="OfficeSurveyDetailDto")



@_attrs_define
class OfficeSurveyDetailDto:
    

    questions: list[OfficeSurveyQuestionDto] | None | Unset = UNSET
    survey: OfficeSurveyDto | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_survey_dto import OfficeSurveyDto # noqa: PLC0415
        from ..models.office_survey_question_dto import OfficeSurveyQuestionDto # noqa: PLC0415
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

        survey: dict[str, Any] | Unset = UNSET
        if not isinstance(self.survey, Unset):
            survey = self.survey.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if questions is not UNSET:
            field_dict["questions"] = questions
        if survey is not UNSET:
            field_dict["survey"] = survey

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_survey_dto import OfficeSurveyDto # noqa: PLC0415
        from ..models.office_survey_question_dto import OfficeSurveyQuestionDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_questions(data: object) -> list[OfficeSurveyQuestionDto] | None | Unset:
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
                    questions_type_0_item = OfficeSurveyQuestionDto.from_dict(questions_type_0_item_data)



                    questions_type_0.append(questions_type_0_item)

                return questions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeSurveyQuestionDto] | None | Unset, data)

        questions = _parse_questions(d.pop("questions", UNSET))


        _survey = d.pop("survey", UNSET)
        survey: OfficeSurveyDto | Unset
        if isinstance(_survey,  Unset):
            survey = UNSET
        else:
            survey = OfficeSurveyDto.from_dict(_survey)




        office_survey_detail_dto = cls(
            questions=questions,
            survey=survey,
        )

        return office_survey_detail_dto

