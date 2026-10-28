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
  from ..models.office_course_completion_row_dto import OfficeCourseCompletionRowDto





T = TypeVar("T", bound="OfficeCourseCompletionReportDto")



@_attrs_define
class OfficeCourseCompletionReportDto:
    

    audience_count: int | Unset = UNSET
    audience_resolved: bool | Unset = UNSET
    completed_count: int | Unset = UNSET
    course_id: UUID | Unset = UNSET
    course_title: None | str | Unset = UNSET
    has_quiz: bool | Unset = UNSET
    in_progress_count: int | Unset = UNSET
    lesson_count: int | Unset = UNSET
    not_started_count: int | Unset = UNSET
    rows: list[OfficeCourseCompletionRowDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_course_completion_row_dto import OfficeCourseCompletionRowDto # noqa: PLC0415
        audience_count = self.audience_count

        audience_resolved = self.audience_resolved

        completed_count = self.completed_count

        course_id: str | Unset = UNSET
        if not isinstance(self.course_id, Unset):
            course_id = str(self.course_id)

        course_title: None | str | Unset
        if isinstance(self.course_title, Unset):
            course_title = UNSET
        else:
            course_title = self.course_title

        has_quiz = self.has_quiz

        in_progress_count = self.in_progress_count

        lesson_count = self.lesson_count

        not_started_count = self.not_started_count

        rows: list[dict[str, Any]] | None | Unset
        if isinstance(self.rows, Unset):
            rows = UNSET
        elif isinstance(self.rows, list):
            rows = []
            for rows_type_0_item_data in self.rows:
                rows_type_0_item = rows_type_0_item_data.to_dict()
                rows.append(rows_type_0_item)


        else:
            rows = self.rows


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if audience_count is not UNSET:
            field_dict["audienceCount"] = audience_count
        if audience_resolved is not UNSET:
            field_dict["audienceResolved"] = audience_resolved
        if completed_count is not UNSET:
            field_dict["completedCount"] = completed_count
        if course_id is not UNSET:
            field_dict["courseId"] = course_id
        if course_title is not UNSET:
            field_dict["courseTitle"] = course_title
        if has_quiz is not UNSET:
            field_dict["hasQuiz"] = has_quiz
        if in_progress_count is not UNSET:
            field_dict["inProgressCount"] = in_progress_count
        if lesson_count is not UNSET:
            field_dict["lessonCount"] = lesson_count
        if not_started_count is not UNSET:
            field_dict["notStartedCount"] = not_started_count
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_course_completion_row_dto import OfficeCourseCompletionRowDto # noqa: PLC0415
        d = dict(src_dict)
        audience_count = d.pop("audienceCount", UNSET)

        audience_resolved = d.pop("audienceResolved", UNSET)

        completed_count = d.pop("completedCount", UNSET)

        _course_id = d.pop("courseId", UNSET)
        course_id: UUID | Unset
        if isinstance(_course_id,  Unset):
            course_id = UNSET
        else:
            course_id = UUID(_course_id)




        def _parse_course_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        course_title = _parse_course_title(d.pop("courseTitle", UNSET))


        has_quiz = d.pop("hasQuiz", UNSET)

        in_progress_count = d.pop("inProgressCount", UNSET)

        lesson_count = d.pop("lessonCount", UNSET)

        not_started_count = d.pop("notStartedCount", UNSET)

        def _parse_rows(data: object) -> list[OfficeCourseCompletionRowDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rows_type_0 = []
                _rows_type_0 = data
                for rows_type_0_item_data in (_rows_type_0):
                    rows_type_0_item = OfficeCourseCompletionRowDto.from_dict(rows_type_0_item_data)



                    rows_type_0.append(rows_type_0_item)

                return rows_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeCourseCompletionRowDto] | None | Unset, data)

        rows = _parse_rows(d.pop("rows", UNSET))


        office_course_completion_report_dto = cls(
            audience_count=audience_count,
            audience_resolved=audience_resolved,
            completed_count=completed_count,
            course_id=course_id,
            course_title=course_title,
            has_quiz=has_quiz,
            in_progress_count=in_progress_count,
            lesson_count=lesson_count,
            not_started_count=not_started_count,
            rows=rows,
        )

        return office_course_completion_report_dto

