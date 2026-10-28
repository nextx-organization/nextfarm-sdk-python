from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_question_detail_dto_status import check_office_question_detail_dto_status
from ..models.office_question_detail_dto_status import OfficeQuestionDetailDtoStatus
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.office_answer_dto import OfficeAnswerDto





T = TypeVar("T", bound="OfficeQuestionDetailDto")



@_attrs_define
class OfficeQuestionDetailDto:
    

    accepted_answer_id: None | Unset | UUID = UNSET
    answers: list[OfficeAnswerDto] | None | Unset = UNSET
    asker_id: UUID | Unset = UNSET
    content: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    status: OfficeQuestionDetailDtoStatus | Unset = UNSET
    title: None | str | Unset = UNSET
    topics: list[str] | None | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_answer_dto import OfficeAnswerDto # noqa: PLC0415
        accepted_answer_id: None | str | Unset
        if isinstance(self.accepted_answer_id, Unset):
            accepted_answer_id = UNSET
        elif isinstance(self.accepted_answer_id, UUID):
            accepted_answer_id = str(self.accepted_answer_id)
        else:
            accepted_answer_id = self.accepted_answer_id

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

        asker_id: str | Unset = UNSET
        if not isinstance(self.asker_id, Unset):
            asker_id = str(self.asker_id)

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status


        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        topics: list[str] | None | Unset
        if isinstance(self.topics, Unset):
            topics = UNSET
        elif isinstance(self.topics, list):
            topics = self.topics


        else:
            topics = self.topics

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if accepted_answer_id is not UNSET:
            field_dict["acceptedAnswerId"] = accepted_answer_id
        if answers is not UNSET:
            field_dict["answers"] = answers
        if asker_id is not UNSET:
            field_dict["askerId"] = asker_id
        if content is not UNSET:
            field_dict["content"] = content
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if topics is not UNSET:
            field_dict["topics"] = topics
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_answer_dto import OfficeAnswerDto # noqa: PLC0415
        d = dict(src_dict)
        def _parse_accepted_answer_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_answer_id_type_0 = UUID(data)



                return accepted_answer_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        accepted_answer_id = _parse_accepted_answer_id(d.pop("acceptedAnswerId", UNSET))


        def _parse_answers(data: object) -> list[OfficeAnswerDto] | None | Unset:
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
                    answers_type_0_item = OfficeAnswerDto.from_dict(answers_type_0_item_data)



                    answers_type_0.append(answers_type_0_item)

                return answers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeAnswerDto] | None | Unset, data)

        answers = _parse_answers(d.pop("answers", UNSET))


        _asker_id = d.pop("askerId", UNSET)
        asker_id: UUID | Unset
        if isinstance(_asker_id,  Unset):
            asker_id = UNSET
        else:
            asker_id = UUID(_asker_id)




        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _status = d.pop("status", UNSET)
        status: OfficeQuestionDetailDtoStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = check_office_question_detail_dto_status(_status)




        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_topics(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                topics_type_0 = cast(list[str], data)

                return topics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        topics = _parse_topics(d.pop("topics", UNSET))


        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        office_question_detail_dto = cls(
            accepted_answer_id=accepted_answer_id,
            answers=answers,
            asker_id=asker_id,
            content=content,
            created_at=created_at,
            id=id,
            status=status,
            title=title,
            topics=topics,
            updated_at=updated_at,
        )

        return office_question_detail_dto

