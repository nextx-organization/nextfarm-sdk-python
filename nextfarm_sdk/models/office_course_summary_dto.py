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






T = TypeVar("T", bound="OfficeCourseSummaryDto")



@_attrs_define
class OfficeCourseSummaryDto:
    

    allow_retake: bool | Unset = UNSET
    audience_group_codes: list[str] | None | Unset = UNSET
    best_score: int | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    cover_image_url: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    description: None | str | Unset = UNSET
    has_quiz: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    is_enrolled: bool | Unset = UNSET
    lesson_count: int | Unset = UNSET
    passing_score: int | Unset = UNSET
    progress_percent: int | Unset = UNSET
    published_at: datetime.datetime | None | Unset = UNSET
    quiz_passed: bool | None | Unset = UNSET
    status: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        allow_retake = self.allow_retake

        audience_group_codes: list[str] | None | Unset
        if isinstance(self.audience_group_codes, Unset):
            audience_group_codes = UNSET
        elif isinstance(self.audience_group_codes, list):
            audience_group_codes = self.audience_group_codes


        else:
            audience_group_codes = self.audience_group_codes

        best_score: int | None | Unset
        if isinstance(self.best_score, Unset):
            best_score = UNSET
        else:
            best_score = self.best_score

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        cover_image_url: None | str | Unset
        if isinstance(self.cover_image_url, Unset):
            cover_image_url = UNSET
        else:
            cover_image_url = self.cover_image_url

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        has_quiz = self.has_quiz

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_enrolled = self.is_enrolled

        lesson_count = self.lesson_count

        passing_score = self.passing_score

        progress_percent = self.progress_percent

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        elif isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        quiz_passed: bool | None | Unset
        if isinstance(self.quiz_passed, Unset):
            quiz_passed = UNSET
        else:
            quiz_passed = self.quiz_passed

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
        if allow_retake is not UNSET:
            field_dict["allowRetake"] = allow_retake
        if audience_group_codes is not UNSET:
            field_dict["audienceGroupCodes"] = audience_group_codes
        if best_score is not UNSET:
            field_dict["bestScore"] = best_score
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if cover_image_url is not UNSET:
            field_dict["coverImageUrl"] = cover_image_url
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if has_quiz is not UNSET:
            field_dict["hasQuiz"] = has_quiz
        if id is not UNSET:
            field_dict["id"] = id
        if is_enrolled is not UNSET:
            field_dict["isEnrolled"] = is_enrolled
        if lesson_count is not UNSET:
            field_dict["lessonCount"] = lesson_count
        if passing_score is not UNSET:
            field_dict["passingScore"] = passing_score
        if progress_percent is not UNSET:
            field_dict["progressPercent"] = progress_percent
        if published_at is not UNSET:
            field_dict["publishedAt"] = published_at
        if quiz_passed is not UNSET:
            field_dict["quizPassed"] = quiz_passed
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
        allow_retake = d.pop("allowRetake", UNSET)

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


        def _parse_best_score(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        best_score = _parse_best_score(d.pop("bestScore", UNSET))


        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)



                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))


        def _parse_cover_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_image_url = _parse_cover_image_url(d.pop("coverImageUrl", UNSET))


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


        has_quiz = d.pop("hasQuiz", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        is_enrolled = d.pop("isEnrolled", UNSET)

        lesson_count = d.pop("lessonCount", UNSET)

        passing_score = d.pop("passingScore", UNSET)

        progress_percent = d.pop("progressPercent", UNSET)

        def _parse_published_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = datetime.datetime.fromisoformat(data)



                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        published_at = _parse_published_at(d.pop("publishedAt", UNSET))


        def _parse_quiz_passed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        quiz_passed = _parse_quiz_passed(d.pop("quizPassed", UNSET))


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




        office_course_summary_dto = cls(
            allow_retake=allow_retake,
            audience_group_codes=audience_group_codes,
            best_score=best_score,
            completed_at=completed_at,
            cover_image_url=cover_image_url,
            created_at=created_at,
            description=description,
            has_quiz=has_quiz,
            id=id,
            is_enrolled=is_enrolled,
            lesson_count=lesson_count,
            passing_score=passing_score,
            progress_percent=progress_percent,
            published_at=published_at,
            quiz_passed=quiz_passed,
            status=status,
            title=title,
            updated_at=updated_at,
        )

        return office_course_summary_dto

