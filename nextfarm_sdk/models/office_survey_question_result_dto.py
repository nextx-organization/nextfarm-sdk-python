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
  from ..models.office_survey_option_tally_dto import OfficeSurveyOptionTallyDto





T = TypeVar("T", bound="OfficeSurveyQuestionResultDto")



@_attrs_define
class OfficeSurveyQuestionResultDto:
    

    answer_count: int | Unset = UNSET
    is_required: bool | Unset = UNSET
    options: list[OfficeSurveyOptionTallyDto] | None | Unset = UNSET
    question_id: UUID | Unset = UNSET
    rating_average: float | None | Unset = UNSET
    text: None | str | Unset = UNSET
    text_answers: list[str] | None | Unset = UNSET
    text_answers_truncated: bool | Unset = UNSET
    type_: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_survey_option_tally_dto import OfficeSurveyOptionTallyDto # noqa: PLC0415
        answer_count = self.answer_count

        is_required = self.is_required

        options: list[dict[str, Any]] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = []
            for options_type_0_item_data in self.options:
                options_type_0_item = options_type_0_item_data.to_dict()
                options.append(options_type_0_item)


        else:
            options = self.options

        question_id: str | Unset = UNSET
        if not isinstance(self.question_id, Unset):
            question_id = str(self.question_id)

        rating_average: float | None | Unset
        if isinstance(self.rating_average, Unset):
            rating_average = UNSET
        else:
            rating_average = self.rating_average

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        text_answers: list[str] | None | Unset
        if isinstance(self.text_answers, Unset):
            text_answers = UNSET
        elif isinstance(self.text_answers, list):
            text_answers = self.text_answers


        else:
            text_answers = self.text_answers

        text_answers_truncated = self.text_answers_truncated

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if answer_count is not UNSET:
            field_dict["answerCount"] = answer_count
        if is_required is not UNSET:
            field_dict["isRequired"] = is_required
        if options is not UNSET:
            field_dict["options"] = options
        if question_id is not UNSET:
            field_dict["questionId"] = question_id
        if rating_average is not UNSET:
            field_dict["ratingAverage"] = rating_average
        if text is not UNSET:
            field_dict["text"] = text
        if text_answers is not UNSET:
            field_dict["textAnswers"] = text_answers
        if text_answers_truncated is not UNSET:
            field_dict["textAnswersTruncated"] = text_answers_truncated
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_survey_option_tally_dto import OfficeSurveyOptionTallyDto # noqa: PLC0415
        d = dict(src_dict)
        answer_count = d.pop("answerCount", UNSET)

        is_required = d.pop("isRequired", UNSET)

        def _parse_options(data: object) -> list[OfficeSurveyOptionTallyDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = []
                _options_type_0 = data
                for options_type_0_item_data in (_options_type_0):
                    options_type_0_item = OfficeSurveyOptionTallyDto.from_dict(options_type_0_item_data)



                    options_type_0.append(options_type_0_item)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeSurveyOptionTallyDto] | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))


        _question_id = d.pop("questionId", UNSET)
        question_id: UUID | Unset
        if isinstance(_question_id,  Unset):
            question_id = UNSET
        else:
            question_id = UUID(_question_id)




        def _parse_rating_average(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rating_average = _parse_rating_average(d.pop("ratingAverage", UNSET))


        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))


        def _parse_text_answers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                text_answers_type_0 = cast(list[str], data)

                return text_answers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        text_answers = _parse_text_answers(d.pop("textAnswers", UNSET))


        text_answers_truncated = d.pop("textAnswersTruncated", UNSET)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        office_survey_question_result_dto = cls(
            answer_count=answer_count,
            is_required=is_required,
            options=options,
            question_id=question_id,
            rating_average=rating_average,
            text=text,
            text_answers=text_answers,
            text_answers_truncated=text_answers_truncated,
            type_=type_,
        )

        return office_survey_question_result_dto

