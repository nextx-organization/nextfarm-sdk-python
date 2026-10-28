from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.office_survey_question_input import OfficeSurveyQuestionInput





T = TypeVar("T", bound="OfficeUpdateSurveyRequest")



@_attrs_define
class OfficeUpdateSurveyRequest:
    

    audience_group_codes: list[str] | None | Unset = UNSET
    closes_at: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    questions: list[OfficeSurveyQuestionInput] | None | Unset = UNSET
    title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_survey_question_input import OfficeSurveyQuestionInput # noqa: PLC0415
        audience_group_codes: list[str] | None | Unset
        if isinstance(self.audience_group_codes, Unset):
            audience_group_codes = UNSET
        elif isinstance(self.audience_group_codes, list):
            audience_group_codes = self.audience_group_codes


        else:
            audience_group_codes = self.audience_group_codes

        closes_at: None | str | Unset
        if isinstance(self.closes_at, Unset):
            closes_at = UNSET
        elif isinstance(self.closes_at, datetime.datetime):
            closes_at = self.closes_at.isoformat()
        else:
            closes_at = self.closes_at

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if audience_group_codes is not UNSET:
            field_dict["audienceGroupCodes"] = audience_group_codes
        if closes_at is not UNSET:
            field_dict["closesAt"] = closes_at
        if description is not UNSET:
            field_dict["description"] = description
        if questions is not UNSET:
            field_dict["questions"] = questions
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_survey_question_input import OfficeSurveyQuestionInput # noqa: PLC0415
        d = dict(src_dict)
        def _parse_audience_group_codes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                audience_group_codes_type_0 = cast(list[str], data)

                return audience_group_codes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        audience_group_codes = _parse_audience_group_codes(d.pop("audienceGroupCodes", UNSET))


        def _parse_closes_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closes_at_type_0 = datetime.datetime.fromisoformat(data)



                return closes_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closes_at = _parse_closes_at(d.pop("closesAt", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_questions(data: object) -> list[OfficeSurveyQuestionInput] | None | Unset:
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
                    questions_type_0_item = OfficeSurveyQuestionInput.from_dict(questions_type_0_item_data)



                    questions_type_0.append(questions_type_0_item)

                return questions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeSurveyQuestionInput] | None | Unset, data)

        questions = _parse_questions(d.pop("questions", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        office_update_survey_request = cls(
            audience_group_codes=audience_group_codes,
            closes_at=closes_at,
            description=description,
            questions=questions,
            title=title,
        )

        return office_update_survey_request

