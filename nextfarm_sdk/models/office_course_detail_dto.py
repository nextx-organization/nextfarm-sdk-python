from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_course_lesson_dto import OfficeCourseLessonDto
  from ..models.office_course_summary_dto import OfficeCourseSummaryDto





T = TypeVar("T", bound="OfficeCourseDetailDto")



@_attrs_define
class OfficeCourseDetailDto:
    

    course: OfficeCourseSummaryDto | Unset = UNSET
    lessons: list[OfficeCourseLessonDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_course_lesson_dto import OfficeCourseLessonDto # noqa: PLC0415
        from ..models.office_course_summary_dto import OfficeCourseSummaryDto # noqa: PLC0415
        course: dict[str, Any] | Unset = UNSET
        if not isinstance(self.course, Unset):
            course = self.course.to_dict()

        lessons: list[dict[str, Any]] | None | Unset
        if isinstance(self.lessons, Unset):
            lessons = UNSET
        elif isinstance(self.lessons, list):
            lessons = []
            for lessons_type_0_item_data in self.lessons:
                lessons_type_0_item = lessons_type_0_item_data.to_dict()
                lessons.append(lessons_type_0_item)


        else:
            lessons = self.lessons


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if course is not UNSET:
            field_dict["course"] = course
        if lessons is not UNSET:
            field_dict["lessons"] = lessons

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_course_lesson_dto import OfficeCourseLessonDto # noqa: PLC0415
        from ..models.office_course_summary_dto import OfficeCourseSummaryDto # noqa: PLC0415
        d = dict(src_dict)
        _course = d.pop("course", UNSET)
        course: OfficeCourseSummaryDto | Unset
        if isinstance(_course,  Unset):
            course = UNSET
        else:
            course = OfficeCourseSummaryDto.from_dict(_course)




        def _parse_lessons(data: object) -> list[OfficeCourseLessonDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                lessons_type_0 = []
                _lessons_type_0 = data
                for lessons_type_0_item_data in (_lessons_type_0):
                    lessons_type_0_item = OfficeCourseLessonDto.from_dict(lessons_type_0_item_data)



                    lessons_type_0.append(lessons_type_0_item)

                return lessons_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeCourseLessonDto] | None | Unset, data)

        lessons = _parse_lessons(d.pop("lessons", UNSET))


        office_course_detail_dto = cls(
            course=course,
            lessons=lessons,
        )

        return office_course_detail_dto

