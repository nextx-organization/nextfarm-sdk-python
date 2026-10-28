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






T = TypeVar("T", bound="OfficeSurveyDto")



@_attrs_define
class OfficeSurveyDto:
    

    audience_group_codes: list[str] | None | Unset = UNSET
    author_id: UUID | Unset = UNSET
    can_manage: bool | Unset = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET
    closes_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    description: None | str | Unset = UNSET
    has_responded: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    is_accepting_responses: bool | Unset = UNSET
    is_anonymous: bool | Unset = UNSET
    opened_at: datetime.datetime | None | Unset = UNSET
    question_count: int | Unset = UNSET
    response_count: int | Unset = UNSET
    status: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        audience_group_codes: list[str] | None | Unset
        if isinstance(self.audience_group_codes, Unset):
            audience_group_codes = UNSET
        elif isinstance(self.audience_group_codes, list):
            audience_group_codes = self.audience_group_codes


        else:
            audience_group_codes = self.audience_group_codes

        author_id: str | Unset = UNSET
        if not isinstance(self.author_id, Unset):
            author_id = str(self.author_id)

        can_manage = self.can_manage

        closed_at: None | str | Unset
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        closes_at: None | str | Unset
        if isinstance(self.closes_at, Unset):
            closes_at = UNSET
        elif isinstance(self.closes_at, datetime.datetime):
            closes_at = self.closes_at.isoformat()
        else:
            closes_at = self.closes_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        has_responded = self.has_responded

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_accepting_responses = self.is_accepting_responses

        is_anonymous = self.is_anonymous

        opened_at: None | str | Unset
        if isinstance(self.opened_at, Unset):
            opened_at = UNSET
        elif isinstance(self.opened_at, datetime.datetime):
            opened_at = self.opened_at.isoformat()
        else:
            opened_at = self.opened_at

        question_count = self.question_count

        response_count = self.response_count

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if audience_group_codes is not UNSET:
            field_dict["audienceGroupCodes"] = audience_group_codes
        if author_id is not UNSET:
            field_dict["authorId"] = author_id
        if can_manage is not UNSET:
            field_dict["canManage"] = can_manage
        if closed_at is not UNSET:
            field_dict["closedAt"] = closed_at
        if closes_at is not UNSET:
            field_dict["closesAt"] = closes_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if has_responded is not UNSET:
            field_dict["hasResponded"] = has_responded
        if id is not UNSET:
            field_dict["id"] = id
        if is_accepting_responses is not UNSET:
            field_dict["isAcceptingResponses"] = is_accepting_responses
        if is_anonymous is not UNSET:
            field_dict["isAnonymous"] = is_anonymous
        if opened_at is not UNSET:
            field_dict["openedAt"] = opened_at
        if question_count is not UNSET:
            field_dict["questionCount"] = question_count
        if response_count is not UNSET:
            field_dict["responseCount"] = response_count
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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


        _author_id = d.pop("authorId", UNSET)
        author_id: UUID | Unset
        if isinstance(_author_id,  Unset):
            author_id = UNSET
        else:
            author_id = UUID(_author_id)




        can_manage = d.pop("canManage", UNSET)

        def _parse_closed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = datetime.datetime.fromisoformat(data)



                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closed_at = _parse_closed_at(d.pop("closedAt", UNSET))


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


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        has_responded = d.pop("hasResponded", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_accepting_responses = d.pop("isAcceptingResponses", UNSET)

        is_anonymous = d.pop("isAnonymous", UNSET)

        def _parse_opened_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opened_at_type_0 = datetime.datetime.fromisoformat(data)



                return opened_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        opened_at = _parse_opened_at(d.pop("openedAt", UNSET))


        question_count = d.pop("questionCount", UNSET)

        response_count = d.pop("responseCount", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        office_survey_dto = cls(
            audience_group_codes=audience_group_codes,
            author_id=author_id,
            can_manage=can_manage,
            closed_at=closed_at,
            closes_at=closes_at,
            created_at=created_at,
            description=description,
            has_responded=has_responded,
            id=id,
            is_accepting_responses=is_accepting_responses,
            is_anonymous=is_anonymous,
            opened_at=opened_at,
            question_count=question_count,
            response_count=response_count,
            status=status,
            title=title,
            updated_at=updated_at,
        )

        return office_survey_dto

