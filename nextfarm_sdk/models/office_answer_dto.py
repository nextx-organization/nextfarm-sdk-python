from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="OfficeAnswerDto")



@_attrs_define
class OfficeAnswerDto:
    

    answerer_id: UUID | Unset = UNSET
    content: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    is_accepted: bool | Unset = UNSET
    like_count: int | Unset = UNSET
    liked_by_me: bool | Unset = UNSET
    question_id: UUID | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        answerer_id: str | Unset = UNSET
        if not isinstance(self.answerer_id, Unset):
            answerer_id = str(self.answerer_id)

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

        is_accepted = self.is_accepted

        like_count = self.like_count

        liked_by_me = self.liked_by_me

        question_id: str | Unset = UNSET
        if not isinstance(self.question_id, Unset):
            question_id = str(self.question_id)

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if answerer_id is not UNSET:
            field_dict["answererId"] = answerer_id
        if content is not UNSET:
            field_dict["content"] = content
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if is_accepted is not UNSET:
            field_dict["isAccepted"] = is_accepted
        if like_count is not UNSET:
            field_dict["likeCount"] = like_count
        if liked_by_me is not UNSET:
            field_dict["likedByMe"] = liked_by_me
        if question_id is not UNSET:
            field_dict["questionId"] = question_id
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _answerer_id = d.pop("answererId", UNSET)
        answerer_id: UUID | Unset
        if isinstance(_answerer_id,  Unset):
            answerer_id = UNSET
        else:
            answerer_id = UUID(_answerer_id)




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




        is_accepted = d.pop("isAccepted", UNSET)

        like_count = d.pop("likeCount", UNSET)

        liked_by_me = d.pop("likedByMe", UNSET)

        _question_id = d.pop("questionId", UNSET)
        question_id: UUID | Unset
        if isinstance(_question_id,  Unset):
            question_id = UNSET
        else:
            question_id = UUID(_question_id)




        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        office_answer_dto = cls(
            answerer_id=answerer_id,
            content=content,
            created_at=created_at,
            id=id,
            is_accepted=is_accepted,
            like_count=like_count,
            liked_by_me=liked_by_me,
            question_id=question_id,
            updated_at=updated_at,
        )

        return office_answer_dto

