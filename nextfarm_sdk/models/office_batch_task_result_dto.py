from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.office_batch_task_line_dto import OfficeBatchTaskLineDto
  from ..models.office_task_warning_dto import OfficeTaskWarningDto





T = TypeVar("T", bound="OfficeBatchTaskResultDto")



@_attrs_define
class OfficeBatchTaskResultDto:
    

    created: int | Unset = UNSET
    failed: int | Unset = UNSET
    lines: list[OfficeBatchTaskLineDto] | None | Unset = UNSET
    warnings: list[OfficeTaskWarningDto] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.office_batch_task_line_dto import OfficeBatchTaskLineDto # noqa: PLC0415
        from ..models.office_task_warning_dto import OfficeTaskWarningDto # noqa: PLC0415
        created = self.created

        failed = self.failed

        lines: list[dict[str, Any]] | None | Unset
        if isinstance(self.lines, Unset):
            lines = UNSET
        elif isinstance(self.lines, list):
            lines = []
            for lines_type_0_item_data in self.lines:
                lines_type_0_item = lines_type_0_item_data.to_dict()
                lines.append(lines_type_0_item)


        else:
            lines = self.lines

        warnings: list[dict[str, Any]] | None | Unset
        if isinstance(self.warnings, Unset):
            warnings = UNSET
        elif isinstance(self.warnings, list):
            warnings = []
            for warnings_type_0_item_data in self.warnings:
                warnings_type_0_item = warnings_type_0_item_data.to_dict()
                warnings.append(warnings_type_0_item)


        else:
            warnings = self.warnings


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if created is not UNSET:
            field_dict["created"] = created
        if failed is not UNSET:
            field_dict["failed"] = failed
        if lines is not UNSET:
            field_dict["lines"] = lines
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.office_batch_task_line_dto import OfficeBatchTaskLineDto # noqa: PLC0415
        from ..models.office_task_warning_dto import OfficeTaskWarningDto # noqa: PLC0415
        d = dict(src_dict)
        created = d.pop("created", UNSET)

        failed = d.pop("failed", UNSET)

        def _parse_lines(data: object) -> list[OfficeBatchTaskLineDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                lines_type_0 = []
                _lines_type_0 = data
                for lines_type_0_item_data in (_lines_type_0):
                    lines_type_0_item = OfficeBatchTaskLineDto.from_dict(lines_type_0_item_data)



                    lines_type_0.append(lines_type_0_item)

                return lines_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeBatchTaskLineDto] | None | Unset, data)

        lines = _parse_lines(d.pop("lines", UNSET))


        def _parse_warnings(data: object) -> list[OfficeTaskWarningDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = []
                _warnings_type_0 = data
                for warnings_type_0_item_data in (_warnings_type_0):
                    warnings_type_0_item = OfficeTaskWarningDto.from_dict(warnings_type_0_item_data)



                    warnings_type_0.append(warnings_type_0_item)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OfficeTaskWarningDto] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))


        office_batch_task_result_dto = cls(
            created=created,
            failed=failed,
            lines=lines,
            warnings=warnings,
        )

        return office_batch_task_result_dto

