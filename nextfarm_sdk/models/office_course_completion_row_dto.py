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






T = TypeVar("T", bound="OfficeCourseCompletionRowDto")



@_attrs_define
class OfficeCourseCompletionRowDto:
    

    best_score: int | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    display_name: None | str | Unset = UNSET
    is_enrolled: bool | Unset = UNSET
    last_activity_at: datetime.datetime | None | Unset = UNSET
    progress_percent: int | Unset = UNSET
    quiz_passed: bool | None | Unset = UNSET
    user_id: UUID | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
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

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        is_enrolled = self.is_enrolled

        last_activity_at: None | str | Unset
        if isinstance(self.last_activity_at, Unset):
            last_activity_at = UNSET
        elif isinstance(self.last_activity_at, datetime.datetime):
            last_activity_at = self.last_activity_at.isoformat()
        else:
            last_activity_at = self.last_activity_at

        progress_percent = self.progress_percent

        quiz_passed: bool | None | Unset
        if isinstance(self.quiz_passed, Unset):
            quiz_passed = UNSET
        else:
            quiz_passed = self.quiz_passed

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if best_score is not UNSET:
            field_dict["bestScore"] = best_score
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if is_enrolled is not UNSET:
            field_dict["isEnrolled"] = is_enrolled
        if last_activity_at is not UNSET:
            field_dict["lastActivityAt"] = last_activity_at
        if progress_percent is not UNSET:
            field_dict["progressPercent"] = progress_percent
        if quiz_passed is not UNSET:
            field_dict["quizPassed"] = quiz_passed
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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


        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))


        is_enrolled = d.pop("isEnrolled", UNSET)

        def _parse_last_activity_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_activity_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_activity_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_activity_at = _parse_last_activity_at(d.pop("lastActivityAt", UNSET))


        progress_percent = d.pop("progressPercent", UNSET)

        def _parse_quiz_passed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        quiz_passed = _parse_quiz_passed(d.pop("quizPassed", UNSET))


        _user_id = d.pop("userId", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id,  Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)




        office_course_completion_row_dto = cls(
            best_score=best_score,
            completed_at=completed_at,
            display_name=display_name,
            is_enrolled=is_enrolled,
            last_activity_at=last_activity_at,
            progress_percent=progress_percent,
            quiz_passed=quiz_passed,
            user_id=user_id,
        )

        return office_course_completion_row_dto

