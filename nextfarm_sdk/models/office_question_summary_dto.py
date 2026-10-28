from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.office_question_summary_dto_status import check_office_question_summary_dto_status
from ..models.office_question_summary_dto_status import OfficeQuestionSummaryDtoStatus
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="OfficeQuestionSummaryDto")



@_attrs_define
class OfficeQuestionSummaryDto:
    

    answer_count: int | Unset = UNSET
    asker_id: UUID | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    has_accepted_answer: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    status: OfficeQuestionSummaryDtoStatus | Unset = UNSET
    title: None | str | Unset = UNSET
    topics: list[str] | None | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        answer_count = self.answer_count

        asker_id: str | Unset = UNSET
        if not isinstance(self.asker_id, Unset):
            asker_id = str(self.asker_id)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        has_accepted_answer = self.has_accepted_answer

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
        if answer_count is not UNSET:
            field_dict["answerCount"] = answer_count
        if asker_id is not UNSET:
            field_dict["askerId"] = asker_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if has_accepted_answer is not UNSET:
            field_dict["hasAcceptedAnswer"] = has_accepted_answer
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
        d = dict(src_dict)
        answer_count = d.pop("answerCount", UNSET)

        _asker_id = d.pop("askerId", UNSET)
        asker_id: UUID | Unset
        if isinstance(_asker_id,  Unset):
            asker_id = UNSET
        else:
            asker_id = UUID(_asker_id)




        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        has_accepted_answer = d.pop("hasAcceptedAnswer", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _status = d.pop("status", UNSET)
        status: OfficeQuestionSummaryDtoStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = check_office_question_summary_dto_status(_status)




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




        office_question_summary_dto = cls(
            answer_count=answer_count,
            asker_id=asker_id,
            created_at=created_at,
            has_accepted_answer=has_accepted_answer,
            id=id,
            status=status,
            title=title,
            topics=topics,
            updated_at=updated_at,
        )

        return office_question_summary_dto

